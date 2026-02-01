#!/usr/bin/env python3
"""
批量处理动画精灵为糖果风格
"""

from PIL import Image, ImageEnhance
import os

def candify_animation(input_path, output_path=None, saturation=1.2, brightness=1.05):
    """将动画帧调整为糖果风格"""
    try:
        img = Image.open(input_path)

        # 转换为 RGBA
        if img.mode != 'RGBA':
            img = img.convert('RGBA')

        # 增加饱和度（比 UI 元素稍微温和一些）
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

def batch_candify_animations(animations_dir):
    """批量处理动画帧"""
    print("=" * 70)
    print("🎬 批量调整动画帧为糖果风格")
    print("=" * 70)

    processed = 0

    for filename in sorted(os.listdir(animations_dir)):
        if not filename.lower().endswith('.png'):
            continue

        file_path = os.path.join(animations_dir, filename)

        if candify_animation(file_path, saturation=1.2, brightness=1.05):
            processed += 1
            if processed % 50 == 0:
                print(f"已处理 {processed} 个动画帧...")

    print(f"\n✅ 完成！处理了 {processed} 个动画帧")

if __name__ == "__main__":
    batch_candify_animations("extracted_sprites/animations")

    print("\n下一步：")
    print("1. 重新打包动画精灵图集")
