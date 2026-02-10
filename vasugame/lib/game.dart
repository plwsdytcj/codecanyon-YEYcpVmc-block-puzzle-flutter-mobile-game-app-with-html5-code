import 'package:flutter/material.dart';
import 'package:webview_flutter_plus/webview_flutter_plus.dart';
import 'package:flutter/services.dart';
import 'ad_manager.dart';

class MainPage extends StatefulWidget {
  @override
  State<MainPage> createState() => _MainPageState();
}

class _MainPageState extends State<MainPage> with WidgetsBindingObserver {
  late WebViewControllerPlus _controller;
  bool _isLoading = true;
  bool _hasError = false;
  String? _errorDescription;
  Future<void>? _watchdog;

  @override
  void initState() {
    super.initState();
    WidgetsBinding.instance.addObserver(this);

    _controller = WebViewControllerPlus()
      ..setJavaScriptMode(JavaScriptMode.unrestricted)
      ..setBackgroundColor(const Color(0xFF000000)) // 改为黑色背景，提升性能
      ..setNavigationDelegate(
        NavigationDelegate(
          onPageStarted: (url) {
            setState(() {
              _isLoading = true;
              _hasError = false;
              _errorDescription = null;
            });
          },
          onProgress: (progress) {
            // 进度到 90% 先行隐藏 loading，避免 onPageFinished 未回调导致长时间等待
            if (progress >= 90 && _isLoading && mounted) {
              setState(() {
                _isLoading = false;
              });
            }
          },
          onPageFinished: (url) {
            if (mounted) {
              setState(() {
                _isLoading = false;
              });
            }
          },
          onWebResourceError: (error) {
            if (mounted) {
              setState(() {
                _hasError = true;
                _isLoading = false;
                _errorDescription = error.description;
              });
            }
          },
        ),
      )
      ..addJavaScriptChannel(
        'AdMobChannel',
        onMessageReceived: (JavaScriptMessage message) {
          _handleAdRequest(message.message);
        },
      )
      ..loadFlutterAssetServer('lib/Game/index.html');

    // Watchdog：极端情况下未触发 onPageFinished，最多等待 6 秒
    _watchdog = Future.delayed(const Duration(seconds: 6), () {
      if (mounted && _isLoading && !_hasError) {
        setState(() {
          _isLoading = false;
        });
      }
    });

    // 设置系统 UI 模式 - 只在初始化时设置一次
    SystemChrome.setEnabledSystemUIMode(
      SystemUiMode.manual,
      overlays: [SystemUiOverlay.top],
    );
    SystemChrome.setSystemUIOverlayStyle(const SystemUiOverlayStyle(
      statusBarColor: Colors.transparent,
    ));
  }

  // 处理来自 JavaScript 的广告请求
  void _handleAdRequest(String message) async {
    print('📱 收到广告请求: $message');

    if (message == 'showRewardedAd') {
      bool rewarded = await AdManager().showRewardedAd();
      if (rewarded) {
        // 通知 JavaScript 用户获得了奖励
        _controller.runJavaScript('onAdRewardEarned()');
      } else {
        // 未获得奖励或未显示成功时，通知 JS 以便回调链能结束
        _controller.runJavaScript('if (typeof onAdRewardDismissed === "function") { onAdRewardDismissed(); }');
      }
    } else if (message == 'showInterstitialAd') {
      await AdManager().showInterstitialAd();
    } else if (message == 'isRewardedAdReady') {
      bool isReady = AdManager().isRewardedAdReady;
      _controller.runJavaScript('onAdReadyStatusChanged($isReady)');
    }
  }

  // 处理应用生命周期变化
  @override
  void didChangeAppLifecycleState(AppLifecycleState state) {
    super.didChangeAppLifecycleState(state);

    // 当应用恢复时（例如截图后），确保游戏继续运行
    if (state == AppLifecycleState.resumed) {
      // 延迟一小段时间后恢复游戏，确保系统 UI 已稳定
      Future.delayed(const Duration(milliseconds: 100), () {
        _controller.runJavaScript('if(window.game && window.game.unpauseGame) { window.game.unpauseGame(true); }');
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black,
      body: Stack(
        children: [
          WebViewWidget(controller: _controller),
          if (_isLoading)
            const Center(
              child: CircularProgressIndicator(color: Colors.white),
            ),
          if (_hasError)
            Center(
              child: Column(
                mainAxisSize: MainAxisSize.min,
                children: [
                  const Text(
                    '加载失败',
                    style: TextStyle(color: Colors.white, fontSize: 18),
                  ),
                  if (_errorDescription != null) ...[
                    const SizedBox(height: 8),
                    Padding(
                      padding: const EdgeInsets.symmetric(horizontal: 24.0),
                      child: Text(
                        _errorDescription!,
                        style: const TextStyle(color: Colors.white70, fontSize: 14),
                        textAlign: TextAlign.center,
                      ),
                    ),
                  ],
                  const SizedBox(height: 16),
                  ElevatedButton(
                    onPressed: () {
                      setState(() {
                        _hasError = false;
                        _isLoading = true;
                        _errorDescription = null;
                      });
                      _controller.reload();
                    },
                    child: const Text('重试'),
                  ),
                ],
              ),
            ),
        ],
      ),
    );
  }

  @override
  void dispose() {
    WidgetsBinding.instance.removeObserver(this);
    _controller.server.close();
    super.dispose();
  }
}
