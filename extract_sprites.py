#!/usr/bin/env python3
"""
精灵图集提取工具
从 assets.png 中提取所有单个精灵图片
"""

import json
import os
from PIL import Image

def extract_sprites(atlas_path, json_path, output_dir):
    """
    从精灵图集中提取所有精灵

    Args:
        atlas_path: 精灵图集 PNG 文件路径
        json_path: 精灵坐标 JSON 文件路径
        output_dir: 输出目录
    """
    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)

    # 读取精灵图集
    print(f"正在加载精灵图集: {atlas_path}")
    atlas = Image.open(atlas_path)
    print(f"图集尺寸: {atlas.size}")

    # 读取坐标配置
    print(f"正在加载坐标配置: {json_path}")
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    frames = data.get('frames', {})
    print(f"找到 {len(frames)} 个精灵")

    # 提取每个精灵
    extracted_count = 0
    for sprite_name, sprite_info in frames.items():
        try:
            frame = sprite_info['frame']
            x, y, w, h = frame['x'], frame['y'], frame['w'], frame['h']

            # 裁剪精灵
            sprite = atlas.crop((x, y, x + w, y + h))

            # 保存精灵
            output_path = os.path.join(output_dir, f"{sprite_name}.png")
            sprite.save(output_path)

            extracted_count += 1
            if extracted_count % 50 == 0:
                print(f"已提取 {extracted_count}/{len(frames)} 个精灵...")

        except Exception as e:
            print(f"提取 {sprite_name} 失败: {e}")

    print(f"\n✅ 完成！共提取 {extracted_count} 个精灵到: {output_dir}")

if __name__ == "__main__":
    # 配置路径
    base_dir = "vasugame/lib/Game/img"

    # 提取 assets.png
    print("=" * 60)
    print("提取主 UI 精灵图集")
    print("=" * 60)
    extract_sprites(
        atlas_path=f"{base_dir}/assets.png",
        json_path=f"{base_dir}/assets.json",
        output_dir="extracted_sprites/assets"
    )

    # 提取 animations.png
    print("\n" + "=" * 60)
    print("提取动画精灵图集")
    print("=" * 60)
    extract_sprites(
        atlas_path=f"{base_dir}/animations.png",
        json_path=f"{base_dir}/animations.json",
        output_dir="extracted_sprites/animations"
    )

    print("\n" + "=" * 60)
    print("所有精灵已提取完成！")
    print("=" * 60)
