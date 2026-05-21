# MolOhajiki (Molecular Structure Ohajiki)

[日本語](./molohajiki.md) | **English**

> 🧪 **The main game in the series.** Flick ohajiki marbles to gather elements and buy molecule cards in an engine-building duel. Race to claim "the most" in each of the 5 element categories.

A dexterity game with educational depth: flick ohajiki marbles to collect elements and acquire molecule cards. You compete in five element categories — **Carbon, Hydrogen, Oxygen, Nitrogen, Other** — and **whoever wins the most categories takes the game**.

- **Players:** 2 only
- **Time:** 30–45 min
- **Age:** 10+

> 📘 **Marble colors and how to read a card → [COMPONENTS.en.md](./COMPONENTS.en.md)**
> 📗 **Chemistry terms (elements, molecular formulas, functional groups) → [GLOSSARY.en.md](./GLOSSARY.en.md)**

---

## Setup

1. Put all **ohajiki marbles** (50 total = 5 colors × 10) into the bag
2. Separate the **molecule cards** into Lv1, Lv2, Lv3, shuffle each, and place them face-down beside the play area
3. Draw **12 cards from the Lv1 deck** and lay them face-up in a **3×4 grid** (recommended; for tight tables a 3×3 / 9-card grid is acceptable)
4. Give each player **5 element cards** (Carbon, Hydrogen, Oxygen, Nitrogen, Other) and **1 launcher card**
   - Lay the element cards face-up in a row in front of the player
   - Place the **launcher** on the player's side of the grid, slightly separated from the element cards. The launcher can be slid freely along that edge to aim at different cards
5. Decide the starting player by rock-paper-scissors

> **Note:** Players start with **no marbles in hand**. You draw 3 from the bag at the start of your turn.

The diagram below shows a 2-player setup ([larger view](./molohajiki_setup.svg)).

![MolOhajiki setup](./molohajiki_setup.svg)

---

## Flow of play

Starting with the start player, players take turns clockwise. A turn has 3 steps:
**(1) Flick a marble → (2) Buy a card (optional) → End-of-turn upkeep.**

> 📌 **Where things go when used up:** Marbles return to the **bag**. Used cards (decomposed or pushed out of a slot) go to the **discard pile** at the edge of the table. Cards in the discard pile are not reused.

### 1. Flick a marble

This step covers "**launch the marble → check where it lands → grant a purchase right or return it to the bag**." The actual purchase happens in step (2).

1. Draw **3 marbles** randomly from the bag and keep all of them in hand
   - If the bag has fewer than 3: take whatever's there (0 = draw nothing)

2. If you have a card you want, slide your launcher along **your own edge of the grid** to aim (you can reposition before flicking, but cannot move it past corners onto a different edge)

3. Choose **1 marble** from your hand and flick it from the launcher toward the card you want

**If your hand is empty, you must pass. Otherwise you must flick one marble, even if you don't intend to buy.**

#### Landing check

If a marble is touching a card at all, it counts as **landed on that card**.

**If a marble straddles multiple cards (quantum mechanics model):** When a marble physically touches multiple cards, it counts as **landed on all of them simultaneously** (skilled players sometimes straddle on purpose). Which card it "really" belongs to isn't decided in advance — **the player chooses one card at the moment they claim the purchase right** (observation collapses the state). One marble = one card's worth of purchase right at most.

| Landing outcome | Result |
|-----------------|--------|
| Touches a card (**any color**) | Gain a **purchase right** for that card → decide whether to buy in step (2) |
| Lands off the play area / touches no card | The flicked marble **returns to the bag** (no purchase right, end of turn) |

> 💡 You flick only 1 marble per turn, so you can earn at most **1 card's worth of purchase right**.

#### Leftover marbles (terminology)

Marbles sitting on a card that haven't been collected by anyone yet are called **leftover marbles**.

- Any number can pile up on the same card
- When someone eventually buys that card, **the buyer gets all leftover marbles** on it (their own and the opponent's)

### 2. Acquire a molecule card (optional)

**Purchasing is optional.** You can buy **at most 1** card you gained a purchase right for this turn (the card your marble landed on).

- **If you don't buy** → the flicked marble stays on the card as a **leftover marble** (end of turn)
- **If you buy** → follow the procedure below

**Purchase procedure:**

1. Check the molecular formula on the card you have a purchase right for

2. **Cost reduction** (automatic)
   - **A hydrogen slot reduces only hydrogen; an oxygen slot reduces only oxygen** (elements other than the slot you placed the card in count for neither cost reduction nor scoring)
   - The reduction equals the number of that element in the card
   - Example: H₂O (H=2, O=1) placed in the **hydrogen slot** → hydrogen cost is reduced by **2**
   - Example: H₂O (H=2, O=1) placed in the **oxygen slot** → oxygen cost is reduced by **1**
   - No declaration needed — just keep the slot visible to your opponent

3. **Payment:** Pay the reduced cost using **marbles in your hand** (paid marbles **return to the bag**)
   - The marble you just flicked (currently on the card) cannot be used to pay
   - Leftover marbles on the card cannot be used to pay either (you collect those after purchase)
   - **If you can't pay** → the purchase right is lost; the flicked marble becomes a **leftover marble** on that card

4. **Acquire the card → place it in an element slot.** Place the new card in one of your 5 element slots (placement/rearrangement rules below)

5. **Collect marbles:**
   - The marble you flicked → back to your hand
   - All **leftover marbles** on the card → all to your hand

#### Card placement and rearrangement

After you acquire a new card, you may freely rearrange your element slots **until the start of your next turn** (rearrangement is allowed any number of times, even during opponents' turns).

In addition:
- **5-card limit:** You can have at most 5 cards in your element slots. If all 5 are full, you must send 1 existing card to the **discard pile** before placing the new one (discarded cards cannot be reused)
- **Locking timing:** Your placement locks at the start of your next turn. You cannot rearrange again until you acquire another card

### End-of-turn upkeep

After placement/rearrangement, process the following in order:

1. **Functional group point end check:** If your total is 10 fg pt or more → triggers game end (see [End condition](#end-condition))
2. **Hand size cap check:** Return any marbles exceeding the limits below to the bag

| Limit type | Maximum |
|------------|---------|
| Total marbles in hand | **10 total** |
| Same-color marbles | **5 of any one color** |

> Going over the cap mid-turn is fine. As long as you're at or below the cap after paying, no discard is required.

3. **Refill the grid:** Fill empty slots face-up from the decks (**prefer the same level first**; if that level is empty, draw from the next level up)
4. Pass the turn to the next player

---

## Ending the game

### End condition

**As soon as any player, after placing/rearranging their cards, reaches a total of 10 or more functional group points, the game ends at the end of that round.**

- If you fill all 5 slots and then discard one, dropping back below 10 fg pt, the game continues
- The game also ends when **all decks are exhausted AND the grid is empty**

After all players have taken the same number of turns (1 full round), proceed to scoring.

**Example:** In a 2-player game, if player A (going first) reaches 10+ fg pt → player B takes their turn, then you score.

### Scoring (majority system)

**Step 1: Total each element** (for all 5 categories)
- Marbles of that color on the matching element card
- Element count from molecule cards placed in that slot — but **only** the element of the slot itself

**Important:** A card only contributes the element of the slot it's in. Other elements on the card don't count.
- Example: H₂O (H=2, O=1) placed in the hydrogen slot → contributes only 2 hydrogen

**Step 2: Determine the majority for each element**
- The player with the most → wins **1 category**
- Tie: the player with more functional group points in that slot wins
- Still tied: all tied players win the category

**Step 3: Determine the overall winner**

The player who won the most element categories wins.

**Tiebreakers** (if category wins are tied):
1. Higher total functional group points (fg pt)
2. Marble showdown — draw 1 marble from the bag and compare totals of that color's element

**Scoring example:**

| Player | C | H | O | N | Other | Categories won |
|--------|---|---|---|---|-------|----------------|
| Alice | 8 | 12 | 7 | 2 | 1 | 2 (C, O) |
| Bob | 6 | 15 | 5 | 4 | 2 | 3 (H, N, Other) |

→ Bob wins.

---

## FAQ

### Q: Does landing on a card always grant a purchase right?
A: Yes. Regardless of marble color, touching a card at all earns you the purchase right.

### Q: What happens to a marble that lands on a card I don't buy?
A: It stays on the card as a leftover marble. Whoever eventually buys that card collects all leftover marbles on it (yours and your opponent's).

### Q: Are there hand-size limits?
A: Two caps: (1) max 10 total marbles, (2) max 5 of any single color. Return any excess to the bag (checked at end of turn).

### Q: What if the bag runs low?
A: Draw whatever's there (0 = no draw). If you want a card, you can still flick from your hand. If your hand is also empty, you must pass.

### Q: I placed H₂O in the hydrogen slot. Can I also use it as oxygen?
A: No. H₂O in the hydrogen slot only contributes 2 hydrogen. Only the slot's element counts.

### Q: When does the game end?
A: When any player reaches 10+ fg pt, the round finishes and the game ends. It also ends if all decks are exhausted and the grid is empty.

### Q: Does reaching 10+ fg pt automatically win the game?
A: No. It only triggers the end. Victory is decided by element majorities — the player who wins the most of the 5 categories.

---

# Advanced rules

## Card decomposition ⭐

> An advanced rule that lets you discard one of your owned cards as a one-shot aid to acquire a bigger molecule.

When acquiring a new molecule card, you can **decompose** an existing card to reduce the cost.

**Reduction vs. decomposition:**

| | Reduction | Decomposition |
|--|-----------|---------------|
| Card handling | Stays in the slot | Sent to discard |
| Usable elements | **Only the slot's element** | **Choose 1 element** from the card |
| Usage frequency | Any number of times | Once, then gone |
| Example (H₂O, H=2, O=1) | In H slot: -2 H only | Choose -2 H **or** -1 O |

- **You can't do both with the same card** (once you remove it from the slot, only decomposition applies)
- With multiple cards, one can be used for reduction and another for decomposition

**Decomposition procedure:**
1. Declare "I'm decomposing this card" and remove 1 card from your element slots (cannot be undone)
2. Choose **1 element** present in that card and reduce the cost by that element's count
   - Example: H₂O → choose either "-2 H" or "-1 O"
3. Put the decomposed card in the discard pile (cannot be reused)
4. Pay the reduced cost with marbles (treat any negative cost as 0)

**Note:** Standard rule allows decomposing at most 1 card per turn.

**Decomposition example:**

Target card: C₂H₆O (Ethanol), base cost C2 H6 O1

| Card to decompose | Choice | Remaining cost |
|-------------------|--------|----------------|
| H₂O | Hydrogen | C2 H4 O1 |
| H₂O | Oxygen | C2 H6 (oxygen = 0!) |

**Combining reduction and decomposition:**
- CO₂ in carbon slot → reduction (−1 C, stays in slot)
- H₂O in oxygen slot → decompose, choose oxygen (−1 O, goes to discard)
- Net cost: C1 H6

**Important:** You can't decompose a card you just acquired this turn (1 card max acquired per turn).

### Decomposition FAQ

**Q: What's the difference between reduction and decomposition?**
A: **Reduction** keeps the card in the slot and shrinks cost permanently (reusable). **Decomposition** sends the card to discard for a one-shot reduction, but lets you choose any one element on the card. You can't do both with the same card.

**Q: Do I have to buy a card once I have a purchase right?**
A: No, buying is optional. If you don't, the flicked marble stays on the card as a leftover marble.

---

## Variant list

Pick from the options below before starting. You can combine freely.

### 1. Card decomposition

| Option | Description | Recommended for |
|--------|-------------|-----------------|
| None | No decomposition mechanic | Beginners |
| **1 card limit** | Decompose at most 1 card per turn | Standard |
| Unlimited | Decompose any number per turn | Experts / solo |

### 2. Cards used

| Option | Description | Recommended for |
|--------|-------------|-----------------|
| **All levels** | Use Lv1–Lv3 (50 cards) | Standard (age 10+) |
| Lv1 only | Shopping mode (20 cards, no slots) | Age 7+ |
| None | Marbles only | Age 5+ |

### 3. Movement rules

| Option | Description | Recommended for |
|--------|-------------|-----------------|
| **Fixed** | Stay seated | Low / small table |
| Free | Stand up and move around the table | Large table |

### 4. End condition

| Option | Description | Recommended for |
|--------|-------------|-----------------|
| **10-point system** | Round ends when someone hits 10+ fg pt | Standard |
| Turn limit | End after a fixed number of turns | Time-boxing / kids |

**Recommended turn count for turn limit:** 10 turns per player (~30–40 minutes)

**Note:** Don't combine "Lv1 only" with the point system — the game may not be able to end (Lv1 max is +1 fg pt, and the 5-card limit caps you at 5 fg pt).

### 5. Victory condition

| Option | Description | Recommended for |
|--------|-------------|-----------------|
| **Majority system** | Compete for #1 in each of the 5 categories | Standard (age 10+) |
| Card count | Most cards wins | Age 7+ |
| Marble total | Most marbles wins | Age 5+ |

### 6. End-trigger threshold

| Option | Description | Recommended for |
|--------|-------------|-----------------|
| **10 fg pt** | Standard | All players |
| 12–15 fg pt | Longer game | Players who want deeper play |

### Recommended combinations

| Target | Cards | Decomp. | End | Victory |
|--------|-------|---------|-----|---------|
| **Age 5+** | None | – | Turn limit | Marble total |
| **Age 7+** | Lv1 only | None | Turn limit | Card count |
| **Age 10+ (beginner)** | All | None | 10 fg pt | Majority |
| **Age 10+ (standard)** | All | Yes | 10 fg pt | Majority |

---

## Handicap rules

For games with skill gaps (e.g., a flick-savvy adult vs. an unfamiliar child). Agree on the handicaps with all players before starting.

**Design principle: "Make the stronger side weaker."**

### Distance handicap
The stronger player places their launcher 10–20 cm farther from the grid (or at an angle)

### Off-hand handicap (most practical)
The stronger player flicks with their non-dominant hand

### Resource handicap
Give the weaker player 5 marbles to start with

### Blindfold handicap
The stronger player closes their eyes while flicking

### Accuracy penalty
When the stronger player successfully lands on their target, deduct 1 point (or give 1 point to the opponent)

### Suggested combinations

| Matchup | Recommended handicap |
|---------|---------------------|
| Adult vs. age 6–8 | Off-hand + distance |
| Adult vs. age 9–12 | Off-hand only |
| Veteran vs. beginner (same age) | Distance or resource |
| Party / laughs first | Blindfold |

---

## Learn about the molecules

The molecules in this game are all around you in daily life.
Check the description on each card, or look them up online.

---

[← Back to game list](../README.en.md#the-five-games)
