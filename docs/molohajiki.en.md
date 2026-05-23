# MolOhajiki (Molecular Structure Ohajiki)

[日本語](./molohajiki.md) | **English**

> 🧪 **The main game in the series.** Flick ohajiki marbles to gather elements and buy molecule cards in an engine-building duel. Compete for "the most" in each of the 5 element categories.

A dexterity game with educational depth: flick ohajiki marbles to collect elements and acquire molecule cards. You compete in five element categories — **Carbon, Hydrogen, Oxygen, Nitrogen, Other** — and **whoever wins the most categories takes the game**.

> Molecule cards carry **functional group points (fg pt)**, which drive the end-game trigger and tiebreaks (see [GLOSSARY.en.md](./GLOSSARY.en.md)).

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
   - **Element cards serve as "element slots": place owned marbles on the matching color card (public information), and stack acquired molecule cards into the slots (1 card per slot max)**
   - Place the **launcher** on the player's side of the grid, slightly separated from the element cards. The launcher can be slid freely along that edge to aim at different cards
5. Set aside **1 title card** beside the play area (used as the marker for the [Purchase right penalty](#purchase-right-penalty))
6. Decide the starting player by rock-paper-scissors

The diagram below shows a 2-player setup ([larger view](./molohajiki_setup.svg)).

![MolOhajiki setup](./molohajiki_setup.svg)

---

## Flow of play

Players take turns alternately, starting with the start player. A turn has 3 steps:
**(1) Flick a marble → (2) Buy a card (optional) → End-of-turn upkeep.**

### 1. Flick a marble

1. Draw **3 marbles** randomly from the bag and keep all of them in hand
   - If the bag has fewer than 3: take whatever's there (0 = draw nothing)

2. Slide your launcher freely along **your own edge of the grid** (you can reposition as many times as you like before flicking, but cannot move it past corners onto a different edge)

3. Choose **1 marble** from your hand and flick it from the launcher

**If your hand is empty, you must pass. Otherwise you must flick one marble, even if you don't intend to buy.**

#### Landing check

If a marble is touching a card at all, it counts as **landed on that card**.

**If a marble straddles multiple cards:** The player chooses 1 card at the moment they claim the purchase right. One marble grants at most 1 card's worth of purchase right.

| Landing outcome | Result |
|-----------------|--------|
| Touches a card (**any color**) | Gain a **purchase right** for that card → decide whether to buy in step (2) |
| Lands off the play area / touches no card | The flicked marble **returns to the bag** (no purchase right, end of turn) |

#### Leftover marbles (terminology)

Marbles sitting on a card that haven't been collected by anyone yet are called **leftover marbles**.

- There is no limit to the number of leftover marbles on a single card
- Leftover marbles stay on the card until someone buys it
- When someone eventually buys that card, **the buyer gets all leftover marbles** on it (their own and the opponent's)

#### Purchase right penalty

If the result of your flick sends any marble **outside the card grid** (your own marble or a leftover marble), **place the title card in front of yourself**.

- While you hold it, **you cannot buy cards** (even if your marble lands, it stays as a leftover)
- The penalty is lifted at **the end of your next turn**
- The moment your opponent commits a violation, **the title card transfers to them**

### 2. Acquire a molecule card (optional)

You can buy **at most 1** card you gained a purchase right for this turn (the card your marble landed on).

- **If you don't buy** → the flicked marble stays on the card as a **leftover marble** (end of turn)
- **If you buy** → follow the procedure below

**Purchase procedure:**

1. Check the molecular formula on the card you have a purchase right for

2. **Cost reduction** (automatic)
   - Molecule cards already placed in your element slots reduce cost by the count of that slot's element
   - Example: H₂O in the hydrogen slot → hydrogen cost **−2**; in the oxygen slot → oxygen cost **−1**

3. **Payment:** Pay the reduced cost using **marbles in your hand** (paid marbles **return to the bag**)
   - Marbles on cards (flicked or leftover) cannot be used to pay
   - **If you can't pay** → the purchase right is lost; the flicked marble becomes a **leftover marble** on that card

4. **Acquire the card → place it in an element slot.** Place the new card in one of your 5 element slots (placement/rearrangement rules below)

5. **Collect marbles:**
   - The marble you flicked → back to your hand
   - All **leftover marbles** on the card → all to your hand

#### Card placement and rearrangement

When you acquire a card, you must **place and finalize it in an element slot during your own turn**. Placement cannot be changed until you acquire the next card.

- **One card per slot** (5 slots, 5 cards max). If all 5 are full, send 1 existing card to the **discard pile** before placing the new one (discarded cards cannot be reused)

### End-of-turn upkeep

After placement/rearrangement, process the following in order:

1. **Functional group point end check:** If your total is 15 fg pt or more → triggers game end (see [End condition](#end-condition))
2. **Hand size cap check:** Return any marbles exceeding the limits below to the bag

| Limit type | Maximum |
|------------|---------|
| Total marbles in hand | **10 total** |
| Same-color marbles | **5 of any one color** |

3. **Refill the grid:** Fill empty slots face-up from the decks (**prefer the same level first**; if that level is empty, draw from the next level up)
4. Pass the turn to the next player

---

## Ending the game

### End condition

**As soon as any player reaches 15 or more functional group points, the game-end trigger fires. Scoring takes place at the end of that round.**

- If you fill all 5 slots and then discard one, dropping back below 15 fg pt, the game continues
- The game also ends when **all decks are exhausted AND the grid is empty**

**Example:** If player A (going first) reaches 15+ fg pt → player B takes their turn, then you score.

### Scoring (majority system)

**Step 1: Total each element** (for all 5 categories)
- Marbles of that color on the matching element card
- Element count from molecule cards placed in that slot — **only the slot's element counts** (other elements on the card are ignored)

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

### Q: I placed H₂O in the hydrogen slot. Can I also use it as oxygen?
A: No. Only the slot's element counts. The hydrogen slot contributes only 2 hydrogen.

### Q: Does reaching 15+ fg pt automatically win the game?
A: No. It only triggers the end. Victory is decided by element majorities — the player who wins the most of the 5 categories.

---

# Advanced rules

## Card decomposition ⭐

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

**Example:** Target C₂H₆O (Ethanol, base cost C2 H6 O1)
- CO₂ in the carbon slot → use for reduction (−1 C, stays in slot)
- H₂O in the oxygen slot → decompose, choose oxygen (−1 O, goes to discard)
- Effective cost: **C1 H6**

You cannot decompose a card you just acquired this turn (1 card max acquired per turn).

---

## Variant list

Pick from the options below before starting. You can combine freely.

### 1. Card decomposition

| Option | Description | Recommended for |
|--------|-------------|-----------------|
| None | No decomposition mechanic | Beginners |
| **1 card limit** | Decompose at most 1 card per turn | Standard |
| Unlimited | Decompose any number per turn | Experts / solo |

### 2. End condition

| Option | Description | Recommended for |
|--------|-------------|-----------------|
| **15-point system** | Round ends when someone hits 15+ fg pt | Standard |
| 10-point system | Shorter game | Beginners / quick play |
| 20-point system | Long game | Players who want deeper play |
| Turn limit | End after a fixed number of turns (10 per player) | Time-boxing |

---

## Handicap rules

For games with skill gaps (e.g., a flick-savvy adult vs. an unfamiliar child). Agree on the handicaps with both players before starting.

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

[← Back to game list](../README.en.md#the-five-games)
