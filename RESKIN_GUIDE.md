# Block Puzzle Flutter Game - Reskin 完整指南

## 📋 项目概述

这是一个 Flutter 包装的 HTML5/Phaser.js 方块拼图游戏。游戏主体使用 Phaser 游戏引擎开发，通过 Flutter WebView 在移动端运行。

**项目结构**:
- **Flutter 层**: `vasugame/lib/` - 应用外壳和 WebView 容器
- **游戏层**: `vasugame/lib/Game/` - HTML5 游戏核心
- **资源文件**: 精灵图集、音频、字体等

---

## 🎯 Reskin 工作量评估

### 最小化 Reskin（推荐新手）
**工作量**: 1-2 天
**改动**: 10-15 个文件
- 方块颜色（7个）
- 背景图（1个）
- 应用图标
- 游戏标题

### 中度 Reskin
**工作量**: 3-5 天
**改动**: 60-80 个图形元素
- 方块 + 特效
- 主要按钮
- 图标
- 窗口背景

### 完全 Reskin
**工作量**: 1-2 周
**改动**: 592 个图形元素
- 全部 325 个 UI 精灵
- 全部 267 个动画帧
- 所有配置和资源

---

## 📁 核心文件清单

### 1. 游戏精灵图集（最重要）

#### assets.png - 主 UI 精灵图集

**文件路径**: `vasugame/lib/Game/img/assets.png`
**文件大小**: 335 KB
**精灵数量**: 325 个
**配置文件**: `vasugame/lib/Game/img/assets.json`

**包含的精灵类别**:

| 类别 | 数量 | 说明 |
|------|------|------|
| **方块 (block)** | 7 | 7种颜色的游戏方块主体 |
| **方块发光 (blockGlow)** | 7 | 方块的发光效果 |
| **灰色方块 (blockGrey)** | 7 | 不可用状态的方块 |
| **星标方块 (blockStarred)** | 7 | 带星星的特殊方块 |
| **按钮** | ~15 | 成就、购买、关闭、继续、重启、复活、设置等 |
| **图标** | ~20 | 炸弹、闪电、星星、奖杯、复活等 |
| **文字元素** | ~100 | 金色/灰色数字字母、倍数文字 |
| **成就系统** | ~50 | 成就徽章、通知、进度条 |
| **窗口元素** | ~20 | 窗口背景、标题板、分数板 |
| **其他 UI** | ~92 | 格子、控制条、特效等 |

#### animations.png - 动画精灵图集

**文件路径**: `vasugame/lib/Game/img/animations.png`
**文件大小**: 466 KB
**动画帧数**: 267 个
**配置文件**: `vasugame/lib/Game/img/animations.json`

包含各种游戏动画的逐帧图像。

#### 其他图像资源

| 文件 | 大小 | 说明 |
|------|------|------|
| `background.png` | 811 KB | 游戏主背景图 |
| `background.jpg` | 108 KB | 备用背景图 |
| `preloader.png` | 257 KB | 加载界面精灵图 |
| `preloader.json` | 6 KB | 加载界面配置 |
| `field-cover.png` | 25 KB | 游戏区域遮罩 |
| `18.png` | 571 KB | 额外图形资源 |
| `22.png` | 406 KB | 额外图形资源 |

---

### 2. 颜色和主题配置

#### CSS 样式文件

**文件路径**: `vasugame/lib/Game/app.css`

```css
/* 背景颜色 */
html {
    background: black;  /* 改为你的主题色 */
}

/* 背景图片 */
body {
    background: url("img/background.png") no-repeat center;
    background-size: cover;
}

/* 字体 */
@font-face {
    font-family: 'Kanit';  /* 主字体 */
}

@font-face {
    font-family: 'Russo One';  /* 副字体 */
}
```

#### JavaScript 颜色配置

**文件路径**: `vasugame/lib/Game/game.js`

**需要修改的颜色代码**:

| 颜色代码 | 用途 | 位置 |
|----------|------|------|
| `0xFFFFFF` | 白色 - 遮罩和文字 | 多处 |
| `0xFF0000` | 红色 - 错误提示 | game.js:6256-6257 |
| `#FFFFFF` | 白色 - HTML 颜色 | 多处 |
| `#FF5E40` | 橙红色 | 多处 |
| `#DAFFF4` | 浅青色 | 多处 |
| `#000000` | 黑色阴影 | 多处 |

**搜索方法**:
```bash
# 查找所有十六进制颜色代码
grep -n "0x[0-9A-Fa-f]\{6\}" vasugame/lib/Game/game.js
grep -n "#[0-9A-Fa-f]\{6\}" vasugame/lib/Game/game.js
```

---

### 3. 应用图标

#### Android 图标

**基础路径**: `vasugame/android/app/src/main/res/`

需要替换 5 个密度级别的图标：

| 目录 | 密度 | 尺寸 | 文件 |
|------|------|------|------|
| `mipmap-mdpi/` | 160dpi | 48x48 | 6个图标文件 |
| `mipmap-hdpi/` | 240dpi | 72x72 | 6个图标文件 |
| `mipmap-xhdpi/` | 320dpi | 96x96 | 6个图标文件 |
| `mipmap-xxhdpi/` | 480dpi | 144x144 | 6个图标文件 |
| `mipmap-xxxhdpi/` | 640dpi | 192x192 | 6个图标文件 |

**每个目录包含的文件**:
- `ic_launcher.png` - 标准应用图标
- `ic_launcher_adaptive_back.png` - 自适应图标背景
- `ic_launcher_adaptive_fore.png` - 自适应图标前景
- `ic_launcher_background.png` - 图标背景层
- `ic_launcher_foreground.png` - 图标前景层
- `ic_launcher_monochrome.png` - 单色图标（Android 13+）

**总计**: 30 个图标文件

#### iOS 图标

**路径**: `vasugame/ios/Runner/Assets.xcassets/AppIcon.appiconset/`

需要替换的图标尺寸：

| 文件名 | 尺寸 | 用途 |
|--------|------|------|
| `Icon-App-1024x1024@1x.png` | 1024x1024 | App Store |
| `Icon-App-20x20@1x.png` | 20x20 | 通知 |
| `Icon-App-20x20@2x.png` | 40x40 | 通知 @2x |
| `Icon-App-20x20@3x.png` | 60x60 | 通知 @3x |
| `Icon-App-29x29@1x.png` | 29x29 | 设置 |
| `Icon-App-29x29@2x.png` | 58x58 | 设置 @2x |
| `Icon-App-29x29@3x.png` | 87x87 | 设置 @3x |
| `Icon-App-40x40@1x.png` | 40x40 | Spotlight |
| `Icon-App-40x40@2x.png` | 80x80 | Spotlight @2x |
| `Icon-App-40x40@3x.png` | 120x120 | Spotlight @3x |
| `Icon-App-60x60@2x.png` | 120x120 | 应用图标 @2x |
| `Icon-App-60x60@3x.png` | 180x180 | 应用图标 @3x |
| `Icon-App-76x76@1x.png` | 76x76 | iPad |
| `Icon-App-76x76@2x.png` | 152x152 | iPad @2x |
| `Icon-App-83.5x83.5@2x.png` | 167x167 | iPad Pro |

**总计**: 15 个图标文件

---

### 4. 启动画面

#### Android 启动画面

**文件路径**: `vasugame/android/app/src/main/res/drawable/launch_background.xml`

这是一个 XML 配置文件，定义启动画面的布局和颜色。

#### iOS 启动画面

**路径**: `vasugame/ios/Runner/Assets.xcassets/LaunchImage.imageset/`

包含不同尺寸的启动图片。

---

### 5. 字体文件

**路径**: `vasugame/lib/Game/fonts/`

| 文件 | 字体名称 | 用途 |
|------|----------|------|
| `Kanit-Bold.woff2` | Kanit Bold | 主要游戏字体 |
| `RussoOne-Regular.woff2` | Russo One | 版权和特殊文字 |

**如何替换字体**:
1. 准备新字体的 `.woff2` 格式文件
2. 替换字体文件（保持文件名）
3. 或修改 `app.css` 中的 `@font-face` 声明

---

### 6. 游戏配置文件

#### 游戏设置

**文件路径**: `vasugame/lib/Game/settings.js`

```javascript
// 可配置的游戏参数
difficulty_level = 2;  // 难度等级 (1-10)
bomb_powerup_basic_price = 15;  // 炸弹道具价格
lightning_powerup_basic_price = 25;  // 闪电道具价格
```

#### 游戏标题和元数据

**文件路径**: `vasugame/lib/Game/index.html`

```html
<!-- 第 486 行 -->
<title>Element Blocks</title>  <!-- 改为你的游戏名 -->

<!-- 第 493 行 -->
<script>
    window.famobi_gameID = "element-blocks";  <!-- 游戏 ID -->
</script>
```

---

## 🛠️ Reskin 工作流程

### 阶段 1: 准备工作

#### 1.1 备份原始文件
```bash
# 创建备份目录
mkdir -p backup/original_assets

# 备份关键文件
cp vasugame/lib/Game/img/assets.png backup/original_assets/
cp vasugame/lib/Game/img/animations.png backup/original_assets/
cp vasugame/lib/Game/img/background.png backup/original_assets/
cp vasugame/lib/Game/app.css backup/original_assets/
cp vasugame/lib/Game/game.js backup/original_assets/
```

#### 1.2 安装必要工具

**推荐工具**:

1. **TexturePacker** (付费，最专业)
   - 官网: https://www.codeandweb.com/texturepacker
   - 功能: 解包/打包精灵图集
   - 价格: ~$40

2. **Free Texture Packer** (免费)
   - 在线版: https://free-tex-packer.com/
   - 桌面版: https://github.com/odrick/free-tex-packer
   - 功能: 基础的精灵图集打包

3. **Shoebox** (免费)
   - 官网: https://renderhjs.net/shoebox/
   - 功能: 精灵图集工具集

4. **图像编辑软件**
   - Adobe Photoshop (付费)
   - GIMP (免费)
   - Figma (免费/付费)

---

### 阶段 2: 解包精灵图集

#### 2.1 使用 TexturePacker 解包

```bash
# 命令行解包（需要 TexturePacker CLI）
TexturePacker --sheet assets.png --data assets.json --unpack
```

或使用 GUI:
1. 打开 TexturePacker
2. File → Import → Sprite Sheet
3. 选择 `assets.png` 和 `assets.json`
4. 导出所有单个精灵到文件夹

#### 2.2 手动定位精灵（不推荐，但可行）

使用 `assets.json` 中的坐标在 Photoshop 中手动裁剪：

```json
"block0000": {
    "frame": {"x":100, "y":200, "w":50, "h":50}
}
```

在 Photoshop 中:
1. 打开 `assets.png`
2. 使用矩形选框工具
3. 输入坐标: X=100, Y=200, W=50, H=50
4. 裁剪并保存

---

### 阶段 3: 设计新视觉元素

#### 3.1 方块设计（最重要）

**需要设计的方块类型**:

| 方块类型 | 数量 | 精灵名称 | 说明 |
|----------|------|----------|------|
| 普通方块 | 7 | block0000-block0006 | 7种颜色 |
| 发光方块 | 7 | blockGlow0000-blockGlow0006 | 发光效果 |
| 灰色方块 | 7 | blockGrey0000-blockGrey0006 | 禁用状态 |
| 星标方块 | 7 | blockStarred0000-blockStarred0006 | 特殊方块 |

**设计建议**:
- 保持方块尺寸一致
- 使用清晰的颜色区分
- 确保在小屏幕上可见
- 考虑色盲友好的配色

**推荐配色方案**:
- 方案 1（经典）: 红、橙、黄、绿、青、蓝、紫
- 方案 2（糖果）: 粉、橙、黄、薄荷绿、天蓝、紫、玫红
- 方案 3（宝石）: 红宝石、琥珀、黄玉、翡翠、蓝宝石、紫水晶、钻石

#### 3.2 UI 按钮设计

**主要按钮列表**:

| 按钮精灵名称 | 用途 | 建议尺寸 |
|--------------|------|----------|
| `buttonAchievements` | 成就按钮 | ~80x80 |
| `buttonSettings` | 设置按钮 | ~80x80 |
| `buttonBuy` | 购买按钮 | ~120x60 |
| `buttonClose` | 关闭按钮 | ~60x60 |
| `buttonContinue` | 继续按钮 | ~150x70 |
| `buttonRestart` | 重新开始 | ~150x70 |
| `buttonRevive` | 复活按钮 | ~150x70 |
| `buttonTutorial` | 教程按钮 | ~80x80 |

**设计要点**:
- 按钮需要有清晰的视觉反馈
- 考虑按下状态（可能需要多个状态）
- 保持统一的设计风格
- 确保文字可读性

#### 3.3 背景设计

**文件**: `background.png` (811 KB)
**推荐尺寸**: 1920x1080 或更高
**格式**: PNG（支持透明）或 JPG

**设计建议**:
- 使用柔和的颜色，不要太抢眼
- 确保游戏区域的对比度
- 考虑不同屏幕比例的适配
- 可以使用渐变或纹理

---

### 阶段 4: 重新打包精灵图集

#### 4.1 使用 TexturePacker 打包

1. 将所有修改后的精灵放入一个文件夹
2. 打开 TexturePacker
3. 添加精灵文件夹
4. 设置输出格式为 "Phaser (JSONHash)"
5. 设置输出文件名为 "assets"
6. 点击 "Publish" 生成新的 `assets.png` 和 `assets.json`

**重要设置**:
- Data Format: Phaser (JSONHash)
- Texture Format: PNG-8 或 PNG-32
- Algorithm: MaxRects
- Trim Mode: Trim (保持原有的 trim 设置)
- Size Constraints: POT (Power of 2)

#### 4.2 验证打包结果

```bash
# 检查文件大小
ls -lh vasugame/lib/Game/img/assets.png
ls -lh vasugame/lib/Game/img/assets.json

# 验证 JSON 格式
cat vasugame/lib/Game/img/assets.json | python -m json.tool > /dev/null
echo "JSON 格式正确"
```

---

### 阶段 5: 修改代码配置

#### 5.1 修改颜色

**修改 CSS 背景色**:

```bash
# 编辑 app.css
nano vasugame/lib/Game/app.css

# 修改第 5 行
background: #你的颜色;
```

**批量替换 JavaScript 颜色**:

```bash
# 备份原文件
cp vasugame/lib/Game/game.js vasugame/lib/Game/game.js.backup

# 替换白色为新颜色（示例）
sed -i '' 's/0xFFFFFF/0x新颜色/g' vasugame/lib/Game/game.js
```

#### 5.2 修改游戏标题

```bash
# 编辑 index.html
nano vasugame/lib/Game/index.html

# 修改第 486 行
<title>你的游戏名</title>

# 修改第 493 行
window.famobi_gameID = "your-game-id";
```

#### 5.3 修改应用包名（可选）

**Android**:

```bash
# 编辑 build.gradle
nano vasugame/android/app/build.gradle

# 修改 applicationId
applicationId "com.yourcompany.yourgame"
```

**iOS**:

```bash
# 编辑 Info.plist
nano vasugame/ios/Runner/Info.plist

# 修改 CFBundleIdentifier
<key>CFBundleIdentifier</key>
<string>com.yourcompany.yourgame</string>
```

---

### 阶段 6: 替换应用图标

#### 6.1 生成多尺寸图标

**推荐工具**:
- **App Icon Generator**: https://appicon.co/
- **Android Asset Studio**: https://romannurik.github.io/AndroidAssetStudio/
- **Icon Kitchen**: https://icon.kitchen/

**步骤**:
1. 准备一个 1024x1024 的主图标
2. 上传到图标生成器
3. 下载生成的所有尺寸
4. 替换到对应目录

#### 6.2 替换 Android 图标

```bash
# 批量替换（假设新图标在 new_icons/android/ 目录）
cp new_icons/android/mipmap-mdpi/* vasugame/android/app/src/main/res/mipmap-mdpi/
cp new_icons/android/mipmap-hdpi/* vasugame/android/app/src/main/res/mipmap-hdpi/
cp new_icons/android/mipmap-xhdpi/* vasugame/android/app/src/main/res/mipmap-xhdpi/
cp new_icons/android/mipmap-xxhdpi/* vasugame/android/app/src/main/res/mipmap-xxhdpi/
cp new_icons/android/mipmap-xxxhdpi/* vasugame/android/app/src/main/res/mipmap-xxxhdpi/
```

#### 6.3 替换 iOS 图标

```bash
# 批量替换（假设新图标在 new_icons/ios/ 目录）
cp new_icons/ios/* vasugame/ios/Runner/Assets.xcassets/AppIcon.appiconset/
```

---

### 阶段 7: 测试和调试

#### 7.1 本地测试

```bash
# 进入 Flutter 项目目录
cd vasugame

# 清理缓存
flutter clean

# 获取依赖
flutter pub get

# 运行应用（Android）
flutter run

# 运行应用（iOS）
flutter run -d ios
```

#### 7.2 检查清单

- [ ] 游戏能正常启动
- [ ] 所有方块显示正确
- [ ] 按钮可以点击且显示正确
- [ ] 背景图显示正常
- [ ] 应用图标显示正确
- [ ] 游戏标题已更改
- [ ] 颜色主题一致
- [ ] 没有缺失的精灵（控制台无错误）
- [ ] 动画播放正常
- [ ] 音效正常（如果修改了音频）

#### 7.3 常见问题排查

**问题 1: 精灵显示为空白或错误**
- 检查 `assets.json` 中的坐标是否正确
- 确认精灵名称没有改变
- 验证 PNG 文件没有损坏

**问题 2: 游戏加载缓慢**
- 优化图片大小（使用 TinyPNG 等工具压缩）
- 检查精灵图集是否过大
- 考虑使用 WebP 格式（需要修改代码）

**问题 3: 颜色没有改变**
- 清除 Flutter 缓存: `flutter clean`
- 检查是否修改了所有颜色代码
- 确认 CSS 文件已保存

**问题 4: 应用图标没有更新**
- 卸载旧应用后重新安装
- 清理构建缓存
- 检查图标文件名是否正确

---

## 📊 精灵坐标参考

### 核心游戏方块坐标

以下是从 `assets.json` 提取的关键精灵坐标（需要时可以手动定位）：

```json
// 示例：方块精灵坐标
// 实际坐标请查看 vasugame/lib/Game/img/assets.json
{
  "block0000": {"frame": {"x": ?, "y": ?, "w": ?, "h": ?}},
  "block0001": {"frame": {"x": ?, "y": ?, "w": ?, "h": ?}},
  // ... 更多精灵
}
```

**提取所有方块坐标的命令**:

```bash
# 提取所有 block 相关精灵的坐标
grep -A 1 '"block[0-9]' vasugame/lib/Game/img/assets.json | grep frame
```

---

## 🎨 设计资源推荐

### 免费图标和素材

- **Flaticon**: https://www.flaticon.com/ - 免费图标
- **Freepik**: https://www.freepik.com/ - 免费矢量图
- **Kenney**: https://kenney.nl/ - 免费游戏素材
- **OpenGameArt**: https://opengameart.org/ - 开源游戏美术

### 配色工具

- **Coolors**: https://coolors.co/ - 配色方案生成器
- **Adobe Color**: https://color.adobe.com/ - 配色轮
- **Paletton**: https://paletton.com/ - 配色设计工具

### 字体资源

- **Google Fonts**: https://fonts.google.com/ - 免费网页字体
- **DaFont**: https://www.dafont.com/ - 免费字体下载
- **Font Squirrel**: https://www.fontsquirrel.com/ - 商用免费字体

---

## 📝 Reskin 检查清单

### 必须修改的文件

- [ ] `vasugame/lib/Game/img/assets.png` - 主精灵图集
- [ ] `vasugame/lib/Game/img/assets.json` - 精灵坐标
- [ ] `vasugame/lib/Game/img/background.png` - 背景图
- [ ] `vasugame/lib/Game/index.html` - 游戏标题
- [ ] Android 图标（30个文件）
- [ ] iOS 图标（15个文件）

### 推荐修改的文件

- [ ] `vasugame/lib/Game/img/animations.png` - 动画精灵
- [ ] `vasugame/lib/Game/img/animations.json` - 动画配置
- [ ] `vasugame/lib/Game/img/preloader.png` - 加载界面
- [ ] `vasugame/lib/Game/app.css` - 样式和颜色
- [ ] `vasugame/lib/Game/game.js` - 游戏内颜色
- [ ] `vasugame/lib/Game/fonts/` - 字体文件
- [ ] 启动画面（Android + iOS）

### 可选修改的文件

- [ ] `vasugame/lib/Game/settings.js` - 游戏参数
- [ ] `vasugame/lib/Game/sound/mp3/` - 音效文件（34个）
- [ ] Android 包名和应用名
- [ ] iOS Bundle ID 和应用名
- [ ] 营销素材（logo.png, Preview Image.jpg）

---

## 🚀 发布前准备

### 1. 版本号更新

**Flutter pubspec.yaml**:
```yaml
version: 1.0.0+1  # 改为你的版本号
```

**Android build.gradle**:
```gradle
versionCode 1  # 版本代码（整数）
versionName "1.0.0"  # 版本名称
```

**iOS Info.plist**:
```xml
<key>CFBundleShortVersionString</key>
<string>1.0.0</string>
<key>CFBundleVersion</key>
<string>1</string>
```

### 2. 构建发布版本

**Android APK**:
```bash
cd vasugame
flutter build apk --release
```

**Android App Bundle** (推荐用于 Google Play):
```bash
flutter build appbundle --release
```

**iOS**:
```bash
flutter build ios --release
```

### 3. 测试发布版本

- 在真实设备上测试
- 检查性能和内存使用
- 验证所有功能正常
- 测试不同屏幕尺寸

---

## 💡 高级技巧

### 批量处理精灵

**Python 脚本示例** - 从精灵图集提取单个精灵:

```python
import json
from PIL import Image

# 读取精灵图集和配置
atlas = Image.open('vasugame/lib/Game/img/assets.png')
with open('vasugame/lib/Game/img/assets.json', 'r') as f:
    data = json.load(f)

# 提取所有精灵
for name, info in data['frames'].items():
    frame = info['frame']
    sprite = atlas.crop((
        frame['x'],
        frame['y'],
        frame['x'] + frame['w'],
        frame['y'] + frame['h']
    ))
    sprite.save(f'extracted_sprites/{name}.png')
    print(f'Extracted: {name}')
```

### 自动化颜色替换

**Node.js 脚本示例** - 批量替换颜色代码:

```javascript
const fs = require('fs');

// 读取 game.js
let gameJs = fs.readFileSync('vasugame/lib/Game/game.js', 'utf8');

// 定义颜色映射
const colorMap = {
    '0xFFFFFF': '0xYOURCOLOR1',
    '0xFF0000': '0xYOURCOLOR2',
    '#FFFFFF': '#YOURCOLOR3'
};

// 批量替换
for (const [oldColor, newColor] of Object.entries(colorMap)) {
    gameJs = gameJs.replace(new RegExp(oldColor, 'g'), newColor);
}

// 保存
fs.writeFileSync('vasugame/lib/Game/game.js', gameJs);
console.log('Colors replaced successfully!');
```

---

## 📞 获取帮助

### 常见资源

- **Flutter 文档**: https://flutter.dev/docs
- **Phaser 文档**: https://phaser.io/docs
- **TexturePacker 文档**: https://www.codeandweb.com/texturepacker/documentation

### 社区支持

- **Flutter 中文社区**: https://flutter.cn/
- **Phaser 论坛**: https://phaser.discourse.group/
- **Stack Overflow**: 搜索 "flutter" 或 "phaser" 标签

---

## 📄 许可和版权

在发布 reskin 版本前，请确保：

1. 你拥有原始代码的合法许可
2. 所有新的美术资源都有使用权
3. 字体具有商用许可
4. 音效和音乐有适当的授权
5. 遵守 App Store 和 Google Play 的政策

---

## ✅ 总结

Reskin 这个 Block Puzzle 游戏的关键步骤：

1. **备份原始文件** - 始终保留备份
2. **解包精灵图集** - 使用 TexturePacker 或类似工具
3. **设计新视觉元素** - 重点是方块和 UI
4. **重新打包精灵** - 保持相同的命名和格式
5. **修改配置文件** - 颜色、标题、包名等
6. **替换应用图标** - Android 和 iOS
7. **测试和调试** - 确保一切正常
8. **构建发布版本** - 准备上架

**预计工作时间**:
- 最小化 reskin: 1-2 天
- 中度 reskin: 3-5 天
- 完全 reskin: 1-2 周

**最大的工作量在于**:
- 设计和制作 325 个 UI 精灵
- 设计和制作 267 个动画帧
- 确保所有元素风格统一

祝你 reskin 顺利！🎉
