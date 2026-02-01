#!/usr/bin/env python3
"""
批量调整 UI 元素为糖果风格
增加饱和度和亮度，使其更加糖果化
"""

from PIL import Image, ImageEnhance
import os

def candify_image(input_path, output_path=None, saturation=1.3, brightness=1.1):
    """
    将图像调整为糖果风格

    Args:
        input_path: 输入图像路径
        output_path: 输出路径（如果为 None 则覆盖原文件）
        saturation: 饱和度因子（>1 更鲜艳）
        brightness: 亮度因子（>1 更亮）
    """
    try:
        # 打开图像
        img = Image.open(input_path)

        # 转换为 RGBA 模式（如果不是的话）
        if img.mode != 'RGBA':
            img = img.convert('RGBA')

        # 增加饱和度
        enhancer = ImageEnhance.Color(img)
        img = enhancer.enhance(saturation)

        # 增加亮度
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(brightness)

        # 保存
        if output_path is None:
            output_path = input_path
        img.save(output_path)

        return True
    except Exception as e:
        print(f"处理失败 {os.path.basename(input_path)}: {e}")
        return False

def batch_candify_ui(sprites_dir, exclude_blocks=True):
    """
    批量处理 UI 元素

    Args:
        sprites_dir: 精灵目录
        exclude_blocks: 是否排除方块（方块已经处理过了）
    """
    print("=" * 70)
    print("🍭 批量调整 UI 元素为糖果风格")
    print("=" * 70)

    processed = 0
    skipped = 0

    # 需要排除的文件（已经处理过的方块）
    exclude_patterns = []
    if exclude_blocks:
        exclude_patterns = ['block0', 'blockGlow', 'blockGrey', 'blockStarred']

    for filename in sorted(os.listdir(sprites_dir)):
        if not filename.lower().endswith('.png'):
            continue

        # 检查是否需要排除
        should_skip = False
        for pattern in exclude_patterns:
            if filename.startswith(pattern):
                should_skip = True
                break

        if should_skip:
            skipped += 1
            continue

        file_path = os.path.join(sprites_dir, filename)

        # 处理图像
        if candify_image(file_path, saturation=1.3, brightness=1.1):
            processed += 1
            if processed % 50 == 0:
                print(f"已处理 {processed} 个文件...")

    print(f"\n✅ 完成！")
    print(f"   处理: {processed} 个文件")
    print(f"   跳过: {skipped} 个文件（方块）")

if __name__ == "__main__":
    # 批量处理 UI 元素
    batch_candify_ui("extracted_sprites/assets", exclude_blocks=True)

    print("\n下一步：")
    print("1. 重新打包精灵图集: python3 repack_assets.py")
    print("2. 替换游戏文件")
