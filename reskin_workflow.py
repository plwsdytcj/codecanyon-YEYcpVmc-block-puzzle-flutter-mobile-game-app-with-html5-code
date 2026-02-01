#!/usr/bin/env python3
"""
一键 Reskin 工作流
自动化处理精灵提取、颜色替换、重新打包
"""

import os
import sys
from extract_sprites import extract_sprites
from recolor_sprites import batch_replace_color, adjust_brightness, adjust_saturation
from pack_sprites import pack_sprites

def reskin_workflow():
    """
    完整的 reskin 工作流
    """
    print("=" * 70)
    print("Block Puzzle 游戏 Reskin 自动化工具")
    print("=" * 70)

    # 步骤 1: 提取精灵
    print("\n[步骤 1/4] 提取精灵...")
    print("-" * 70)
    extract_sprites(
        atlas_path="vasugame/lib/Game/img/assets.png",
        json_path="vasugame/lib/Game/img/assets.json",
        output_dir="reskin_workspace/1_extracted"
    )

    # 步骤 2: 颜色替换（示例）
    print("\n[步骤 2/4] 应用颜色主题...")
    print("-" * 70)
    print("提示：编辑此脚本来定义你的颜色方案")

    # 示例颜色替换配置
    color_replacements = [
        # (旧颜色 RGB, 新颜色 RGB, 容差)
        # ((255, 0, 0), (0, 100, 255), 30),  # 红色 -> 蓝色
        # ((0, 255, 0), (255, 100, 0), 30),  # 绿色 -> 橙色
    ]

    if color_replacements:
        os.makedirs("reskin_workspace/2_recolored", exist_ok=True)
        for old_color, new_color, tolerance in color_replacements:
            print(f"替换颜色: {old_color} -> {new_color}")
            batch_replace_color(
                input_dir="reskin_workspace/1_extracted",
                old_color=old_color,
                new_color=new_color,
                tolerance=tolerance,
                output_dir="reskin_workspace/2_recolored"
            )
    else:
        print("跳过颜色替换（未配置）")
        print("你可以手动编辑 reskin_workspace/1_extracted 中的精灵")

    # 步骤 3: 调整效果（可选）
    print("\n[步骤 3/4] 调整图像效果...")
    print("-" * 70)
    print("跳过（可选步骤）")

    # 步骤 4: 重新打包
    print("\n[步骤 4/4] 重新打包精灵图集...")
    print("-" * 70)

    source_dir = "reskin_workspace/2_recolored" if color_replacements else "reskin_workspace/1_extracted"

    pack_sprites(
        sprites_dir=source_dir,
        output_atlas="reskin_workspace/3_final/assets_new.png",
        output_json="reskin_workspace/3_final/assets_new.json",
        max_width=2048
    )

    # 完成
    print("\n" + "=" * 70)
    print("✅ Reskin 工作流完成！")
    print("=" * 70)
    print("\n下一步：")
    print("1. 检查 reskin_workspace/3_final/ 中的新图集")
    print("2. 如果满意，替换原文件：")
    print("   cp reskin_workspace/3_final/assets_new.png vasugame/lib/Game/img/assets.png")
    print("   cp reskin_workspace/3_final/assets_new.json vasugame/lib/Game/img/assets.json")
    print("3. 测试游戏：cd vasugame && flutter run")

if __name__ == "__main__":
    try:
        reskin_workflow()
    except Exception as e:
        print(f"\n❌ 错误: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
