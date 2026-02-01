#!/usr/bin/env python3
"""
精灵图集打包工具
将单个精灵重新打包成精灵图集
"""

import json
import os
from PIL import Image
import math

def pack_sprites(sprites_dir, output_atlas, output_json, max_width=2048):
    """
    将目录中的精灵打包成精灵图集

    Args:
        sprites_dir: 精灵目录
        output_atlas: 输出图集路径
        output_json: 输出 JSON 路径
        max_width: 最大宽度
    """
    # 收集所有精灵
    sprites = []
    for filename in sorted(os.listdir(sprites_dir)):
        if filename.lower().endswith('.png'):
            sprite_path = os.path.join(sprites_dir, filename)
            img = Image.open(sprite_path)
            sprite_name = os.path.splitext(filename)[0]
            sprites.append({
                'name': sprite_name,
                'image': img,
                'width': img.width,
                'height': img.height
            })

    if not sprites:
        print("错误：没有找到精灵文件")
        return

    print(f"找到 {len(sprites)} 个精灵")

    # 按高度排序（简单的打包算法）
    sprites.sort(key=lambda s: s['height'], reverse=True)

    # 计算布局
    current_x = 0
    current_y = 0
    row_height = 0
    atlas_width = 0
    atlas_height = 0

    for sprite in sprites:
        # 如果当前行放不下，换行
        if current_x + sprite['width'] > max_width:
            current_x = 0
            current_y += row_height + 2  # 2px 间距
            row_height = 0

        # 记录位置
        sprite['x'] = current_x
        sprite['y'] = current_y

        # 更新位置
        current_x += sprite['width'] + 2  # 2px 间距
        row_height = max(row_height, sprite['height'])

        # 更新图集尺寸
        atlas_width = max(atlas_width, current_x)
        atlas_height = max(atlas_height, current_y + sprite['height'])

    # 创建图集
    print(f"创建图集: {atlas_width}x{atlas_height}")
    atlas = Image.new('RGBA', (atlas_width, atlas_height), (0, 0, 0, 0))

    # 粘贴精灵
    frames = {}
    for sprite in sprites:
        atlas.paste(sprite['image'], (sprite['x'], sprite['y']))

        # 记录坐标
        frames[sprite['name']] = {
            "frame": {
                "x": sprite['x'],
                "y": sprite['y'],
                "w": sprite['width'],
                "h": sprite['height']
            },
            "rotated": False,
            "trimmed": False,
            "spriteSourceSize": {
                "x": 0,
                "y": 0,
                "w": sprite['width'],
                "h": sprite['height']
            },
            "sourceSize": {
                "w": sprite['width'],
                "h": sprite['height']
            }
        }

    # 保存图集
    atlas.save(output_atlas)
    print(f"✓ 图集已保存: {output_atlas}")

    # 保存 JSON
    json_data = {
        "frames": frames,
        "meta": {
            "image": os.path.basename(output_atlas),
            "size": {"w": atlas_width, "h": atlas_height},
            "scale": "1"
        }
    }

    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=2)
    print(f"✓ 配置已保存: {output_json}")

if __name__ == "__main__":
    print("=" * 60)
    print("精灵图集打包工具")
    print("=" * 60)

    # 示例：重新打包 assets
    # pack_sprites(
    #     sprites_dir="recolored_sprites",  # 修改后的精灵目录
    #     output_atlas="vasugame/lib/Game/img/assets_new.png",
    #     output_json="vasugame/lib/Game/img/assets_new.json",
    #     max_width=2048
    # )

    print("\n使用方法：")
    print("1. 将修改后的精灵放在一个目录中")
    print("2. 取消注释上面的示例代码")
    print("3. 修改路径")
    print("4. 运行脚本")
    print("\n注意：这是简单的打包算法，专业项目建议使用 TexturePacker")
