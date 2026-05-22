#!/usr/bin/env python3
"""GitHub/puzzles/json/ をスキャンし、SVG未生成のパズルを一括生成する。

Usage:
  python3 scripts/puzzle_svg_sync.py            # 未生成のみ
  python3 scripts/puzzle_svg_sync.py --force    # 全件再生成
  python3 scripts/puzzle_svg_sync.py --dry-run  # 対象を表示するだけ
"""

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from generate_puzzle_setup_svg import (
    OUT_DIR_A, OUT_DIR_Q, PUZZLES_DIR,
    build_answer_svg, build_question_svg,
    puzzle_label, write_and_report,
)

JSON_DIR = os.path.join(PUZZLES_DIR, "json")


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--force",   action="store_true", help="既存SVGも再生成する")
    parser.add_argument("--dry-run", action="store_true", help="対象を表示するだけ")
    args = parser.parse_args()

    if not args.dry_run:
        os.makedirs(OUT_DIR_Q, exist_ok=True)
        os.makedirs(OUT_DIR_A, exist_ok=True)

    hashes = sorted(
        os.path.splitext(f)[0]
        for f in os.listdir(JSON_DIR)
        if f.endswith(".json")
    )
    print(f"JSONファイル: {len(hashes)}件")

    generated = skipped = errors = 0

    for puzzle_hash in hashes:
        q_svg = os.path.join(OUT_DIR_Q, f"{puzzle_hash}.svg")
        a_svg = os.path.join(OUT_DIR_A, f"{puzzle_hash}.svg")
        both_exist = os.path.exists(q_svg) and os.path.exists(a_svg)

        if both_exist and not args.force:
            skipped += 1
            continue

        json_path = os.path.join(JSON_DIR, f"{puzzle_hash}.json")
        with open(json_path) as f:
            puzzle = json.load(f)

        label = puzzle_label(json_path)

        if args.dry_run:
            print(f"  [{puzzle_hash}] → 生成予定")
            generated += 1
            continue

        try:
            write_and_report(build_question_svg(puzzle, label, style="text"), q_svg,
                             want_png=False, png_width=0)
            write_and_report(build_answer_svg(puzzle, label, style="text"),   a_svg,
                             want_png=False, png_width=0)
            generated += 1
        except Exception as e:
            print(f"  ERROR [{puzzle_hash}]: {e}", file=sys.stderr)
            errors += 1

    action = "生成予定" if args.dry_run else "生成"
    print(f"\n{action}: {generated}件 / スキップ（既存）: {skipped}件"
          + (f" / エラー: {errors}件" if errors else ""))


if __name__ == "__main__":
    main()
