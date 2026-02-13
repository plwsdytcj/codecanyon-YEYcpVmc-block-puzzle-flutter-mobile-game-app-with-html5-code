#!/usr/bin/env python3
"""
重新打包 animations 精灵图集
"""

from pack_sprites import pack_sprites

print("=" * 70)
print("重新打包 animations 精灵图集")
print("=" * 70)

pack_sprites(
    sprites_dir="extracted_sprites/animations",
    output_atlas="vasugame/lib/Game/img/animations_new.png",
    output_json="vasugame/lib/Game/img/animations_new.json",
    max_width=2048,
    scale=0.92,             # 动画可以小幅降分辨率 
    quantize_colors=160,    # 动画色数往往更多，可用 160-192；如出现色带升到 192
    png_optimize=True,
    png_compress_level=9
)

print("\n✅ 打包完成！")
print("\n下一步：")
print("1. 备份原文件：")
print("   cp vasugame/lib/Game/img/animations.png vasugame/lib/Game/img/animations_backup.png")
print("   cp vasugame/lib/Game/img/animations.json vasugame/lib/Game/img/animations_backup.json")
print("2. 替换文件：")
print("   mv vasugame/lib/Game/img/animations_new.png vasugame/lib/Game/img/animations.png")
print("   mv vasugame/lib/Game/img/animations_new.json vasugame/lib/Game/img/animations.json")
