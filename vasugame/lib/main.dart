import 'package:flutter/material.dart';
// Platform-specific WebView tuning can be enabled when needed.
import 'game.dart';
import 'ad_manager.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  // 如需启用 Android Surface 组合或其他 WebView 优化，请告知我来按插件版本适配。
  runApp(const MyApp());
  // 广告初始化放到首帧之后执行，避免首屏阻塞
  WidgetsBinding.instance.addPostFrameCallback((_) {
    AdManager().initialize();
  });
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: MainPage(),
    );
  }
}
