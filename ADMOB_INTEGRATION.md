# AdMob 集成完成 ✅

## 📱 已完成的配置

### 1. **依赖安装**
- ✅ 添加 `google_mobile_ads: ^5.3.1` 到 pubspec.yaml
- ✅ 运行 `flutter pub get` 安装依赖

### 2. **Android 配置**
- ✅ 在 `AndroidManifest.xml` 中添加 AdMob App ID
- ✅ 当前使用测试 ID：`ca-app-pub-3940256099942544~3347511713`

### 3. **iOS 配置**
- ✅ 在 `Info.plist` 中添加 AdMob App ID
- ✅ 添加 SKAdNetwork 配置
- ✅ 当前使用测试 ID：`ca-app-pub-3940256099942544~1458002511`

### 4. **代码集成**
- ✅ 创建 `ad_manager.dart` 广告管理类
- ✅ 在 `main.dart` 中初始化 AdMob
- ✅ 在 `game.dart` 中添加 JavaScript 桥接
- ✅ 创建 `admob_bridge.js` JavaScript 接口
- ✅ 在 `index.html` 中引入桥接脚本

---

## 🎮 如何在游戏中调用广告

### JavaScript 调用方式

在你的游戏代码中（例如 `game.js` 或 `custom.js`），可以这样调用广告：

```javascript
// 显示激励视频广告（用户观看后获得奖励）
window.FlutterAdMob.showRewardedAd();

// 显示插屏广告（全屏广告）
window.FlutterAdMob.showInterstitialAd();

// 检查激励视频是否准备好
window.FlutterAdMob.checkRewardedAdReady();
```

### 示例：在游戏中添加"观看广告获得星星"按钮

```javascript
// 当用户点击"观看广告"按钮时
function onWatchAdButtonClick() {
    console.log('用户点击观看广告按钮');
    window.FlutterAdMob.showRewardedAd();
}

// 当用户获得广告奖励时（自动调用）
window.onAdRewardEarned = function() {
    console.log('🎁 用户获得广告奖励！');
    // 奖励用户 10 个星星
    addStars(10);
    // 显示提示信息
    showMessage('恭喜！你获得了 10 个星星！');
};
```

---

## 🧪 测试广告

### 当前使用的是 Google 测试广告 ID

**Android 测试 ID：**
- App ID: `ca-app-pub-3940256099942544~3347511713`
- Rewarded Ad: `ca-app-pub-3940256099942544/5224354917`
- Interstitial Ad: `ca-app-pub-3940256099942544/1033173712`

**iOS 测试 ID：**
- App ID: `ca-app-pub-3940256099942544~1458002511`
- Rewarded Ad: `ca-app-pub-3940256099942544/1712485313`
- Interstitial Ad: `ca-app-pub-3940256099942544/4411468910`

### 测试步骤

1. **重新构建应用**
   ```bash
   flutter clean
   flutter run -d emulator-5554
   ```

2. **在游戏中触发广告**
   - 打开浏览器控制台（如果有）
   - 调用 `window.FlutterAdMob.showRewardedAd()`
   - 应该会看到 Google 测试广告

3. **查看日志**
   ```bash
   adb logcat | grep -i "admob\|ad"
   ```

---

## 🚀 上线前需要做的事

### 1. **注册 AdMob 账号并创建应用**
   - 访问 [admob.google.com](https://admob.google.com/)
   - 创建新应用
   - 获取真实的 App ID 和 Ad Unit IDs

### 2. **替换测试 ID 为真实 ID**

**Android (`AndroidManifest.xml`):**
```xml
<meta-data
    android:name="com.google.android.gms.ads.APPLICATION_ID"
    android:value="你的真实 Android App ID"/>
```

**iOS (`Info.plist`):**
```xml
<key>GADApplicationIdentifier</key>
<string>你的真实 iOS App ID</string>
```

**广告单元 ID (`ad_manager.dart`):**
```dart
static String get rewardedAdUnitId {
  if (Platform.isAndroid) {
    return '你的 Android 激励视频 ID';
  } else if (Platform.isIOS) {
    return '你的 iOS 激励视频 ID';
  }
  return '';
}
```

### 3. **测试真实广告**
   - 使用真实设备测试
   - 确保广告正常显示
   - 验证奖励逻辑正确

### 4. **遵守 AdMob 政策**
   - 不要在广告上点击自己的广告
   - 不要鼓励用户点击广告
   - 确保广告位置符合政策要求

---

## 📊 广告类型说明

### 激励视频广告（Rewarded Video）
- ✅ 用户主动观看
- ✅ 观看完整后获得奖励
- ✅ 用户体验好
- ✅ 收益高
- **推荐使用场景**：获得星星、解锁关卡、复活等

### 插屏广告（Interstitial）
- ⚠️ 全屏广告
- ⚠️ 可能影响用户体验
- ⚠️ 需要控制频率
- **推荐使用场景**：游戏结束、关卡切换等

---

## 🔧 故障排除

### 广告不显示？
1. 检查网络连接
2. 确认 AdMob App ID 正确
3. 查看 logcat 日志
4. 确认广告已加载（需要几秒钟）

### JavaScript 调用无效？
1. 检查 `admob_bridge.js` 是否正确加载
2. 打开浏览器控制台查看错误
3. 确认 `AdMobChannel` 已注册

### 测试广告不显示？
1. 使用真实设备或模拟器（不是浏览器）
2. 确保使用 Google 测试 ID
3. 等待几秒让广告加载

---

## 📞 需要帮助？

如果遇到问题，请提供：
1. 错误日志（logcat）
2. 具体的错误信息
3. 你想实现的功能

---

**集成完成！现在你可以测试 AdMob 广告了！** 🎉
