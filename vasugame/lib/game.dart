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
            // Add any necessary logic when a new page starts loading
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
      body: WebViewWidget(
        controller: _controller,
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
