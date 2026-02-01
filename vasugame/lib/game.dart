import 'package:flutter/material.dart';
import 'package:webview_flutter_plus/webview_flutter_plus.dart';
import 'package:flutter/services.dart';
import 'ad_manager.dart';

class MainPage extends StatefulWidget {
  @override
  State<MainPage> createState() => _MainPageState();
}

class _MainPageState extends State<MainPage> {
  late WebViewControllerPlus _controller;

  @override
  void initState() {
    _controller = WebViewControllerPlus()
      ..setJavaScriptMode(JavaScriptMode.unrestricted)
      ..setBackgroundColor(const Color(0x00000000))
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
    super.initState();
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
      }
    } else if (message == 'showInterstitialAd') {
      await AdManager().showInterstitialAd();
    } else if (message == 'isRewardedAdReady') {
      bool isReady = AdManager().isRewardedAdReady;
      _controller.runJavaScript('onAdReadyStatusChanged($isReady)');
    }
  }

  @override
  Widget build(BuildContext context) {
    SystemChrome.setEnabledSystemUIMode(SystemUiMode.manual,
        overlays: [SystemUiOverlay.top]);
    return Scaffold(
      body: WebViewWidget(
        controller: _controller,
      ),
    );
  }

  @override
  void dispose() {
    _controller.server.close();
    super.dispose();
  }
}
