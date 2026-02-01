#!/usr/bin/env python3
"""
一键批量替换方块颜色
配置你想要的新颜色方案，然后运行此脚本
"""

import os
import sys
from PIL import Image, ImageEnhance
import numpy as np

def replace_color_in_image(img, old_color, new_color, tolerance=40):
    """替换图像中的颜色"""
    data = np.array(img)
    red, green, blue, alpha = data[:,:,0], data[:,:,1], data[:,:,2], data[:,:,3]

    # 创建颜色匹配掩码
    mask = (
        (np.abs(red - old_color[0]) <= tolerance) &
        (np.abs(green - old_color[1]) <= tolerance) &
        (np.abs(blue - old_color[2]) <= tolerance) &
        (alpha > 128)  # 只处理非透明像素
    )

    # 替换颜色
    data[:,:,0][mask] = new_color[0]
    data[:,:,1][mask] = new_color[1]
    data[:,:,2][mask] = new_color[2]

    return Image.fromarray(data)

def batch_reskin_blocks(color_scheme_name="candy"):
    """
    批量替换方块颜色

    预设颜色方案：
    - classic: 经典彩虹色
    - candy: 糖果色
    - neon: 霓虹色
    - pastel: 马卡龙色
    - jewel: 宝石色
    """

    # 当前方块颜色（从游戏中提取）
    current_colors = [
        (176, 78, 67),    # 方块 0: 红褐色
        (27, 123, 19),    # 方块 1: 绿色
        (167, 191, 14),   # 方块 2: 黄绿色
        (53, 105, 185),   # 方块 3: 蓝色
        (224, 143, 59),   # 方块 4: 橙色
        (128, 174, 168),  # 方块 5: 青色
        (168, 65, 187),   # 方块 6: 紫色
    ]

    # 颜色方案库
    color_schemes = {
        "classic": [
            (255, 50, 50),    # 鲜红
            (255, 165, 0),    # 橙色
            (255, 255, 0),    # 黄色
            (0, 255, 0),      # 绿色
            (0, 191, 255),    # 天蓝
            (0, 0, 255),      # 蓝色
            (148, 0, 211),    # 紫色
        ],
        "candy": [
            (255, 105, 180),  # 粉红
            (255, 140, 0),    # 橙色
            (255, 215, 0),    # 金黄
            (50, 205, 50),    # 薄荷绿
            (135, 206, 250),  # 天蓝
            (186, 85, 211),   # 紫色
            (255, 20, 147),   # 玫红
        ],
        "neon": [
            (255, 0, 102),    # 霓虹粉
            (255, 153, 0),    # 霓虹橙
            (204, 255, 0),    # 霓虹黄
            (0, 255, 102),    # 霓虹绿
            (0, 204, 255),    # 霓虹蓝
            (102, 0, 255),    # 霓虹紫
            (255, 0, 204),    # 霓虹品红
        ],
        "pastel": [
            (255, 179, 186),  # 粉色
            (255, 223, 186),  # 桃色
            (255, 255, 186),  # 淡黄
            (186, 255, 201),  # 淡绿
            (186, 225, 255),  # 淡蓝
            (220, 198, 224),  # 淡紫
            (255, 198, 224),  # 淡粉紫
        ],
        "jewel": [
            (220, 20, 60),    # 红宝石
            (255, 140, 0),    # 琥珀
            (255, 215, 0),    # 黄玉
            (0, 128, 0),      # 翡翠
            (0, 71, 171),     # 蓝宝石
            (102, 2, 60),     # 紫水晶
            (185, 242, 255),  # 钻石
        ],
    }

    if color_scheme_name not in color_schemes:
        print(f"错误：未知的颜色方案 '{color_scheme_name}'")
        print(f"可用方案: {', '.join(color_schemes.keys())}")
        return False

    new_colors = color_schemes[color_scheme_name]

    print("=" * 70)
    print(f"🎨 应用颜色方案: {color_scheme_name.upper()}")
    print("=" * 70)

    # 创建输出目录
    output_dir = f"reskin_output/{color_scheme_name}"
    os.makedirs(output_dir, exist_ok=True)

    # 处理每个方块
    for i in range(7):
        sprite_name = f"block000{i}"
        input_path = f"extracted_sprites/assets/{sprite_name}.png"
        output_path = f"{output_dir}/{sprite_name}.png"

        if not os.path.exists(input_path):
            print(f"⚠️  跳过 {sprite_name} (文件不存在)")
            continue

        # 读取图像
        img = Image.open(input_path).convert('RGBA')

        # 替换颜色
        old_color = current_colors[i]
        new_color = new_colors[i]

        result = replace_color_in_image(img, old_color, new_color, tolerance=50)

        # 保存
        result.save(output_path)

        print(f"✓ {sprite_name}: {old_color} → {new_color}")

    # 同时处理发光效果
    print("\n处理发光效果...")
    for i in range(7):
        sprite_name = f"blockGlow000{i}"
        input_path = f"extracted_sprites/assets/{sprite_name}.png"
        output_path = f"{output_dir}/{sprite_name}.png"

        if os.path.exists(input_path):
            img = Image.open(input_path).convert('RGBA')
            result = replace_color_in_image(img, current_colors[i], new_colors[i], tolerance=50)
            result.save(output_path)
            print(f"✓ {sprite_name}")

    print("\n" + "=" * 70)
    print(f"✅ 完成！新方块已保存到: {output_dir}/")
    print("=" * 70)
    print("\n下一步：")
    print("1. 查看效果: open " + output_dir)
    print("2. 如果满意，复制所有修改后的精灵：")
    print(f"   cp {output_dir}/*.png extracted_sprites/assets/")
    print("3. 重新打包: python3 pack_sprites.py")

    return True

if __name__ == "__main__":
    print("\n可用的颜色方案：")
    print("  classic - 经典彩虹色")
    print("  candy   - 糖果色（推荐）")
    print("  neon    - 霓虹色")
    print("  pastel  - 马卡龙色")
    print("  jewel   - 宝石色")
    print()

    # 默认使用糖果色方案
    scheme = sys.argv[1] if len(sys.argv) > 1 else "candy"

    batch_reskin_blocks(scheme)
