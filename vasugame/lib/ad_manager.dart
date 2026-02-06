import 'dart:io';
import 'package:google_mobile_ads/google_mobile_ads.dart';

class AdManager {
  static final AdManager _instance = AdManager._internal();
  factory AdManager() => _instance;
  AdManager._internal();

  RewardedAd? _rewardedAd;
  InterstitialAd? _interstitialAd;
  bool _isRewardedAdReady = false;
  bool _isInterstitialAdReady = false;

  // 测试广告 ID（开发时使用）
  // 上线前需要替换为你在 AdMob 控制台创建的真实广告 ID
  static String get rewardedAdUnitId {
    if (Platform.isAndroid) {
      return 'ca-app-pub-5937681356868683/3256385858'; // Android 测试 ID
    } else if (Platform.isIOS) {
      return 'ca-app-pub-5937681356868683/1460078715'; // iOS 测试 ID
    }
    return '';
  }

  static String get interstitialAdUnitId {
    if (Platform.isAndroid) {
      return 'ca-app-pub-5937681356868683/8867805185'; // Android 测试 ID
    } else if (Platform.isIOS) {
      return 'ca-app-pub-5937681356868683/6341714198'; // iOS 测试 ID
    }
    return '';
  }

  // 初始化 AdMob
  Future<void> initialize() async {
    await MobileAds.instance.initialize();
    loadRewardedAd();
    loadInterstitialAd();
  }

  // 加载激励视频广告
  void loadRewardedAd() {
    RewardedAd.load(
      adUnitId: rewardedAdUnitId,
      request: const AdRequest(),
      rewardedAdLoadCallback: RewardedAdLoadCallback(
        onAdLoaded: (ad) {
          _rewardedAd = ad;
          _isRewardedAdReady = true;
          print('✅ 激励视频广告加载成功');

          _rewardedAd!.fullScreenContentCallback = FullScreenContentCallback(
            onAdDismissedFullScreenContent: (ad) {
              ad.dispose();
              _isRewardedAdReady = false;
              loadRewardedAd(); // 重新加载下一个广告
            },
            onAdFailedToShowFullScreenContent: (ad, error) {
              print('❌ 激励视频广告显示失败: $error');
              ad.dispose();
              _isRewardedAdReady = false;
              loadRewardedAd();
            },
          );
        },
        onAdFailedToLoad: (error) {
          print('❌ 激励视频广告加载失败: $error');
          _isRewardedAdReady = false;
          // 5秒后重试
          Future.delayed(const Duration(seconds: 5), () {
            loadRewardedAd();
          });
        },
      ),
    );
  }

  // 显示激励视频广告
  Future<bool> showRewardedAd() async {
    if (!_isRewardedAdReady || _rewardedAd == null) {
      print('⚠️ 激励视频广告未准备好');
      return false;
    }

    bool rewardEarned = false;

    await _rewardedAd!.show(
      onUserEarnedReward: (ad, reward) {
        print('🎁 用户获得奖励: ${reward.amount} ${reward.type}');
        rewardEarned = true;
      },
    );

    return rewardEarned;
  }

  // 加载插屏广告
  void loadInterstitialAd() {
    InterstitialAd.load(
      adUnitId: interstitialAdUnitId,
      request: const AdRequest(),
      adLoadCallback: InterstitialAdLoadCallback(
        onAdLoaded: (ad) {
          _interstitialAd = ad;
          _isInterstitialAdReady = true;
          print('✅ 插屏广告加载成功');

          _interstitialAd!.fullScreenContentCallback = FullScreenContentCallback(
            onAdDismissedFullScreenContent: (ad) {
              ad.dispose();
              _isInterstitialAdReady = false;
              loadInterstitialAd();
            },
            onAdFailedToShowFullScreenContent: (ad, error) {
              print('❌ 插屏广告显示失败: $error');
              ad.dispose();
              _isInterstitialAdReady = false;
              loadInterstitialAd();
            },
          );
        },
        onAdFailedToLoad: (error) {
          print('❌ 插屏广告加载失败: $error');
          _isInterstitialAdReady = false;
        },
      ),
    );
  }

  // 显示插屏广告
  Future<void> showInterstitialAd() async {
    if (!_isInterstitialAdReady || _interstitialAd == null) {
      print('⚠️ 插屏广告未准备好');
      return;
    }

    await _interstitialAd!.show();
  }

  // 检查激励视频是否准备好
  bool get isRewardedAdReady => _isRewardedAdReady;

  // 检查插屏广告是否准备好
  bool get isInterstitialAdReady => _isInterstitialAdReady;

  // 释放资源
  void dispose() {
    _rewardedAd?.dispose();
    _interstitialAd?.dispose();
  }
}
