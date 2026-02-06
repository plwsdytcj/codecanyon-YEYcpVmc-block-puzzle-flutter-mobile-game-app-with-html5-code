// AdMob JavaScript 桥接接口
// 用于 HTML5 游戏调用 Flutter 的 AdMob 广告

window.FlutterAdMob = {
    // 显示激励视频广告
    showRewardedAd: function() {
        if (window.AdMobChannel) {
            window.AdMobChannel.postMessage('showRewardedAd');
        } else {
            console.log('⚠️ AdMob 未初始化');
        }
    },

    // 显示插屏广告
    showInterstitialAd: function() {
        if (window.AdMobChannel) {
            window.AdMobChannel.postMessage('showInterstitialAd');
        } else {
            console.log('⚠️ AdMob 未初始化');
        }
    },

    // 检查激励视频是否准备好
    checkRewardedAdReady: function() {
        if (window.AdMobChannel) {
            window.AdMobChannel.postMessage('isRewardedAdReady');
        } else {
            console.log('⚠️ AdMob 未初始化');
        }
    }
};

// 由 Flutter 维护的 AdMob 状态（只存放必要的同步标志）
window.FlutterAdMobState = {
    rewardedReady: false
};

// 当用户获得广告奖励时的回调（由 Flutter 调用）
window.onAdRewardEarned = function() {
    console.log('🎁 用户获得广告奖励！');
    // 通知 famobi 回调链，发放奖励并结束广告流程
    if (typeof window.showRewarded_adViewed === 'function') {
        try { window.showRewarded_adViewed(); } catch(e) { console.log(e); }
    }
};

// 当用户关闭广告且未获得奖励（由 Flutter 调用）
window.onAdRewardDismissed = function() {
    console.log('ℹ️ 用户关闭广告，未获得奖励');
    if (typeof window.showRewarded_adDismissed === 'function') {
        try { window.showRewarded_adDismissed(); } catch(e) { console.log(e); }
    }
};

// 广告准备状态回调（由 Flutter 调用）
window.onAdReadyStatusChanged = function(isReady) {
    console.log('📱 广告准备状态:', isReady);
    window.FlutterAdMobState.rewardedReady = !!isReady;
};

console.log('✅ AdMob JavaScript 桥接已加载');
