#!/usr/bin/env python3
"""
分子パズル お題ジェネレーター

Usage:
  python scripts/puzzle_generator.py                      # 1問、ランダム
  python scripts/puzzle_generator.py --count 10          # 10問生成
  python scripts/puzzle_generator.py --seed 42           # 再現可能
  python scripts/puzzle_generator.py --test              # 動作確認（seed=0固定）

パズルID:
  選んだ9枚のカードID（ソート済み）のSHA256先頭8文字
  例: "8,9,17,29,32,37,38,42,43" → sha256 → a3f2b1c0

出力:
  puzzles/{hash}.json        完全版（解答含む、ローカル保管）
  puzzles/public/{hash}.json 公開版（解答なし、GitHub用）
  puzzles/public/index.json  投稿番号↔ハッシュのマッピング
"""

import csv, hashlib, json, random, itertools, argparse
from pathlib import Path
from datetime import date

ELEMENTS = ['C', 'H', 'O', 'N', 'etc']
ELEMENT_COLOR = {
    'C': '緑(炭素)',
    'H': '水色(水素)',
    'O': '赤(酸素)',
    'N': '青(窒素)',
    'etc': '黄(その他)',
}

# 3×3グリッドの隣接ペア（行優先 0〜8）
# 0 1 2
# 3 4 5
# 6 7 8
ADJACENT_PAIRS = [
    (0,1),(1,2),(3,4),(4,5),(6,7),(7,8),  # 横
    (0,3),(1,4),(2,5),(3,6),(4,7),(5,8),  # 縦
]


def load_molecules(csv_path):
    molecules = []
    with open(csv_path, encoding='utf-8') as f:
        for row in csv.DictReader(f):
            molecules.append({
                'id':       int(row['id']),
                'formula':  row['formula'],
                'name_jp':  row['name_jp'],
                'level':    int(row['level']),
                'C':        int(row['C']),
                'H':        int(row['H']),
                'O':        int(row['O']),
                'N':        int(row['N']),
                'etc':      int(row['etc']),
            })
    return molecules


def make_puzzle_id(card_ids, budget):
    """ソート済みカードID＋おはじき予算からSHA256先頭8文字のハッシュを生成。
    同じ9枚でも予算（元素内訳）が違えば別ハッシュになる。"""
    ids_part = ",".join(str(i) for i in sorted(card_ids))
    budget_part = "|" + ",".join(f"{e}:{budget[e]}" for e in ELEMENTS)
    return hashlib.sha256((ids_part + budget_part).encode()).hexdigest()[:8]


def best_connection(card_a, card_b):
    """2枚のカードを接続する最安元素とコストを返す。有効な元素がなければNone。"""
    best = None
    for e in ELEMENTS:
        if card_a[e] > 0 and card_b[e] > 0:
            cost = abs(card_a[e] - card_b[e])
            if best is None or cost < best['cost']:
                best = {'element': e, 'cost': cost,
                        'a': card_a[e], 'b': card_b[e]}
    return best


def evaluate_arrangement(cards):
    """9枚の配置を評価。全ペアの最安コストを合計して返す。
    接続不可ペアがあればNoneを返す。"""
    total = 0
    breakdown = {e: 0 for e in ELEMENTS}
    connections = []
    for i, j in ADJACENT_PAIRS:
        conn = best_connection(cards[i], cards[j])
        if conn is None:
            return None
        breakdown[conn['element']] += conn['cost']
        total += conn['cost']
        connections.append({
            'pos': [i, j],
            'element': conn['element'],
            'cost': conn['cost'],
            'counts': [conn['a'], conn['b']],
        })
    return {'total': total, 'breakdown': breakdown, 'connections': connections}


def generate_puzzle(molecules, seed=None, fixed_cards=None):
    """9枚を選択し全配置を探索して最小コストの配置を返す。
    fixed_cards: 分子式のリスト（指定時はランダム選択しない）"""
    if fixed_cards is not None:
        mol_by_formula = {m['formula']: m for m in molecules}
        missing = [f for f in fixed_cards if f not in mol_by_formula]
        if missing:
            print(f"エラー: 見つからない分子式: {missing}")
            return None
        if len(fixed_cards) != 9:
            print(f"エラー: --cards には9枚必要です（{len(fixed_cards)}枚指定）")
            return None
        selected = [mol_by_formula[f] for f in fixed_cards]
    else:
        if seed is not None:
            random.seed(seed)
        selected = random.sample(molecules, 9)

    best_total = None
    best_result = None
    best_perm = None
    valid_count = 0

    for perm in itertools.permutations(range(9)):
        cards = [selected[i] for i in perm]
        result = evaluate_arrangement(cards)
        if result is None:
            continue
        valid_count += 1
        if best_total is None or result['total'] < best_total:
            best_total = result['total']
            best_result = result
            best_perm = list(perm)

    if best_total is None:
        return None

    card_ids = [m['id'] for m in selected]

    # おはじき予算 = 最小コストの各元素内訳
    budget = dict(best_result['breakdown'])
    puzzle_id = make_puzzle_id(card_ids, budget)

    return {
        'id':             puzzle_id,
        'card_ids':       card_ids,
        'cards':          [m['formula'] for m in selected],
        'card_names_jp':  [m['name_jp']  for m in selected],
        'card_levels':    [m['level']    for m in selected],
        'ohajiki_budget': budget,
        'total_budget':   sum(budget.values()),
        'min_cost':       best_total,
        'valid_arrangements': valid_count,
        'created':        str(date.today()),
        # 解答（公開版からは除外）
        '_solution_order':       best_perm,
        '_solution_breakdown':   best_result['breakdown'],
        '_solution_connections': best_result['connections'],
    }


def save_puzzle(puzzle, path):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(puzzle, f, ensure_ascii=False, indent=2)


def print_puzzle_summary(puzzle):
    cards_str = ', '.join(puzzle['card_names_jp'])
    budget_parts = [
        f"{ELEMENT_COLOR[e]}:{v}"
        for e, v in puzzle['ohajiki_budget'].items() if v > 0
    ]
    print(f"  [{puzzle['id']}]: {cards_str}")
    print(f"         最小コスト={puzzle['min_cost']} / 予算合計={puzzle['total_budget']}"
          f" / 有効配置={puzzle['valid_arrangements']:,}")
    print(f"         おはじき: {' / '.join(budget_parts)}")


def main():
    parser = argparse.ArgumentParser(description='分子パズル お題ジェネレーター')
    parser.add_argument('--count',  type=int, default=1)
    parser.add_argument('--seed',   type=int, default=None)
    parser.add_argument('--test',   action='store_true')
    parser.add_argument('--cards',  type=str, default=None,
                        help='カンマ区切りで9枚の分子式を指定（例: H2O,-OH,CO2,...）')
    parser.add_argument('--created', type=str, default=None,
                        help='作成日（YYYY-MM-DD、省略時は今日）')
    args = parser.parse_args()

    if args.test:
        args.count = 2
        args.seed  = 0
        print("=== テストモード（seed=0、2問） ===")

    root = Path(__file__).parent.parent
    csv_path = root / 'data' / 'molecules.csv'
    if not csv_path.exists():
        print(f"エラー: {csv_path} が見つかりません")
        return 1

    molecules = load_molecules(csv_path)
    print(f"分子カード読み込み: {len(molecules)}枚")

    puzzle_dir = root / 'GitHub' / 'puzzles' / 'json'
    puzzle_dir.mkdir(parents=True, exist_ok=True)

    # --cards モード（1問固定生成）
    if args.cards is not None:
        fixed = [f.strip() for f in args.cards.split(',')]
        puzzle = generate_puzzle(molecules, fixed_cards=fixed)
        if puzzle is None:
            return 1
        if args.created:
            puzzle['created'] = args.created
        puzzle_id = puzzle['id']
        out_path = puzzle_dir / f"{puzzle_id}.json"
        if out_path.exists():
            print(f"既存: [{puzzle_id}] — 上書きしません")
            print_puzzle_summary(puzzle)
            return 0
        save_puzzle(puzzle, out_path)
        print_puzzle_summary(puzzle)
        print(f"\n保存: {puzzle_id}.json")
        return 0

    generated = 0
    skipped   = 0
    duplicates = 0

    for i in range(args.count):
        seed   = (args.seed + i) if args.seed is not None else None
        puzzle = generate_puzzle(molecules, seed=seed)

        if puzzle is None:
            print("  有効な配置なし（スキップ）")
            skipped += 1
            continue

        puzzle_id = puzzle['id']
        out_path  = puzzle_dir / f"{puzzle_id}.json"

        if out_path.exists():
            print(f"  [{puzzle_id}]: 重複（スキップ）")
            duplicates += 1
            continue

        save_puzzle(puzzle, out_path)
        print_puzzle_summary(puzzle)
        generated += 1

    print(f"\n生成: {generated}問 / 重複: {duplicates}問 / スキップ: {skipped}問")
    print(f"保存先: {puzzle_dir}/")
    return 0


if __name__ == '__main__':
    exit(main())
