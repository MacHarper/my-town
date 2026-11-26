# My Town activity rules

The Vet Clinic is the standard (Mac, Nov 25, 2026). Every activity in every building (Hair Salon, Department Store, new buildings) works the same way, with the same timing, so brushing, washing or drying feels the same everywhere. These numbers are read from `vet-clinic/vet-clinic.html`; when you build or change an activity, copy them. Looks (colors, buttons, panels, arrows, pop-up messages) are in [style-guide.md](style-guide.md).

## 1. Screen layout
- **Task bar on top**, full width, edge to edge: logo badge, place name, a thin divider, then the step pills joined by dotted trails. Done steps are white with a green check. The current step is a sunny yellow pill (`#ffc94d`, darker edge `0 4px 0 #d9a531`), bigger than the rest, and tapping it starts it. Later steps are pale lavender (`#f3edf8`). A new current step pops in with `popSoft .45s`.
- **One guide line** says what to do next. In a room it sits at the bottom center (white-cream box, bold, 18 px corners). In a pop-up, the pop-up's own line replaces it, so words never show in two places. Tapping the wrong thing bounces the guide line (`nudge .45s`, scale 1.12) instead of showing a second message.
- **Activity pop-up** (the bath): title at the top with a round close button, then a row of step pills that starts at the left, then the stage, then the words line at the bottom.
- **The thing you care for sits in the middle of the stage. The tools sit outside it, in a tool area** (the bath's column on the left, or the panel beside the frame). A tool never starts on top of the pet, doll or hair.

## 2. Tools: drag them in to use them
- Only the tool for the current step can be picked up. It wears a glow ring, and the other tools have none.
- Glow ring: a rounded box or circle, fill `rgba(255,246,176,.18)`, stroke `#fff6b0`, 12 to 14 thick, 40-unit corners. It shows fully on the current tool, at 75% on hover, and goes away (0) while the tool is held.
- Tools are never faded (Mac, Nov 26, 2026). Tools already used simply have no highlight and can't be picked up.
- Press on the tool and drag it into the frame. It is carried over the pet (drawn on top) and it is the tool that does the work: wherever it passes, that part gets done. A mouse or finger alone never rubs.
- Let go anywhere and the tool goes straight back to its place in the tool area. The shower goes back on its hook.
- The shower sprays down and to the left of its head. Water lands 120 units below-left of the head (direction -0.6, 0.8) and reaches 70 units.
- A brush turns its bristles toward the pet while you move it.
- Close enough counts: a drop works within about 45 units of the target. Never stop the player partway through a drag.

## 3. How much rubbing finishes a step
- The thing being cared for is split into a **7 × 8 grid of cells** over its picture. A cell counts only where the picture is solid (alpha over 200). In the tub, only the top 75% counts, because the bottom is behind the tub.
- A hand tool (soap, towel, brush) finishes the cells within **46 units** of the pointer. That's about one cell width, since the pet is about 300 units wide. The shower reaches **70 units**.
- **A step is done at 70% of the cells** (`RUB_DONE = .7`) **and at least 3 seconds of rubbing** (Mac, Nov 26, 2026). It never stops you: you keep rubbing until you let go of the tool, and only then does the step count as done. Snipping nails needs every glowing spot. Each step starts over with fresh cells: rinsing and drying need 70% again, not just the soapy part.
- What you see while rubbing:
  - Soap leaves a little cluster of uneven white bubbles on each cell, and the stinky lines fade as you go.
  - Rinsing fades each cell's bubbles out over 0.4 s.
  - The towel leaves a green puff (`#bae5ca`) and the brush a yellow puff (`#fff6b0`). Each puff floats up and fades in 0.5 s.
- What happens when a step is done:
  - After rinsing, the pet shows its wet picture. After drying, it's back to normal.

## 4. Pacing between steps
- **No step moves on by itself.** When a step is done, the words go quiet, the next step's pill blinks (`blink 1.1s`: opacity 1 to .4 and back), and the next tool's ring lights up. The player keeps rubbing as long as they like, then picks up the next tool (or taps the blinking pill) to move on.
- **Interactions never force you to stop** (Mac, Nov 26, 2026). Every rubbing step, the last one too, lasts at least 3 seconds and keeps going while you hold the tool; it ends 0.2 s after you let go.
- **All done in the pop-up:** every pill is checked and the words say "[Name] is all clean.". The pet shows its happy picture and one burst of 8 yellow stars (`#ffd34d`) flies out once over 0.8 s. **1.6 s later** the pop-up closes.
- Moving the pet: 0.6 s onto the scale and 0.75 s into the tub. The bath pop-up opens 1.15 s after you send the pet in. A quick tap gets a reply in 0.25 to 0.6 s. Water and food tasks finish about 2.3 s after they start.
- After the last task: 0.7 to 0.9 s, then the Thanks card.

## 5. Thanks card and money
- **This is the standard for every payout in every game (Mac, Nov 26, 2026)**: the Vet Clinic thanks card. Copy it exactly, changing only the career, its color and the "help more" words.
- When the job is done, one card shows the career person from the career card (in their outfit, on a lavender `#f3edf8` panel). Above the thanks, the **career name** sits in a soft pill in the career's color ("Veterinarian"). It says **"Thanks for your help!"** in big green (`#5fae7a`) letters, with a short line about what you did.
- A spinning dollar bill shows "+$10". **1.4 s** after the card opens, **6 bills** fly from it into the money button in the toolbar, **0.11 s** apart, each taking **0.76 s**, with a rising tick sound as each one lands. Then the money is added.
- Only once all the money is in do the buttons fade in (0.35 s): **a help-more button** in the career's color ("Care for another pet") and **"Back to town"** (pink `#e0457b`).
- Shops (the Hair Salon) take money only at their Pay step. Trying things is free.

## 6. Messages and words
- Short words, emerging readers. Use the pet's or player's name ("Rub the soap on Bella.").
- Toast messages stay up at least 4.5 s (`tbReadMs`: 1.8 s plus 0.09 s per letter). Never a quick flash.
- "Not yet": two soft falling notes (330 then 262 Hz, sine) plus a toast that says what to do first.

## 7. Sounds
- Short Web Audio tones only.
- Good things play rising notes: give a toy C-E-G-C (523, 659, 784, 1047). Get paid uses the same rising notes, plus one high tick per bill.
- Rubbing, rinsing and drying make no sound, so the bath stays calm. Snipping nails clicks three times.
- Every sound goes through the toolbar's `tbBeep`, so the toolbar's sound setting works.

## 8. Glows in the room
- Room glows always follow each item's real outline (a traced glow picture, like the Vet Clinic sink), never a rectangle around the area (Mac, Nov 26, 2026).
- In a town room, only the things you can use right now get a glow. Things that aren't built yet (the Vet Clinic room's food, sink and tub) never light up; only the crates do. The current task's spot glows steadily. When it's time to pick a pet, a bobbing arrow points at the crates instead. While you hover one thing, only that thing lights up.
- Once a spot is done or in use, its glow goes away.

## 9. Opening a building (Mac, Nov 26, 2026)
Every building opens the same way, the Vet Clinic way:
1. The task bar is always there: full width across the top, with the building's logo, its name and the divider.
2. The room picture sits under it in the framed game-screen layout.
3. A pop-up meets you: the career card (career doll, name and a few words), or a welcome card with the building's logo when there is no career doll yet (the Hair Salon).
4. Closing it leaves a short line and a bobbing arrow pointing at the one thing to tap, which has an outline glow.
- No loading or "getting dressed up" screen between a room and its activity.
