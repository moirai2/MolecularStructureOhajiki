# MolPuzzle (Molecule Puzzle)

[日本語](./puzzle.md) | **English**

> 🧩 **Solo puzzle: use every marble, exactly.** Arrange 9 molecules in a 3×3 grid and connect each adjacent pair by a shared element. Solve a puzzle by using the given marble budget with no leftover.

A solo puzzle: place 9 molecule cards into a 3×3 grid and connect every pair of adjacent cards by **comparing the count of a shared element**. For example, place Water next to Ethanol — both contain 1 oxygen, so they can be connected by oxygen. If the counts differ, you bridge the gap with marbles for the difference. **The puzzle is solved when your given marble budget is used exactly to connect every adjacent pair.**

- **Players:** 1 (solo)
- **Time:** 10–20 min per puzzle
- **Age:** 12+

> 📘 **Marble colors and how to read a card → [COMPONENTS.en.md](./COMPONENTS.en.md)**
> 📗 **Chemistry terms → [GLOSSARY.en.md](./GLOSSARY.en.md)**

---

## Components

- **Puzzle:** Pick one from [the `puzzles/public/` folder on GitHub](https://github.com/moirai2/MolecularStructureOhajiki/tree/main/puzzles/public) or from [X (@AkiraMeruru)'s daily posts](https://x.com/AkiraMeruru)
  (each puzzle specifies "the 9 molecule cards to use" and "the marble colors and counts to use")
- **9 molecule cards:** Take the specified cards from your MolOhajiki set
- **Marbles:** Take the specified colors and counts from your MolOhajiki set

---

## Adjacency rule (core mechanic)

Cards arranged in the 3×3 grid are connected on every adjacent pair, up/down/left/right (**12 pairs in total**; diagonals don't count).

Here's a **sample puzzle** as a walkthrough.

### Puzzle

![Sample puzzle problem](../puzzles/question/5b1c7f20.svg)

**Figure 1. Puzzle.** The 9 molecule cards (Hydrogen Peroxide, Carboxyl, Hydrogen Sulfide, Acetylene, Dopamine, Serotonin, Amino, Methane, Carbon Dioxide) and the marble budget (Carbon C × 1, Hydrogen H × 1, Nitrogen N × 1, total 3 marbles).

### Solution

![Sample puzzle solution](../puzzles/answer/5b1c7f20.svg)

**Figure 2. Example solution.** Pairs where the chosen element count matches are placed **touching** (cost 0, no marbles in between). Pairs where the count differs are placed **apart**, with the difference in marbles between them. The puzzle is solved when all 3 marbles are used exactly.

### How to connect

For each adjacent pair, choose **1 element** to connect them by.
Whether the **count** (number of that element's atoms in the molecule) is the same or different changes **how you physically place the cards**.

| Condition | Card placement | Cost |
|-----------|----------------|------|
| Chosen element count **matches** on both cards | Place cards **touching** (edge to edge) | 0 marbles (free) |
| Counts **differ** | Place cards **apart**, with the difference in marbles in the gap | 1 marble of that color per unit of difference |

**Constraint:** The element you pick must be present in both cards (count ≥ 1 in each).

### Connection examples (from Puzzle #001)

| Card 1 | Card 2 | Element used | Placement | Cost |
|--------|--------|--------------|-----------|------|
| TNT (O:6) | Glucose (O:6) | O (both 6) | Touching | 0 (free) |
| Hydroxyl (O:1) | Lactic Acid (O:3) | O (diff 1 vs 3) | Apart, 2 red marbles in between | 2 |
| Hydrogen Sulfide (H:2) | TNT (H:5) | H (diff 2 vs 5) | Apart, 3 white marbles in between | 3 |
| Methyl (C:1) | Guanidine (C:1) | C (both 1) | Touching | 0 (free) |

You're free to choose which element to connect by. The puzzle isn't always about minimizing cost — some puzzles can only be solved by deliberately taking expensive connections to spend the exact marble budget.

---

## Flow

1. Pick a puzzle; gather the specified 9 cards and the specified marbles
2. Arrange the 9 cards in a 3×3 grid in any order
3. For each adjacent pair, pick an element to connect by
   - Matching count → cards **touching** (cost 0)
   - Differing count → cards **apart**, with the difference in marbles in the gap
4. Use your marble budget exactly, with every adjacent pair connected → **puzzle solved**

You can rearrange cards as many times as you like. Swapping between touching/apart, or repositioning marbles, is always allowed.

### Failure conditions

- You don't have enough marbles to connect a pair
- You connected all adjacent pairs but have marbles left over (didn't use the budget exactly)

→ Rearrange and try again.

---

## Difficulty

The marble budget for each puzzle is designed to be spent **exactly**.
Just minimizing cost isn't enough — picking which pairs to keep touching vs. spread apart is the heart of the puzzle.

---

## Puzzle problems

→ **[Puzzle problem set](../puzzles/puzzles.en.md)**

New puzzles are added periodically. Puzzles are listed in ascending order by marble count. **If you're new, start from the top** — fewer marbles tend to mean simpler structures.

---

## House Rules Welcome

Number of cards, total marble budget, time limit… feel free to change anything.

**Share your custom rules on X with `#MolPuzzle` — we'd love to hear them.**

---

[← Back to game list](../README.en.md#the-five-games)
