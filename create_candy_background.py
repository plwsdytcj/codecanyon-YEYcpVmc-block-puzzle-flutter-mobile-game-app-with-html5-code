#!/usr/bin/env python3
"""
创建糖果风格的背景图
"""

from PIL import Image, ImageDraw, ImageFilter
import random
import math

def create_candy_gradient(width, height):
    """创建糖果色渐变背景"""
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)

    # 糖果色渐变：从粉色到淡蓝色
    for y in range(height):
        # 计算渐变比例
        ratio = y / height

        # 粉色 (255, 182, 193) 到 淡蓝色 (173, 216, 230)
        r = int(255 * (1 - ratio) + 173 * ratio)
        g = int(182 * (1 - ratio) + 216 * ratio)
        b = int(193 * (1 - ratio) + 230 * ratio)

        draw.line([(0, y), (width, y)], fill=(r, g, b))

    return img

def add_candy_circles(img, num_circles=30):
    """添加糖果圆圈装饰"""
    draw = ImageDraw.Draw(img, 'RGBA')
    width, height = img.size

    # 糖果色调色板
    candy_colors = [
        (255, 182, 193, 80),  # 粉色
        (255, 218, 185, 80),  # 桃色
        (255, 255, 224, 80),  # 淡黄
        (224, 255, 255, 80),  # 淡青
        (230, 230, 250, 80),  # 淡紫
        (255, 240, 245, 80),  # 淡粉
    ]

    for _ in range(num_circles):
        # 随机位置和大小
        x = random.randint(0, width)
        y = random.randint(0, height)
        radius = random.randint(30, 150)

        # 随机颜色
        color = random.choice(candy_colors)

        # 绘制圆圈
        draw.ellipse(
            [x - radius, y - radius, x + radius, y + radius],
            fill=color,
            outline=None
        )

    return img

def add_candy_stripes(img, num_stripes=15):
    """添加糖果条纹"""
    draw = ImageDraw.Draw(img, 'RGBA')
    width, height = img.size

    stripe_colors = [
        (255, 192, 203, 60),  # 粉色
        (255, 228, 196, 60),  # 桃色
        (255, 255, 240, 60),  # 象牙色
    ]

    for _ in range(num_stripes):
        # 随机角度的条纹
        x1 = random.randint(-width, width * 2)
        y1 = 0
        x2 = x1 + random.randint(-200, 200)
        y2 = height

        color = random.choice(stripe_colors)
        stripe_width = random.randint(20, 60)

        draw.line([(x1, y1), (x2, y2)], fill=color, width=stripe_width)

    return img

def create_candy_background(output_path, width=1920, height=1080):
    """创建完整的糖果背景"""
    print("=" * 70)
    print("🍬 创建糖果风格背景")
    print("=" * 70)

    # 1. 创建渐变背景
    print("\n[1/4] 创建渐变背景...")
    img = create_candy_gradient(width, height)

    # 2. 添加条纹
    print("[2/4] 添加糖果条纹...")
    img = add_candy_stripes(img, num_stripes=12)

    # 3. 添加圆圈
    print("[3/4] 添加糖果圆圈...")
    img = add_candy_circles(img, num_circles=25)

    # 4. 应用模糊效果使其更柔和
    print("[4/4] 应用柔和效果...")
    img = img.filter(ImageFilter.GaussianBlur(radius=15))

    # 保存
    img.save(output_path, quality=95)
    print(f"\n✅ 糖果背景已保存到: {output_path}")
    print(f"   尺寸: {width}x{height}")
    print(f"   文件大小: {os.path.getsize(output_path) / 1024:.1f} KB")

    return img

if __name__ == "__main__":
    import os

    # 创建糖果背景
    create_candy_background(
        output_path="vasugame/lib/Game/img/background_candy.png",
        width=1920,
        height=1080
    )

    print("\n下一步：")
    print("1. 查看效果: open vasugame/lib/Game/img/background_candy.png")
    print("2. 如果满意，备份并替换：")
    print("   cp vasugame/lib/Game/img/background.png vasugame/lib/Game/img/background_backup.png")
    print("   cp vasugame/lib/Game/img/background_candy.png vasugame/lib/Game/img/background.png")
