#!/usr/bin/env python3
"""
创建糖果风格的应用图标
"""

from PIL import Image, ImageDraw, ImageFilter
import os

def create_candy_icon(size=1024):
    """创建糖果风格的应用图标"""
    # 创建画布
    img = Image.new('RGB', (size, size), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # 背景渐变（粉色到紫色）
    for y in range(size):
        ratio = y / size
        r = int(255 * (1 - ratio) + 200 * ratio)
        g = int(182 * (1 - ratio) + 150 * ratio)
        b = int(193 * (1 - ratio) + 255 * ratio)
        draw.line([(0, y), (size, y)], fill=(r, g, b))

    # 添加大圆圈（代表方块）
    center = size // 2
    radius = size // 3

    # 绘制多个彩色圆圈
    colors = [
        (255, 105, 180),  # 粉红
        (255, 215, 0),    # 金黄
        (135, 206, 250),  # 天蓝
    ]

    positions = [
        (center - radius//2, center - radius//2),
        (center + radius//2, center - radius//2),
        (center, center + radius//2),
    ]

    for pos, color in zip(positions, colors):
        r = radius // 2
        draw.ellipse(
            [pos[0] - r, pos[1] - r, pos[0] + r, pos[1] + r],
            fill=color,
            outline=(255, 255, 255),
            width=size//50
        )

    # 应用模糊使其更柔和
    img = img.filter(ImageFilter.GaussianBlur(radius=size//100))

    # 添加圆角
    img = add_rounded_corners(img, radius=size//8)

    return img

def add_rounded_corners(img, radius):
    """添加圆角"""
    # 创建圆角蒙版
    mask = Image.new('L', img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle([(0, 0), img.size], radius=radius, fill=255)

    # 应用蒙版
    output = Image.new('RGBA', img.size, (0, 0, 0, 0))
    output.paste(img, (0, 0))
    output.putalpha(mask)

    return output

def resize_icon(img, size):
    """调整图标大小"""
    return img.resize((size, size), Image.Resampling.LANCZOS)

def generate_android_icons(base_icon, output_dir):
    """生成所有 Android 图标"""
    print("\n生成 Android 图标...")

    # Android 图标尺寸
    densities = {
        'mipmap-mdpi': 48,
        'mipmap-hdpi': 72,
        'mipmap-xhdpi': 96,
        'mipmap-xxhdpi': 144,
        'mipmap-xxxhdpi': 192,
    }

    icon_names = [
        'ic_launcher.png',
        'ic_launcher_foreground.png',
    ]

    for density, size in densities.items():
        density_dir = os.path.join(output_dir, 'android', density)
        os.makedirs(density_dir, exist_ok=True)

        for icon_name in icon_names:
            icon = resize_icon(base_icon, size)
            icon_path = os.path.join(density_dir, icon_name)
            icon.save(icon_path)
            print(f"  ✓ {density}/{icon_name}")

def generate_ios_icons(base_icon, output_dir):
    """生成所有 iOS 图标"""
    print("\n生成 iOS 图标...")

    # iOS 图标尺寸
    sizes = [
        ('Icon-App-1024x1024@1x.png', 1024),
        ('Icon-App-20x20@1x.png', 20),
        ('Icon-App-20x20@2x.png', 40),
        ('Icon-App-20x20@3x.png', 60),
        ('Icon-App-29x29@1x.png', 29),
        ('Icon-App-29x29@2x.png', 58),
        ('Icon-App-29x29@3x.png', 87),
        ('Icon-App-40x40@1x.png', 40),
        ('Icon-App-40x40@2x.png', 80),
        ('Icon-App-40x40@3x.png', 120),
        ('Icon-App-60x60@2x.png', 120),
        ('Icon-App-60x60@3x.png', 180),
        ('Icon-App-76x76@1x.png', 76),
        ('Icon-App-76x76@2x.png', 152),
        ('Icon-App-83.5x83.5@2x.png', 167),
    ]

    ios_dir = os.path.join(output_dir, 'ios')
    os.makedirs(ios_dir, exist_ok=True)

    for filename, size in sizes:
        icon = resize_icon(base_icon, size)
        icon_path = os.path.join(ios_dir, filename)
        icon.save(icon_path)
        print(f"  ✓ {filename}")

if __name__ == "__main__":
    print("=" * 70)
    print("🍬 创建糖果风格应用图标")
    print("=" * 70)

    # 创建主图标
    print("\n[1/3] 创建主图标 (1024x1024)...")
    base_icon = create_candy_icon(1024)
    base_icon.save("app_icon_candy.png")
    print("  ✓ 主图标已保存: app_icon_candy.png")

    # 生成 Android 图标
    print("\n[2/3] 生成 Android 图标...")
    generate_android_icons(base_icon, "app_icons")

    # 生成 iOS 图标
    print("\n[3/3] 生成 iOS 图标...")
    generate_ios_icons(base_icon, "app_icons")

    print("\n" + "=" * 70)
    print("✅ 所有图标已生成！")
    print("=" * 70)
    print("\n生成的文件：")
    print("  - app_icon_candy.png (主图标)")
    print("  - app_icons/android/ (Android 图标)")
    print("  - app_icons/ios/ (iOS 图标)")
    print("\n下一步：")
    print("1. 查看主图标: open app_icon_candy.png")
    print("2. 如果满意，复制到项目：")
    print("   # Android")
    print("   cp -r app_icons/android/* vasugame/android/app/src/main/res/")
    print("   # iOS")
    print("   cp app_icons/ios/* vasugame/ios/Runner/Assets.xcassets/AppIcon.appiconset/")
