#!/usr/bin/env python3
"""
图像颜色批量替换工具
可以批量修改精灵的颜色
"""

import os
from PIL import Image
import numpy as np

def replace_color(image_path, old_color, new_color, tolerance=30, output_path=None):
    """
    替换图像中的颜色

    Args:
        image_path: 输入图像路径
        old_color: 要替换的颜色 (R, G, B)
        new_color: 新颜色 (R, G, B)
        tolerance: 颜色容差（0-255）
        output_path: 输出路径，如果为 None 则覆盖原文件
    """
    # 打开图像
    img = Image.open(image_path).convert('RGBA')
    data = np.array(img)

    # 提取 RGB 通道
    red, green, blue, alpha = data[:,:,0], data[:,:,1], data[:,:,2], data[:,:,3]

    # 创建颜色匹配掩码
    mask = (
        (np.abs(red - old_color[0]) <= tolerance) &
        (np.abs(green - old_color[1]) <= tolerance) &
        (np.abs(blue - old_color[2]) <= tolerance)
    )

    # 替换颜色
    data[:,:,0][mask] = new_color[0]
    data[:,:,1][mask] = new_color[1]
    data[:,:,2][mask] = new_color[2]

    # 保存
    result = Image.fromarray(data)
    if output_path is None:
        output_path = image_path
    result.save(output_path)

    return np.sum(mask)  # 返回替换的像素数

def batch_replace_color(input_dir, old_color, new_color, tolerance=30, output_dir=None):
    """
    批量替换目录中所有图像的颜色

    Args:
        input_dir: 输入目录
        old_color: 要替换的颜色 (R, G, B)
        new_color: 新颜色 (R, G, B)
        tolerance: 颜色容差
        output_dir: 输出目录，如果为 None 则覆盖原文件
    """
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    processed = 0
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename) if output_dir else None

            try:
                pixels_changed = replace_color(input_path, old_color, new_color, tolerance, output_path)
                processed += 1
                print(f"✓ {filename}: 替换了 {pixels_changed} 个像素")
            except Exception as e:
                print(f"✗ {filename}: 失败 - {e}")

    print(f"\n完成！处理了 {processed} 个文件")

def adjust_brightness(image_path, factor, output_path=None):
    """
    调整图像亮度

    Args:
        image_path: 输入图像路径
        factor: 亮度因子（1.0 = 原始，>1.0 = 更亮，<1.0 = 更暗）
        output_path: 输出路径
    """
    from PIL import ImageEnhance

    img = Image.open(image_path)
    enhancer = ImageEnhance.Brightness(img)
    result = enhancer.enhance(factor)

    if output_path is None:
        output_path = image_path
    result.save(output_path)

def adjust_saturation(image_path, factor, output_path=None):
    """
    调整图像饱和度

    Args:
        image_path: 输入图像路径
        factor: 饱和度因子（1.0 = 原始，>1.0 = 更饱和，<1.0 = 更灰）
        output_path: 输出路径
    """
    from PIL import ImageEnhance

    img = Image.open(image_path)
    enhancer = ImageEnhance.Color(img)
    result = enhancer.enhance(factor)

    if output_path is None:
        output_path = image_path
    result.save(output_path)

if __name__ == "__main__":
    print("=" * 60)
    print("图像颜色批量替换工具")
    print("=" * 60)

    # 示例：替换方块颜色
    # 假设你已经提取了精灵到 extracted_sprites/assets/

    # 示例 1: 将红色方块改为蓝色
    # old_color = (255, 0, 0)    # 红色
    # new_color = (0, 0, 255)    # 蓝色
    # batch_replace_color(
    #     input_dir="extracted_sprites/assets",
    #     old_color=old_color,
    #     new_color=new_color,
    #     tolerance=30,
    #     output_dir="recolored_sprites"
    # )

    # 示例 2: 调整所有精灵的亮度
    # for filename in os.listdir("extracted_sprites/assets"):
    #     if filename.endswith('.png'):
    #         path = os.path.join("extracted_sprites/assets", filename)
    #         adjust_brightness(path, 1.2)  # 增加 20% 亮度

    print("\n使用方法：")
    print("1. 取消注释上面的示例代码")
    print("2. 修改颜色值和路径")
    print("3. 运行脚本")
    print("\n或者在你的代码中导入这些函数使用")
