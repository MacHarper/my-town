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

### Tools work the same everywhere (Mac, Nov 26, 2026; the Vet Clinic's cat and dog food are the model)
- **Labeled:** every tool wears a name tag above its place: a pill in the tool's own color with its name in white ("1 cup", "½ cup", "Tbsp", "tsp", "Whisk", "Oven mitt"). The recipe or list shows each amount in the same color as its tool. Things that are hard to tell apart (flour, sugar, milk) wear a label: white pill, dark edge, dark bold word, like the Vet Clinic's "Food".
- **Only what's needed:** only the tools this job uses are out; a tool for a later step comes out when that step starts. The same goes for anything else on screen: no card or reminder stays up once it isn't needed (the oven number shows only in the dial pop-up) (Mac, Nov 26).
- **Name tags side by side:** a row of tools has its name tags at one height, side by side, never overlapping or staggered. Spread the tools (and widen their area) so each tag sits centered above its own tool (Mac, Nov 26).
- **It stays in your hand:** a tool never snaps back while you hold it, after filling or after pouring. Only letting go sends it back to its place.
- **Filling:** a cup or spoon fills as soon as it touches what it's filling (a jar's lid opens and closes), while you keep holding it. The scoop sits inside the cup's opening.
- **Pouring:** when a full tool (cup, spoon, bowl) is held above what it pours into (never down on it or below its rim), it turns and pours by itself: it turns nearly upside down so its opening faces down over the target, dry food falls straight down as lots of small grains and milk or batter as one smooth stream, then it turns back upright, still in your hand. It never pours sideways or backwards, and never crosses over to the far side of what it pours into (a bowl pouring into a pan stays on its own side and tips toward it). What it pours into fills up as you go (a bowl's level rises). Batter pours as a thick stream and the pan fills where it lands: cup by cup, spot by spot, or one pool spreading across the pan, before it shows the full pan (Mac, Nov 26). The full method is in the game-design skill, Pouring.
- **Stirring:** pick up the whisk or spoon and it flips over, tip down; dip it in the bowl (the tip goes into the food, behind the bowl's front) and stir. Like the cat food: every bit of stirring counts (about 4 times round) and it finishes by itself. No line may show across the bowl where the front is drawn over the whisk. Once it is in the bowl it stays down in the food wherever you move (like the cat food spoon), so you stir round and round; it leans toward the side it is on.
- **Everything turns naturally:** pouring batter into a pan, food into a bowl, anything poured tips and pours; nothing just disappears into something else.
- **Pouring into a pan** happens in the counter close-up pop-up, like Mix; food set down in a room sits on the surface (its bottom on the counter or shelf top, never over the front edge).
- **The oven** opens when you bring the pan or the oven mitt to it and closes after. The pan slides onto the rack (seen from the side). When it's baked, the oven mitt comes out (not before): bring it to the oven, it takes hold of the pan, and you carry the pan out; let go and it snaps onto the counter (Mac, Nov 26).
- **Numbers to pick** (an oven temperature): once the pan is in, the oven dial opens big in a pop-up by itself with an up and a down arrow; tap the arrows until the number matches the recipe, then it closes by itself (Mac, Nov 26).

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
- **Steps match what you see** (Mac, Nov 26, 2026, Hair Salon wash): soap keeps adding bubbles while you rub (never stops after the cells are covered); rinsing is done when **no bubbles are left**; the towel keeps leaving puffs while you rub and the wet look fades as you dry, so drying is done when the hair looks dry (70%). Still at least 3 seconds and only after you let go; if you let go before 3 seconds with the step looking done, it finishes when the 3 seconds are up (you don't have to pick the tool up again).

## 4. Pacing between steps
- **No step moves on by itself.** When a step is done, the words go quiet, the next step's pill blinks (`blink 1.1s`: opacity 1 to .4 and back), and the next tool's ring lights up. The player keeps rubbing as long as they like, then picks up the next tool (or taps the blinking pill) to move on.
- **Interactions never force you to stop** (Mac, Nov 26, 2026). Every rubbing step, the last one too, lasts at least 3 seconds and keeps going while you hold the tool; it ends 0.2 s after you let go.
- **All done in the pop-up:** every pill is checked and the words say "[Name] is all clean.". The pet shows its happy picture and one burst of 8 yellow stars (`#ffd34d`) flies out once over 0.8 s. **1.6 s later** the pop-up closes.
- Moving the pet: 0.6 s onto the scale and 0.75 s into the tub. The bath pop-up opens 1.15 s after you send the pet in. A quick tap gets a reply in 0.25 to 0.6 s. Water and food tasks finish about 2.3 s after they start.
- After the last task: 0.7 to 0.9 s, then the Thanks card.

## 5. Thanks card and money
- **This is the standard for every payout in every game (Mac, Nov 26, 2026)**: the Vet Clinic thanks card. Copy it exactly, changing only the career, its color and the "help more" words.
- The card's bottom sits just above the tallest pet's head (`#allDone`: `align-items: safe flex-end; padding-bottom: 28.4%`), the same in every game (Mac, Nov 26).
- When the job is done, one card shows the career person from the career card (in their outfit, on a lavender `#f3edf8` panel). Above the thanks, the **career name** sits in a soft pill in the career's color ("Veterinarian"). It says **"Thanks for your help!"** in big green (`#5fae7a`) letters, with a short line about what you did.
- A spinning dollar bill shows "+$10". **1.4 s** after the card opens, **6 bills** fly from it into the money button in the toolbar, **0.11 s** apart, each taking **0.76 s**, with a rising tick sound as each one lands. Then the money is added.
- Only once all the money is in do the buttons fade in (0.35 s): **a help-more button** in the career's color ("Care for another pet") and **"Back to town"** (pink `#e0457b`).
- Shops (the Hair Salon) take money only at their Pay step. Trying things is free.

## 6. Messages and words
- **Only directions a new player needs** (Mac, Nov 26, 2026). Write a direction only when someone who has never played wouldn't know what to do ("Tape the box closed."). Skip anything the screen already makes clear (glowing food and a list next to a box) and never tell the player to do what the game does for them (the list checks itself).
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

## 10. Things in rooms look real (Mac, Nov 26, 2026)
Every one of these came from Mac. Run `python3 tools/rules_check.py <game file>` before publishing any game change; it catches the ones a script can see.
- **Glows** are only the outline glow (the salon chair's thin `#fff6b0` line made from the thing's own picture, `glowF`). Never draw a glow by hand: no yellow rings, rectangles or polygons over parts of a picture. A glow lines up exactly with the thing because it comes from the thing itself.
- **Nothing floats.** Things stand on a floor, counter or shelf with their bottom on it; a box on the floor has its shadow right under its bottom corners.
- **Real sizes.** Things next to each other keep their real sizes compared to each other (an apple is small, a cereal box is tall), and each wears a small label near it (white pill, dark edge).
- **Into a container means inside it.** Food put in a box goes down inside, behind the box's front, with only its top showing. It never sits on top of the box.
- **No taps that do nothing.** When a step's goal is reached it finishes by itself (the box shuts by itself when everything is in). Never ask for taps that just move a picture along.
- **Farther away is smaller.** A thing carried away from you (the box to the truck) gets smaller as it goes, and ends sitting where it belongs at the right size (inside the truck, on its floor).
- **Only the thing moves.** Never move the whole screen or a copied piece of the room picture. Don't add moves that don't fit the picture (closing a truck whose doors are open in the picture).
- **Plain words for what you do:** "Tape the box closed", "Put frosting on the cake". Never "rub" unless you really rub (washing, drying).
- **Filling:** a bowl's food reaches close to its edge; the scoop sits exactly in the cup's opening.
- **Heat and light stay inside their shape** (the oven's glow stays in the window glass).
- **Pieces on a plate** (cupcakes, muffins) stand side by side on the plate's flat top, in rows from the back, never stacked like a tower. A whole cake shows as the whole cake as soon as it is lifted out of its pan (Mac, Nov 26).
- **Baked food** comes out the shape of its pan (a round pan makes a round cake, not a muffin top); the plate is a little bigger than the food, and both fit the counter. Finished food stays on the counter (it is not moved onto shelves).
- **Toppings show up:** frosting is a color you can see on the food, piped like real icing, squirting from the bag's tip. A bowl of toppings tips over as you use it and empties as they go on.
