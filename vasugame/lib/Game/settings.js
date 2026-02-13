const enable_rewarded_videos = true; // set false to disable this feature completely
const difficulty_level = 2; // an integer value from 1 to 10, where 1 means the easiest difficulty curve, 10 - the hardest one.
const bomb_powerup_basic_price = 15; // how many stars costs bomb powerup
const bomb_powerup_price_step = 5; // for how many stars will the bomb powerup price increase with each next purchase. E.g. If starting price is 15 and step is 5, the prices after each next purchase of the powerup will look like 15, 20, 25, 30 etc...
const lightning_powerup_basic_price = 25; // how many stars costs lightning powerup
const lightning_powerup_price_step = 5; // for how many stars will the lightning powerup price increase with each next purchase. E.g. If starting price is 25 and step is 5, the prices after each next purchase of the powerup will look like 25, 30, 35, 40 etc...
const get_stars_button_cooldown = 300; //  how often will the "Get Free stars for watching video" button appear, in seconds. Default value is once per 300 seconds (5 minutes). Set 0 to completely disable this button
const get_stars_button_basic_reward = 5; //  how many stars will user get for watching first video ads after he pressed the "Get free stars" button.
const get_stars_button_reward_step = 5; //  each next video watched by pressing "Get free stars" button will give more stars. Default value is 5, which means each next video will give 5 more stars (5, 10, 15, 20 etc). Set to 0 to disable increasing reward and keep it constant.
const results_watch_video_reward = 10; //  how many stars player receives for watching rewarded video by pressing "Watch video" button on results screen

// 性能优化设置 - Performance optimization settings
const ENABLE_PARTICLES = true; // 设置为false可以禁用粒子效果以提升性能
const ENABLE_ANIMATIONS = true; // 设置为false可以禁用部分动画以提升性能
const REDUCE_EFFECTS = false; // 设置为true可以减少特效数量

// 触控拖拽偏移（防手指遮挡）
// - dynamic_drag_offset_enabled: true 启用“越往屏幕上方偏移越大”的动态策略；false 使用固定偏移
// - drag_offset_bottom_factor: 底部区域的偏移倍数（1.0=保持初始）
// - drag_offset_top_factor: 顶部区域的偏移倍数（建议 1.4 - 2.0）
// - drag_offset_smoothing: 平滑系数 0-1，越小越平滑
const dynamic_drag_offset_enabled = true;
const drag_offset_bottom_factor = 1.0;
const drag_offset_top_factor = 1.3; // 降低顶部偏移强度，手感更跟手
const drag_offset_smoothing = 0.6;   // 提升响应（0=很黏滞，1=立即到位）

// 固定偏移量（当 dynamic_drag_offset_enabled=false 时生效）
// 负值表示方块相对手指向上偏移，单位：像素（基于游戏坐标的缩放前像素）
const figure_view_dragging_delta = -80;

// 指数缓冲拖拽偏移（启用则覆盖上方动态偏移策略）
// d2(Δy) = d1 + maxExtra × (1 - e^(-k × Δy))
// - drag_expo_enabled: 是否启用指数偏移
// - drag_expo_max_extra: 最大额外偏移（像素）
// - drag_expo_k: 衰减系数（越大越快接近上限）
const drag_expo_enabled = true;
const drag_expo_max_extra = 50;      // 降低额外偏移上限，避免“漂移感”
const drag_expo_k = 0.012;           // 放缓指数增长，减小向上拖拽的放大效应
