#!/usr/bin/env python3
"""
重新打包 assets 精灵图集
"""

from pack_sprites import pack_sprites

print("=" * 70)
print("重新打包 assets 精灵图集")
print("=" * 70)

pack_sprites(
    sprites_dir="extracted_sprites/assets",
    output_atlas="vasugame/lib/Game/img/assets_new.png",
    output_json="vasugame/lib/Game/img/assets_new.json",
    max_width=2048,
    scale=1.0,              # 可按需改为 0.9 或 0.85 进一步降分辨率
    quantize_colors=192,    # 颜色量化以降体积（如有色带可升到 224/256）
    png_optimize=True,
    png_compress_level=9
)

print("\n✅ 打包完成！")
print("\n下一步：")
print("1. 备份原文件：")
print("   cp vasugame/lib/Game/img/assets.png vasugame/lib/Game/img/assets_backup.png")
print("   cp vasugame/lib/Game/img/assets.json vasugame/lib/Game/img/assets_backup.json")
print("2. 替换文件：")
print("   mv vasugame/lib/Game/img/assets_new.png vasugame/lib/Game/img/assets.png")
print("   mv vasugame/lib/Game/img/assets_new.json vasugame/lib/Game/img/assets.json")
