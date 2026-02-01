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

// 当用户获得广告奖励时的回调（由 Flutter 调用）
window.onAdRewardEarned = function() {
    console.log('🎁 用户获得广告奖励！');
    // 在这里添加奖励逻辑，例如增加星星
    if (typeof addStars === 'function') {
        addStars(10); // 奖励 10 个星星
    }
};

// 广告准备状态回调（由 Flutter 调用）
window.onAdReadyStatusChanged = function(isReady) {
    console.log('📱 广告准备状态:', isReady);
};

console.log('✅ AdMob JavaScript 桥接已加载');
