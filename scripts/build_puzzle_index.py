#!/usr/bin/env python3
"""GitHub/puzzles/json/ をスキャンし、puzzles.md / puzzles.en.md を再生成する。

並び順: (created 日付の昇順, ハッシュのアルファベット順) で固定。
連番 #001 から振り直し、問題/解答SVGへのリンク・おはじき総数・Lv構成を表で出力する。

Usage:
  python3 scripts/build_puzzle_index.py            # 生成して書き込み
  python3 scripts/build_puzzle_index.py --dry-run  # 標準出力にプレビュー
"""

import argparse
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
PUZZLES_DIR = os.path.normpath(os.path.join(HERE, "..", "puzzles"))
JSON_DIR = os.path.join(PUZZLES_DIR, "json")
OUT_JA = os.path.join(PUZZLES_DIR, "puzzles.md")
OUT_EN = os.path.join(PUZZLES_DIR, "puzzles.en.md")


def load_puzzles():
    rows = []
    for fname in os.listdir(JSON_DIR):
        if not fname.endswith(".json"):
            continue
        puzzle_hash = os.path.splitext(fname)[0]
        with open(os.path.join(JSON_DIR, fname)) as f:
            data = json.load(f)
        created = data.get("created", "9999-99-99")
        total = data.get("total_budget", sum(data.get("ohajiki_budget", {}).values()))
        levels = data.get("card_levels", [])
        lv1 = levels.count(1)
        lv2 = levels.count(2)
        lv3 = levels.count(3)
        rows.append({
            "hash": puzzle_hash,
            "created": created,
            "total": total,
            "lv1": lv1,
            "lv2": lv2,
            "lv3": lv3,
        })
    rows.sort(key=lambda r: (r["created"], r["hash"]))
    for i, r in enumerate(rows, start=1):
        r["seq"] = i
    return rows


def render_ja(rows):
    lines = [
        "# パズルお題集",
        "",
        "**日本語** | [English](./puzzles.en.md)",
        "",
        "3×3グリッドに9枚のカードを並べ、隣接する全ペアを元素でつなぎましょう。",
        "おはじきを指定の数ぴったりで全12ペアを接続できれば完成です。",
        "",
        "ルールの詳細は [→ 分子パズルのルール](../docs/puzzle.md) を参照してください。",
        "",
        f"全 **{len(rows)}** 問。**おはじき総数**と **Lv構成**（使用カードのレベル内訳）が複雑さの目安になります。",
        "リンクを一度クリックすればブラウザの既読色で解いた問題が分かります。",
        "",
        "| # | 問題 | 解答 | おはじき（個） | Lv1 | Lv2 | Lv3 |",
        "|---|------|------|---------------|-----|-----|-----|",
    ]
    for r in rows:
        seq = f"{r['seq']:03d}"
        q = f"[問題](question/{r['hash']}.svg)"
        a = f"[解答](answer/{r['hash']}.svg)"
        lines.append(f"| {seq} | {q} | {a} | {r['total']} | {r['lv1']} | {r['lv2']} | {r['lv3']} |")
    lines.append("")
    lines.append("*新しいお題は随時追加されます。*")
    lines.append("")
    return "\n".join(lines)


def render_en(rows):
    lines = [
        "# Puzzle Problem Set",
        "",
        "[日本語](./puzzles.md) | **English**",
        "",
        "Arrange 9 cards in a 3×3 grid and connect every adjacent pair by a shared element.",
        "Solve a puzzle by connecting all 12 adjacent pairs with the given marble budget, used exactly.",
        "",
        "See [→ MolPuzzle rules](../docs/puzzle.en.md) for the full rules.",
        "",
        f"**{len(rows)}** puzzles in total. **Marble total** and **Lv mix** (level breakdown of the 9 cards) hint at the difficulty.",
        "Clicking a link once lets your browser's visited-link color mark which puzzles you've already opened.",
        "",
        "| # | Question | Answer | Marbles | Lv1 | Lv2 | Lv3 |",
        "|---|----------|--------|---------|-----|-----|-----|",
    ]
    for r in rows:
        seq = f"{r['seq']:03d}"
        q = f"[Question](question/{r['hash']}.svg)"
        a = f"[Answer](answer/{r['hash']}.svg)"
        lines.append(f"| {seq} | {q} | {a} | {r['total']} | {r['lv1']} | {r['lv2']} | {r['lv3']} |")
    lines.append("")
    lines.append("*New puzzles are added periodically.*")
    lines.append("")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--dry-run", action="store_true",
                        help="ファイルに書かず、先頭20行だけ標準出力に表示")
    args = parser.parse_args()

    rows = load_puzzles()
    ja = render_ja(rows)
    en = render_en(rows)

    if args.dry_run:
        print(f"=== {OUT_JA} (先頭20行) ===")
        print("\n".join(ja.splitlines()[:20]))
        print(f"\n=== {OUT_EN} (先頭20行) ===")
        print("\n".join(en.splitlines()[:20]))
        print(f"\n問題数: {len(rows)}")
        return

    with open(OUT_JA, "w") as f:
        f.write(ja)
    with open(OUT_EN, "w") as f:
        f.write(en)
    print(f"書き込み完了: {len(rows)}問")
    print(f"  {OUT_JA}")
    print(f"  {OUT_EN}")


if __name__ == "__main__":
    main()
