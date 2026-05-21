# TicTacMol (Tic-Tac-Toe × Molecules)

[日本語](./tictacmol.md) | **English**

> 🎯 **Simultaneous-flick tic-tac-toe.** Flick marbles to claim territory; lock a vertical, horizontal, or diagonal row to take the cards. Higher-value cards appear as the board evolves.

A two-player duel: flick marbles simultaneously and try to hold 3 cards in a row — vertical, horizontal, or diagonal — to capture them. Every capture replaces cards with higher-value ones, so the board evolves as you play. You can't see your opponent's current aim, but the marbles left on the board hint at their next move.

- **Players:** 2 only
- **Time:** 15–25 min
- **Age:** 6+ (standard / alternating flicks); 10+ (hardcore / two-handed counter-flick)

> 📘 **Marble colors and how to read a card → [COMPONENTS.en.md](./COMPONENTS.en.md)**
> 📗 **Chemistry terms → [GLOSSARY.en.md](./GLOSSARY.en.md)**

---

## Setup

1. The two players sit **face-to-face across the board**
2. Each player chooses 10 marbles of their color and keeps them in hand
3. Shuffle the Lv1 deck, then place **9 cards face-up in a 3×3 grid**, each card oriented **landscape**
4. Lay **3 element cards (C / H / O) above and below the grid**, also in landscape orientation, as a buffer (the 3 cards together match the grid's width; orient each pair so the labels face the player on that side)
5. Place the **2 player cards (launchers)** outside the element-card rows (further from the grid, on each player's side), one per player, in portrait orientation. **Marbles are placed on the launcher and flicked from there** (the card surface is slippery, which makes flicking easier)
6. Stack the rest of the Lv1, Lv2, and Lv3 decks face-down beside the board (right side recommended)

See the diagram for the setup ([larger view](./tictacmol_setup.svg)).

![TicTacMol setup](./tictacmol_setup.svg)

---

## Flow of play

The game repeats **rounds**. Each round is:

> Both players flick **1 marble each** → update who's holding what → check for three-in-a-row → acquire cards & refill the grid

---

### 1. Simultaneous flick

1. Each player silently chooses a card to target (no talking recommended)
2. Either player calls "**3, 2, 1, GO!**"
3. On "GO!" both players flick 1 marble **from their own launcher card** simultaneously
4. Wait for marbles to **come to a complete stop** (even if marbles collide, only the final resting position matters)
5. **Landing check:** if a marble is touching **any molecule card on the board (Lv1 / Lv2 / Lv3)** at all, it has landed. If it touches no molecule card (fully off the board), return it to its owner
6. **Three-in-a-row check** (below)
7. Acquire cards and refill

> **Note:** If a card shifts during a flick, slide it back into place before resolving.

---

### 2. The "holding" rule

> **"Holding"** = a dynamic state where your marble is on a card. You don't physically take the card until a three-in-a-row completes.

- A card with **any** of your marbles on it is one you **hold**
- While you hold a card, it counts toward your **three-in-a-row check**
- **Holding is not permanent:** if your marble gets knocked off the board, you lose your hold (it no longer counts for the next check)
- Holding alone doesn't capture the card — only completing a three-in-a-row does

**Example:** Round 1 you land on the top-right card → you hold it.
Round 2 your opponent knocks that marble off the board → you lose your hold.

**Shared holding:** Both players can hold the same card at the same time. If your opponent's marble lands on a card you also hold, you don't lose your hold (marble counts don't matter).

#### Marble straddling multiple cards (quantum mechanics model)

When a marble physically touches multiple cards, it counts as **holding all touched cards** at once (skilled players can intentionally straddle). Which card it "really" belongs to is **not decided in advance** — the player chooses when the three-in-a-row check happens (observation collapses the state).

But **at the check, 1 marble = at most 1 card's worth of holding**. The player picks the assignment that's most advantageous.

And **when a card is captured, every marble touching it (including straddlers) is returned to its owner**. Physically lifting a card off the board inevitably moves the marbles on top of it, so the straddlers leave with the card.

The upshot: **you can never lock 3 cards with just 2 marbles** (you need at least 3 marbles for 3 cards — physics enforces this automatically).

---

### 3. Three-in-a-row check

> 🔄 **Resolve both players' completions simultaneously.** Identify all completed lines first, then process captures (neither player's capture can disrupt the other's line check).

If you hold **all 3 cards in any vertical, horizontal, or diagonal line** on the 3×3 grid, you capture those 3 cards.

> ⚠️ Note: this is NOT "place 3 marbles in the same row." It's "**all 3 cards in a row each have at least one of your marbles on them**" (the opponent can have marbles there too — that's fine).

**Simultaneous completion:** If both players complete different lines the same round, **both capture** (whichever cards don't overlap go to each player).

**Shared cards:** If both players' completed lines pass through the **same card**, neither captures that card and it stays on the board. All marbles on a shared card (from either player) return to their owners — the shared card is reset as "neutral territory."

**Shared card example:** A completes the middle row, B completes the middle column. Each cell shows who holds that card; ★ is the shared card both hold.

|  | Left | Center | Right |
|:---:|:---:|:---:|:---:|
| Top | — | B | — |
| Middle | A | **★** | A |
| Bottom | — | B | — |

★ (center) is where both lines cross → it stays on the board. **A and B each capture 2 cards** (the two non-center cards on their lines). All marbles on ★ are returned to their owners.

**Multi-line captures (multiple lines completed by 1 marble):**

If a single marble lands at the intersection of multiple lines and you were already holding the other cards on those lines, you can complete multiple lines at once.

| Lines completed | Cards captured | Example |
|-----------------|----------------|---------|
| 1 line | 3 | One horizontal row |
| 2 lines (share 1 card at intersection) | 5 | Row + column / row + diagonal (center is the shared card) |
| 3 lines (share 1 card at intersection) | 7 (the practical maximum) | Vertical + horizontal + diagonal all through the center |

**Example:** You already hold **both diagonal corners (top-left + bottom-right) and all 4 edge cards (top, bottom, left, right)** — 6 cards total. The final marble locks the **center**, completing 1 column + 1 row + 1 diagonal at once → **7 cards captured** (the center is shared across all lines, counted once).

> 💡 **A theoretical 4-line completion is impossible:** The center belongs to 4 lines (1 column, 1 row, 2 diagonals), so 9-card simultaneous completion seems possible on paper. But reaching the prerequisite (holding all 8 surrounding cards) inevitably triggers another line first. So **the practical maximum is 3 lines / 7 cards**.

---

### 4. Capture and refill

1. Take the captured cards in hand
2. Return every marble on the captured cards (yours and your opponent's) to their respective owners
3. Refill empty slots: **while the Lv1 deck has cards, draw from Lv1**. Once Lv1 is empty, draw from Lv2; then Lv3 (treat decks as queues, not per-slot)

---

### 5. Disruption strategies

**(1) Physical disruption:** Knock the opponent's marble off the board. A marble off the board returns to the owner, and they lose their hold on that card.

**(2) Disruption via line completion:** Complete a line that crosses where your opponent is building — in step 4, every marble (including theirs) on captured cards returns home, breaking up their position.
- Only you complete the line → opponent's marbles on captured cards are returned → their hold disappears
- Both complete crossing lines → the shared card stays, and only the holds on it reset

A "sacrifice" strategy emerges: deliberately complete a low-value Lv1 line just to wreck the opponent's setup.

---

## Ending the game

### End condition

**The game ends when, after refilling, all 3 decks (Lv1, Lv2, Lv3) are empty and no further refills are possible.**

- The final round's checks, captures, and any possible refilling are processed as usual
- Cards left on the board at the end (up to 9) **don't count for scoring**
- Late game: once the decks are running thin, you must decide whether to capture low-level cards (speeding up the end) or stall to draw out more Lv3s

### Scoring

Score = total **fg pt (functional group points)** of captured cards. Highest score wins. Fg pt are printed in the top right of each card (see [GLOSSARY.en.md](./GLOSSARY.en.md)).

| Level | Score range | Role |
|-------|-------------|------|
| Lv1 | ~0 pt | Early-game territory, triggers board evolution |
| Lv2 | 0–4 pt | Mid-game point spread |
| Lv3 | 4–6 pt | Late-game high-value brawls |

---

## Strategy tips

- **Deliberately complete Lv1 lines to evolve the board:** Low scoring, but seeds Lv2/Lv3 into the grid
- **Read leftover marbles to predict opponent's targets:** You can't see this round's aim, but past leftover marbles give it away
- **"Doubles" and "triples" are the biggest comebacks:** Aim for intersections that complete multiple lines at once
- **Mind the shared-card risk:** Targeting the same card as your opponent costs both of you — that's where the mind games happen

---

## FAQ

**Q: Does landing on a card always let me hold it?**
A: Yes. Regardless of marble color, **touching any molecule card on the board (Lv1 / Lv2 / Lv3) at all** counts as holding it.

**Q: What if my marble straddles multiple cards?**
A: It counts as holding all touched cards (multi-holding). The card-assignment is not decided in advance — the player picks the most advantageous one at the moment of the check (quantum mechanics model). 1 marble = 1 card's worth of hold at most, so you can never lock 3 cards with just 2 marbles. Marbles touching no molecule card are off-board and returned to the owner.

**Q: Both players completed a line on the same round — what happens to the shared card?**
A: Take the non-shared captured cards first. The shared card stays on the board. **Every marble on the shared card returns to its owner** (the shared card resets to neutral). Next round, both players can fight over it again.

**Q: A card got bumped — what do I do?**
A: If a card moves before the marbles fully stop, slide it back into place before resolving. If it moves after resolution, leave it as is.

**Q: When do off-board marbles return?**
A: Once all marbles have come to a complete stop, return them to the owner.

---

# Advanced rules

## Variant list

Pick from the options below before starting. You can combine freely.

### 1. Flicking style

| Option | Description | Recommended for |
|--------|-------------|-----------------|
| **Simultaneous** | "3, 2, 1, GO!" — both flick at once | Standard (age 6+) |
| Alternating | Take turns, 1 flick each | Younger kids / strategists (age 6+) |
| Two-handed counter-flick | If knocked off, flick 2 next round | Experts |

### 2. Cards used

| Option | Description | Recommended for |
|--------|-------------|-----------------|
| **All levels** | Lv1–Lv3 (50 cards) | Standard |
| Lv1 + Lv2 only | No Lv3 | Shorter game |

### 3. Marble returns

| Option | Description | Recommended for |
|--------|-------------|-----------------|
| **Normal** | Opponent's marbles on captured cards return to owner | Standard |
| Hardcore | Opponent's marbles on captured cards are removed from the game | Adults |

### Recommended combinations

| Target | Flicking | Marble return | Cards |
|--------|----------|---------------|-------|
| **Younger kids (age 6+)** | Alternating | Normal | All levels |
| **Standard (age 6+)** | Simultaneous | Normal | All levels |
| **Experts** | Simultaneous + counter-flick | Hardcore | All levels |

---

## Alternating-flick variant

> Removes the simultaneous-flick tension, letting you focus on strategy and dexterity.

- Decide first player by RPS; alternate each round
- No "3, 2, 1, GO!" — take your time aiming on your turn
- Three-in-a-row check, capture, and refill are the same
- **Shared cards barely ever happen** (you can react to the opponent's flick)

Playable from age 6. Good for players who don't like hands colliding.

---

## Hardcore variant

> A tense adult variant: limited resources, sharper mind games.

Replace normal marble returns with **permanent removal**.

- Marbles of either player on a captured line → **removed from the game** (no return)
- You only have 10 marbles each. **The game ends as soon as one player runs out** (score at that point decides the winner)

Recommended for age 10+.

---

## Two-handed counter-flick variant

> A revenge rule: if knocked off the board, you flick 2 marbles next round.

**Trigger:** Your opponent's marble hit yours and sent it off the board
(your own mistake, or being knocked but staying on the board, doesn't trigger it)

**How it works:**
1. Keep the knocked-off marble in hand
2. Next round, flick that marble + 1 other from your hand **with both hands simultaneously**
3. The call is "**Issei-no-sei!**" (a Japanese chant similar to "one, two, three!")
4. Resolve both marbles' landings/holds as usual (different cards → 2 holds, same card → 1 hold but 2 marbles on it)
5. The three-in-a-row check is the same. **Two hold updates in one round** dramatically boost double/triple-line chances

| Situation | Handling |
|-----------|----------|
| Multiple marbles knocked off | Cap at 2; the rest return normally |
| Both players knocked each other off | "Mutual damage" — both return normally |
| Knocked off as collateral during a line capture | Return normally (no counter-flick) |
| Opponent also has counter-flick pending | Both flick 2 (4 marbles fly simultaneously) |

Your off-hand isn't accurate, so 2 marbles isn't always an advantage. When it works, give a "Well done!" salute.

---

## Handicap rules

For games with skill gaps. Agree on handicaps with all players before starting.

| Handicap | Effect |
|----------|--------|
| Distance | Place the stronger player's launcher 10–20 cm farther from the grid (or at an angle); the gap from the element cards grows |
| Off-hand | The stronger player flicks with their non-dominant hand (simplest and most effective) |
| Resource | In hardcore mode, reduce the stronger player's starting marbles from 10 → 7 |
| Blindfold | The stronger player closes their eyes while flicking |
| Accuracy penalty | When the stronger player hits their target, deduct 1 point or give 1 to the opponent |

**Suggested combinations:**

| Matchup | Recommended handicap |
|---------|---------------------|
| Adult vs. age 6–8 | Off-hand + distance |
| Adult vs. age 9–12 | Off-hand only |
| Veteran vs. beginner | Distance or resource |

---

[← Back to game list](../README.en.md#the-five-games)
