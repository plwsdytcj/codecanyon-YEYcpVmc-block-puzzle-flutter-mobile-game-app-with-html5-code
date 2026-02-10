import 'package:flutter/material.dart';
import 'game.dart';
import 'ad_manager.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();
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
