# NFRP-Anim: Animation versus Description QA

Prepared for CassieGiang and Claude Code · 22 October 2026

## Scope and result

The requirement is visual fidelity: does the animation communicate the action, form and material described in the catalogue? This review screened all 162 MP4 entries and shortlisted eight visual mismatches for correction or reproduction. Other entries have partial matches, readability concerns, or claims that the recordings do not demonstrate. No source changes were made.

Source: [NFRP-Anim](https://github.com/CassieGiang/NFRP-Anim), using `tools/animations.json` as the description contract and the corresponding `clans-and-styles/*.mp4` recordings as evidence. Definition IDs below are lookup keys, not proven implementation causes.

Repository tree snapshot identifier: `6d3a6ba1a7cc1dc77796e4704059ca3320f2263d`. Catalogue links point to the published site and may change after this review; preserve before/after recordings when implementing fixes.

## Method and confidence

- All 162 clips were downloaded and successfully decoded. Each was screened using six timed frames at approximately 0.5, 1.25, 2, 3, 4.5 and 6.5 seconds.
- Seventeen suspicious entries received denser follow-up at approximately six frames per second: 014, 025, 035, 051, 059, 071, 088, 094, 098, 099, 106, 114, 122, 127, 130, 158 and 160.
- The early flight windows of 035 and 088 were also checked at 24 frames per second; 059 was checked again through approximately 8.4 seconds.
- This is a first-pass visual audit using extracted frames, not uninterrupted playback of every clip or an in-game regression run. Short actions may fall between samples. Replay the linked clips at normal speed before finalizing implementation work.
- A visual mismatch means the reviewed recording does not clearly depict its defining promise. It does not establish whether the cause is renderer code, assets, a stale recording, or scene setup.
- Damage, armour bypass, accuracy, durations longer than the recording, permissions, equipment prerequisites and actual status mechanics remain unverified.

## Priority corrections

Priority P1 here means a defining visual promise is missing or contradicted in the recording, not a crash or gameplay severity rating. Times are approximate seconds from the start.

### V01 · P1 · Sōao Hōkiboshi (Twin Blue Comets)

- **Definition:** `NF_AnbuU_TwinComets`
- **Clip:** [130-s-ao-h-kiboshi-twin-blue-comets.mp4](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/130-s-ao-h-kiboshi-twin-blue-comets.mp4) · inspect 2.0–3.1 s
- **Expected visual:** Two simultaneous blue fire comets.
- **Observed:** Two brown/olive rod-like shapes dominate the travel phase.
- **Acceptance:** Render two clearly separated blue flame heads with blue/cyan trails. Their direction and wide path must read without the aim overlay.

### V02 · P1 · Nikudan Sensha: Human Bullet Tank

- **Definition:** `NF_HumanBulletTank`
- **Clip:** [071-nikudan-sensha-human-bullet-tank.mp4](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/071-nikudan-sensha-human-bullet-tank.mp4) · inspect 1.3–3.0 s
- **Expected visual:** Caster becomes a giant ball and rolls through a line.
- **Observed:** Caster remains recognizably upright while dashing with colored afterimages.
- **Acceptance:** Show a distinct ball silhouette larger than the ordinary pawn, sustained rotation during travel and impacts along the path. Test the spiked variant separately.

### V03 · P1 · Hitoshirezu Mushiryūdan: Hidden Bug Dragon

- **Definition:** `NF_BugDragon`
- **Clip:** [035-hitoshirezu-mushiry-dan-hidden-bug-dragon.mp4](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/035-hitoshirezu-mushiry-dan-hidden-bug-dragon.mp4) · inspect 0.7–2.5 s
- **Expected visual:** An insect mass forms a dragon and slams into the area.
- **Observed:** Charge swirl, distorted/ballooned target and dark specks do not form a readable dragon.
- **Acceptance:** Give the travelling swarm a recognizable dragon head, body and tail; break it into insects on impact. Keep the silhouette readable at ordinary zoom.

### V04 · P1 · Kanzen Yōkai (Complete Meltdown)

- **Definition:** `NF_Anbu_Meltdown`
- **Clip:** [114-kanzen-y-kai-complete-meltdown.mp4](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/114-kanzen-y-kai-complete-meltdown.mp4) · inspect 1.8–4.3 s
- **Expected visual:** Fast close strikes and a neck jab; victim sees five ANBU.
- **Observed:** Remote mental tether and purple target marker dominate.
- **Acceptance:** Stage close contact and jab, then five distinct ANBU silhouettes around the victim. Show flight in a separate unobstructed shot. An illusion may be stylized, but its five figures should be countable.

### V05 · P1 · Doken Tsuiseki (Earthen Tracking Hounds)

- **Definition:** `NF_Anbu_Hounds`
- **Clip:** [094-doken-tsuiseki-earthen-tracking-hounds.mp4](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/094-doken-tsuiseki-earthen-tracking-hounds.mp4) · inspect 1.8–4.3 s
- **Expected visual:** Tracking hounds erupt from the ground and pin the victim.
- **Observed:** Orange jagged glyphs form a tether; recognizable hounds and ground emergence are unclear.
- **Acceptance:** Animate canine silhouettes emerging at the victim, then a sustained holding pose. Retain a separate mark cue after the hold ends.

### V06 · P1 · Sōheki (Twin Barrier)

- **Definition:** `NF_Anbu_TwinBarrier`
- **Clip:** [106-s-heki-twin-barrier.mp4](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/106-s-heki-twin-barrier.mp4) · inspect 2.5–6.3 s
- **Expected visual:** Two linked barriers protect nearby allies.
- **Observed:** A single oversized blue swirling bubble/disc dominates.
- **Acceptance:** Make two stable barrier forms and their connection distinguishable. Stage allies inside the affected area; keep pawns visible through the effect.

### V07 · P1 · Seihaku Rai (Pale Bolt)

- **Definition:** `NF_Anbu_PaleBolt`
- **Clip:** [099-seihaku-rai-pale-bolt.mp4](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/099-seihaku-rai-pale-bolt.mp4) · inspect 2.1–3.5 s
- **Expected visual:** One rapid bolt originates at the fingertip.
- **Observed:** A dominant vertical sky strike precedes or overlaps the caster-target electrical line.
- **Acceptance:** Make the first and strongest bolt clearly start at the caster's hand and travel to the victim. Reduce the vertical sky-strike cue. Armour bypass needs a separate mechanical test.

### V08 · P1 · Shugohakke: Protection of the White God

- **Definition:** `NF_WhiteGod`
- **Clip:** [025-shugohakke-protection-of-the-white-god.mp4](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/025-shugohakke-protection-of-the-white-god.mp4) · inspect 3.1–6.3 s
- **Expected visual:** A towering chakra guardian protects the caster and strikes nearby.
- **Observed:** Pale glyphs and arcs suggest protection but no clear towering humanoid avatar.
- **Acceptance:** Give the guardian a head, torso and arms visibly larger than the pawn. Stage a nearby attacker so the avatar's strike is distinguishable from passive orbiting particles.

## Readability and staging follow-ups

| Entry | What is visible | Recommended follow-up |
| --- | --- | --- |
| 059 Seedling Ferns | Small ivory spike clusters appear late, alongside prominent cyan starbursts. | Increase spike density/height and bone identity. Do not report all spikes as absent. The five-second stabbing duration needs a complete timing capture. |
| 098 Lightning Cage | Very faint pale-blue posts behind the STUN marker. | Improve contrast, height and enclosure; make six posts countable. |
| 127 Cage of the Forgotten | Blue cage lattice and thin red diamond-like outlines. | Strengthen the red diamond seal while preserving target visibility. |
| 051 Dance of the Clematis | Large bone-colored spikes around the caster at about 3.7 s. | Make the spine extraction and held weapon distinct from ground spikes. |
| 088 Water Shark Bullet | Water charge and impact are visible; shark shape is hard to resolve. | Replay full-speed flight; use a readable dorsal fin, jaw and tail if the silhouette still fails. |
| 122 Curse Doll | Remote purple target effect. | Show doll preparation/use if intended to be visible; a missing doll in this shot alone is not proof of a bug. |
| 158 Crown Splitter / 160 Tornado Drop | Close arcs, rotation and target collapse. | Separate anticipation, leap/lift and descent/impact. Avoid treating ambiguous sampling as proof that movement is absent. |

Several demonstrations need different fixtures: 040/044/045 need recognizable bonded dogs; 048 needs a clearly dead dog and a visible revived state; 132/133 need obvious corpses before and after; 081/086 need enemy teams that visibly attack their own allies; 135 needs hidden enemies outside normal detection; 161 needs an armed target and visible weapon loss. These are recording gaps until reproduced with proper fixtures.

## Positive visual references

- 017 Empty Palm: forward air rings and displacement communicate the action.
- 019 Great Divination Whirl: circular wind and outward displacement communicate the spin defense.
- 055 Bone Vengeful Grasp: skeletal hands establish the intended material and action.
- 075 Butterfly Mode: blue butterfly wings establish the transformation.
- 097 Thunder Cannon: a forward lightning beam establishes origin, direction and attack identity.

## Implementation handoff for Claude Code

1. Reproduce V01–V08 at normal game speed and the same catalogue rank. Check that the recording matches the current mod revision before editing.
2. Locate each effect through its definition ID in NFRP World. Inspect the ability-to-renderer mapping, selected texture/material, color, scale, lifetime, draw order and origin. These are diagnostic checks, not confirmed root causes.
3. Correct the visual implementation to match the description. Do not silently rewrite descriptions to fit a generic existing effect unless Cassie approves that design change.
4. Record the corrected clip with the same camera, zoom, caster/target spacing and lighting. Preserve a short before/after reference and record mod revision, RimWorld version, rank and required equipment.
5. Verify at normal speed that a viewer can identify the defining shape/action without reading the title; use slowed replay only for diagnosis. Check ordinary and zoomed-out views, target visibility, allies and multiple targets where relevant.
6. Run neighboring abilities that share the changed renderer or material. Include save/load with sustained effects active where applicable, cancellation, interrupted casts and repeated use. Mechanical assertions require in-game state/log evidence.
7. Refresh the catalogue MP4/poster and record what was changed. A documentation-only media repository cannot prove a gameplay fix by itself.

## Complete first-pass matrix

Statuses: **VISUAL MATCH** = defining cue visible, not a mechanical certification; **PARTIAL** = some cues fit but clarity or coverage is incomplete; **VISUAL MISMATCH** = shortlisted above; **CANDIDATE MISMATCH** = overview concern requiring denser replay; **NOT DEMONSTRATED** = fixture/shot does not establish the claim; **UNVERIFIABLE** = claim requires state, audio or controlled comparisons.

| # | Technique / definition | Status | Observation |
| --- | --- | --- | --- |
| 001 | [Katon: Great Fireball](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/001-katon-great-fireball.mp4) · `NF_GreatFireball` | PARTIAL | Fireball/fiery impact is visible; projectile shape needs dense review; rank scaling not shown. |
| 002 | [Katon: Great Fire Annihilation](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/002-katon-great-fire-annihilation.mp4) · `NF_FireAnnihilation` | PARTIAL | Wide orange aim wedge and flames on targets; continuous sea of fire not clearly depicted. |
| 003 | [Battle Ready (Sharingan)](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/003-battle-ready-sharingan.mp4) · `NF_BattleReady` | UNVERIFIABLE | Sharingan emblem and buff cue; no controlled accuracy/dodge demonstration. |
| 004 | [Mirror Heaven and Earth Change](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/004-mirror-heaven-and-earth-change.mp4) · `NF_Mirror` | UNVERIFIABLE | White protective cue, melee happening; reflection cannot be established visually. |
| 005 | [Painful Stare](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/005-painful-stare.mp4) · `NF_PainfulStare` | PARTIAL | Caster-target eye/illusion tether visible; pain itself not measurable. |
| 006 | [Shackling Stakes](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/006-shackling-stakes.mp4) · `NF_ShacklingStakes` | CANDIDATE MISMATCH | Dark bead tether and red orb/ring on target; no obvious stakes pinning victim. |
| 007 | [Burning Stare](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/007-burning-stare.mp4) · `NF_BurningStare` | PARTIAL | Orange flame-like target cue; internal burn duration not demonstrated. |
| 008 | [Fatiguing Stare](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/008-fatiguing-stare.mp4) · `NF_FatiguingStare` | PARTIAL | Area markers and three status cues; actual slowing not shown by stationary subjects. |
| 009 | [Demoralizing Stare](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/009-demoralizing-stare.mp4) · `NF_DemoralizingStare` | PARTIAL | Area illusion cues, purple impact; aim/mind debuff unverified. |
| 010 | [Wilting Stare](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/010-wilting-stare.mp4) · `NF_WiltingStare` | PARTIAL | Single target tether and orange target cue; debuff duration unverified. |
| 011 | [Majestic Stare](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/011-majestic-stare.mp4) · `NF_MajesticStare` | PARTIAL | Large area illusion burst; wide-area targeting visible, awe immobilization not demonstrated. |
| 012 | [Gazing Genjutsu](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/012-gazing-genjutsu.mp4) · `NF_GazingGenjutsu` | PARTIAL | Single target red illusion and later collapse plausible; duration unverified. |
| 013 | [Telescopic Eye](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/013-telescopic-eye.mp4) · `NF_TelescopicEye` | UNVERIFIABLE | White eye/buff cue; no shooting comparison. |
| 014 | [Harichakra: Chakra Needles](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/014-harichakra-chakra-needles.mp4) · `NF_ChakraNeedle` | PARTIAL | Target bursts are visible; solid-chakra needles remain hard to read. Projectile identity needs normal-speed replay. |
| 015 | [Hakke: Chakra Transfer Palm](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/015-hakke-chakra-transfer-palm.mp4) · `NF_ChakraTransfer` | PARTIAL | Green healing cross on adjacent ally; no visible palm/channel transfer. |
| 016 | [Chakra no Bodi: Body of Chakra](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/016-chakra-no-bodi-body-of-chakra.mp4) · `NF_BodyOfChakra` | PARTIAL | Blue body cue during melee; full-body coating weak. |
| 017 | [Hakke Kūshō: Eight Trigrams Empty Palm](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/017-hakke-k-sh-eight-trigrams-empty-palm.mp4) · `NF_EmptyPalm` | VISUAL MATCH | Air stream/rings and targets displaced along line. |
| 018 | [Jūken Tenketsu: Gentle Fist Chakra Points](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/018-j-ken-tenketsu-gentle-fist-chakra-points.mp4) · `NF_Tenketsu` | PARTIAL | Close hit and chakra burst; sealing points implied rather than shown. |
| 019 | [Hakkeshō: Great Divination Whirl](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/019-hakkesh-great-divination-whirl.mp4) · `NF_GreatWhirl` | VISUAL MATCH | Circular wind vortex and enemies thrown away. |
| 020 | [Hakke Hasangeki: Eight Trigrams Mountain Crusher](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/020-hakke-hasangeki-eight-trigrams-mountain-crusher.mp4) · `NF_MountainCrusher` | PARTIAL | Wide aiming cone and white impact effects; palm-blast shape weak. |
| 021 | [Hakke: One Hundred Twenty-Eight Palms](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/021-hakke-one-hundred-twenty-eight-palms.mp4) · `NF_128Palms` | PARTIAL | Repeated close combat/blue rings; exact palms chain needs dense review. |
| 022 | [Shugohakke: Protection of the Sixty-Four Palms](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/022-shugohakke-protection-of-the-sixty-four-palms.mp4) · `NF_ProtectionPalms` | CANDIDATE MISMATCH | Transient loose white shapes; persistent blade sphere not clear. |
| 023 | [Shinkan: Silence Gates](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/023-shinkan-silence-gates.mp4) · `NF_Silence` | PARTIAL | Target chakra markers and sustained affected state; ordered gate closing not legible. |
| 024 | [Hakke Hazan Hōgeki: Crumbling Mountain Bombardment](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/024-hakke-hazan-h-geki-crumbling-mountain-bombardment.mp4) · `NF_CrumblingMountain` | PARTIAL | Area and repeated white-blue impacts; palm-shaped bombardment not clear. |
| 025 | [Shugohakke: Protection of the White God](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/025-shugohakke-protection-of-the-white-god.mp4) · `NF_WhiteGod` | VISUAL MISMATCH | Pale orbiting glyphs and arcs communicate protection, but no clearly recognizable towering guardian avatar is visible at 3.1–6.3 s. |
| 026 | [Mushi Ryūki: Bug Projection](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/026-mushi-ry-ki-bug-projection.mp4) · `NF_BugProjection` | PARTIAL | Dark insect-like stream/target particles; generic blue windup; drain unverified. |
| 027 | [Mushitate: Bug Shield](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/027-mushitate-bug-shield.mp4) · `NF_BugShield` | PARTIAL | Bug-colored dark shell around caster; projectile interception not shown. |
| 028 | [Bug Grappling](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/028-bug-grappling.mp4) · `NF_BugGrapple` | PARTIAL | Dark stream to victim and status marker; limbs/grappling weak. |
| 029 | [Poison Reduction](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/029-poison-reduction.mp4) · `NF_Antitoxins` | UNVERIFIABLE | Green buff cue; no poison/disease comparison. |
| 030 | [Yoroi no Mushi: Armour of Bugs](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/030-yoroi-no-mushi-armour-of-bugs.mp4) · `NF_BugArmor` | CANDIDATE MISMATCH | Ordinary body and buff markers during melee; bug-covered armour not apparent. |
| 031 | [Genwaku Mushiheki: Blinding Bug Burst](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/031-genwaku-mushiheki-blinding-bug-burst.mp4) · `NF_BlindingBurst` | PARTIAL | Area application and insect-colored target cues; eyes not legibly covered. |
| 032 | [Mushikabe: Bug Wall](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/032-mushikabe-bug-wall.mp4) · `NF_BugWall` | PARTIAL | Dark scalloped boundary and insect-like particles; wall reads as ring more than dome. |
| 033 | [Mushi Ame: Bug Rain](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/033-mushi-ame-bug-rain.mp4) · `NF_BugRain` | CANDIDATE MISMATCH | Blue-white snowflake-like impacts and red target effects; falling insects not clear. |
| 034 | [Mushi Kōchisho: Bug Prison](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/034-mushi-k-chisho-bug-prison.mp4) · `NF_BugPrison` | CANDIDATE MISMATCH | Small red/orange target cue; enclosing ball of insects not clear. |
| 035 | [Hitoshirezu Mushiryūdan: Hidden Bug Dragon](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/035-hitoshirezu-mushiry-dan-hidden-bug-dragon.mp4) · `NF_BugDragon` | VISUAL MISMATCH | Early cast frames and impact show a caster swirl, target balloon/distortion and dark specks; no readable dragon-shaped insect mass. |
| 036 | [Mushi Kiri: Bug Mist](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/036-mushi-kiri-bug-mist.mp4) · `NF_BugMist` | CANDIDATE MISMATCH | Caster buff/melee with very little visible insect haze. |
| 037 | [Mushi Kachū: Bug Vortex](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/037-mushi-kach-bug-vortex.mp4) · `NF_BugVortex` | CANDIDATE MISMATCH | Small target bursts; no sustained spinning insect column. |
| 038 | [Yūen Mushinami: Grand Bug Wave](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/038-y-en-mushinami-grand-bug-wave.mp4) · `NF_GrandBugWave` | CANDIDATE MISMATCH | Green aiming wedge then isolated target sparks; no broad insect wave visible. |
| 039 | [Mishu Arano: Bug Wasteland](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/039-mishu-arano-bug-wasteland.mp4) · `NF_BugWasteland` | CANDIDATE MISMATCH | Green range ring and target flashes; ground does not read as seething insect field. |
| 040 | [Canine Bond](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/040-canine-bond.mp4) · `NF_CanineBond` | NOT DEMONSTRATED | Humanoid-looking target with generic bond cue; canine bond not clearly staged. |
| 041 | [Keen Senses](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/041-keen-senses.mp4) · `NF_KeenSenses` | UNVERIFIABLE | Gold buff cue; sensory changes not observable. |
| 042 | [Four Legs Technique](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/042-four-legs-technique.mp4) · `NF_FourLegs` | CANDIDATE MISMATCH | Normal upright pawn during buff/melee; four-legged beast stance not apparent. |
| 043 | [Piercing Fang](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/043-piercing-fang.mp4) · `NF_PiercingFang` | PARTIAL | Trail/dash along line; spinning drill and bonded dog not clear. |
| 044 | [Pack Tactics](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/044-pack-tactics.mp4) · `NF_PackTactics` | NOT DEMONSTRATED | Buff cue on caster; no visible dog pack to show propagation. |
| 045 | [Hound of the Baskervilles](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/045-hound-of-the-baskervilles.mp4) · `NF_HoundRage` | NOT DEMONSTRATED | Caster pulse; no bonded dogs visibly enraging. |
| 046 | [Fearful Howl](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/046-fearful-howl.mp4) · `NF_FearfulHowl` | PARTIAL | Radial howl area and affected enemies; flinch/debuff not established. |
| 047 | [Paralysis Bite](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/047-paralysis-bite.mp4) · `NF_ParalysisBite` | PARTIAL | Close strike and blue effect; distinct bite motion not legible. |
| 048 | [Veterinarian](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/048-veterinarian.mp4) · `NF_Veterinarian` | NOT DEMONSTRATED | Fallen humanoid-looking target remains down; no clear dead-dog resurrection. |
| 049 | [Bone Armour](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/049-bone-armour.mp4) · `NF_BoneArmor` | UNVERIFIABLE | Subdermal armour buff cue; four stage strength not observable. |
| 050 | [Dance of the Larch](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/050-dance-of-the-larch.mp4) · `NF_DanceLarch` | PARTIAL | White spike silhouette appears during melee; persistent bone-spur coat weak. |
| 051 | [Dance of the Clematis](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/051-dance-of-the-clematis.mp4) · `NF_DanceClematis` | PARTIAL | Large bone-colored spikes appear around the caster at about 3.7 s; the huge weapon being drawn from the spine and held is not clearly communicated. |
| 052 | [Deathless](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/052-deathless.mp4) · `NF_Deathless` | UNVERIFIABLE | Red healing/buff cues; wound closure/chakra drain not established. |
| 053 | [Ten Finger Bullets](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/053-ten-finger-bullets.mp4) · `NF_FingerBullets` | PARTIAL | Bone-colored impact; five distinct fingertip bullets require dense review. |
| 054 | [Bone Shards](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/054-bone-shards.mp4) · `NF_BoneShards` | PARTIAL | Cone and white bursts; actual shard spray not obvious in sparse frames. |
| 055 | [Bone's Vengeful Grasp](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/055-bone-s-vengeful-grasp.mp4) · `NF_VengefulGrasp` | VISUAL MATCH | Large skeletal hands visibly erupt over target area. |
| 056 | [Stillbone](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/056-stillbone.mp4) · `NF_Stillbone` | PARTIAL | Target held with bone-colored tether; internal bone locking is abstract. |
| 057 | [Bone Cage](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/057-bone-cage.mp4) · `NF_BoneCage` | PARTIAL | Bone-colored cages/bars around multiple targets; enclosure silhouette needs closer look. |
| 058 | [Osteophage](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/058-osteophage.mp4) · `NF_Osteophage` | PARTIAL | Bone-colored impact and target falls; internal shattering not visible. |
| 059 | [Dance of the Seedling Ferns](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/059-dance-of-the-seedling-ferns.mp4) · `NF_SeedlingFerns` | PARTIAL | Late frames at 6.4–8.4 s do contain small ivory spike clusters around the area. Sparse clusters and prominent cyan starbursts weaken the impression of a bone-spike forest. Do not report spikes as absent. |
| 060 | [Kagemane no Jutsu: Shadow Imitation](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/060-kagemane-no-jutsu-shadow-imitation.mp4) · `NF_ShadowImitation` | PARTIAL | Black beaded tether connects caster to victim; reads as floating beads rather than ground shadow. |
| 061 | [Shadow Strike](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/061-shadow-strike.mp4) · `NF_ShadowStrike` | CANDIDATE MISMATCH | Same black bead tether/target orb as other shadow skills; no shadow punching shadow. |
| 062 | [Kage Kubi Shibari: Shadow Neck Bind](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/062-kage-kubi-shibari-shadow-neck-bind.mp4) · `NF_ShadowNeckBind` | PARTIAL | Shadow tether and target held; neck choke silhouette not clear. |
| 063 | [Shadow Entrapment](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/063-shadow-entrapment.mp4) · `NF_ShadowEntrapment` | PARTIAL | Dark target wrap and tether; target enclosure broadly fits. |
| 064 | [Shadow Blast](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/064-shadow-blast.mp4) · `NF_ShadowBlast` | PARTIAL | Projectile too brief for overview; dense review needed to check kunai/spear silhouette. |
| 065 | [Shadow Envelop](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/065-shadow-envelop.mp4) · `NF_ShadowEnvelop` | PARTIAL | Dark body cue under melee; shadow wrap subtle. |
| 066 | [Kage Nui: Shadow Sewing](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/066-kage-nui-shadow-sewing.mp4) · `NF_ShadowSewing` | PARTIAL | Branching black tethers hit several targets; shadow threads broadly readable. |
| 067 | [Shadow Dome](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/067-shadow-dome.mp4) · `NF_ShadowDome` | PARTIAL | Large dark spiral disc covers area; shadow barrier evident, dome height weak. |
| 068 | [Shadow Endgame](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/068-shadow-endgame.mp4) · `NF_ShadowEndgame` | PARTIAL | Wide area and black multi-target tethers; razor shadow forms weak. |
| 069 | [Bubun Baika: Partial Expansion](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/069-bubun-baika-partial-expansion.mp4) · `NF_PartialExpansion` | PARTIAL | Close attack includes extended tan/orange limb-like shape; giant arm needs dense review. |
| 070 | [Baika no Jutsu: Expansion](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/070-baika-no-jutsu-expansion.mp4) · `NF_Expansion` | PARTIAL | Body appears enlarged after activation; rank-to-rank scaling not shown. |
| 071 | [Nikudan Sensha: Human Bullet Tank](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/071-nikudan-sensha-human-bullet-tank.mp4) · `NF_HumanBulletTank` | VISUAL MISMATCH | Upright caster dashes toward target with colored afterimages; no readable transformation into a giant rolling ball in dense 0.5–4.3 s review. |
| 072 | [Calorie Control](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/072-calorie-control.mp4) · `NF_CalorieControl` | UNVERIFIABLE | Gold body cue; calorie conversion and toughness not visually measurable. |
| 073 | [Ironguts](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/073-ironguts.mp4) · `NF_Ironguts` | UNVERIFIABLE | Neutral buff glyph; toxin/disease resistance not observable. |
| 074 | [Chōbaika: Mega Palm Thrust](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/074-ch-baika-mega-palm-thrust.mp4) · `NF_MegaPalm` | PARTIAL | Large blue fist/hand effect over area; two expanding hands slamming down not clearly staged. |
| 075 | [Chō Mode: Butterfly Mode](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/075-ch-mode-butterfly-mode.mp4) · `NF_ButterflyMode` | VISUAL MATCH | Bright blue butterfly-like wings appear on caster during melee. |
| 076 | [Impact Wave](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/076-impact-wave.mp4) · `NF_ImpactWave` | PARTIAL | Wide shockwave/cone and targets displaced; giant fist itself not clear. |
| 077 | [Mind Pulse](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/077-mind-pulse.mp4) · `NF_MindPulse` | PARTIAL | Mental pulse over area and target cues; daze mechanics unverified. |
| 078 | [Confusion](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/078-confusion.mp4) · `NF_Confusion` | PARTIAL | Mind tether and purple target status; wandering is not clearly demonstrated. |
| 079 | [Mind Imprisonment](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/079-mind-imprisonment.mp4) · `NF_MindImprisonment` | PARTIAL | Target status/tether and stationary pawn; mental prison abstract. |
| 080 | [Broken Mind](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/080-broken-mind.mp4) · `NF_BrokenMind` | PARTIAL | Mental tether and purple head cue; distinct shattering not apparent. |
| 081 | [Shinranshin no Jutsu: Mind Body Disturbance](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/081-shinranshin-no-jutsu-mind-body-disturbance.mp4) · `NF_MindDisturbance` | NOT DEMONSTRATED | Mind tether reaches target; target attacking its allies is not demonstrated. |
| 082 | [Shintenshin no Jutsu: Mind Body Switch](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/082-shintenshin-no-jutsu-mind-body-switch.mp4) · `NF_MindTransfer` | PARTIAL | Transfer tether and possession cue; caster limp-body state and player control need closer check. |
| 083 | [Kontanribon no Jutsu: Mind Ribbon](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/083-kontanribon-no-jutsu-mind-ribbon.mp4) · `NF_MindRibbon` | PARTIAL | Multiple links reach targets; streams of rings/beads read less like ribbons. |
| 084 | [Omoitobikomi no Jutsu: Mind Dive](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/084-omoitobikomi-no-jutsu-mind-dive.mp4) · `NF_MindDive` | PARTIAL | Mental tether and target effect; mind damage not visually demonstrable. |
| 085 | [Omoi Dōran Odori: Mind Disturbance Dance](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/085-omoi-d-ran-odori-mind-disturbance-dance.mp4) · `NF_DisturbanceDance` | PARTIAL | Area mental burst/status on targets; wandering not shown. |
| 086 | [Dancing Minds](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/086-dancing-minds.mp4) · `NF_DancingMinds` | NOT DEMONSTRATED | Wide multi-target mind links; enemies fighting each other not clear. |
| 087 | [Samehada: Shark Skin](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/087-samehada-shark-skin.mp4) · `NF_SharkSkin` | UNVERIFIABLE | Blue body aura; shark hide texture/rasp not strongly distinguishable. |
| 088 | [Suikōdan: Water Shark Bullet](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/088-suik-dan-water-shark-bullet.mp4) · `NF_WaterShark` | PARTIAL | Early flight-window frames show caster charge and watery target burst; shark silhouette is not readable in the reviewed frames. Needs full-speed replay before calling it absent. |
| 089 | [Suiton: Bakurai: Depth Charge](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/089-suiton-bakurai-depth-charge.mp4) · `NF_DepthCharge` | PARTIAL | Blue burst over area; charge projectile and watery detonation not very legible. |
| 090 | [Samekabe: Shark Wall](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/090-samekabe-shark-wall.mp4) · `NF_SharkWall` | PARTIAL | Blue circular wall clearly surrounds spot; shark silhouettes need closer view. |
| 091 | [Chi Kaori: Blood Scent](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/091-chi-kaori-blood-scent.mp4) · `NF_BloodScent` | PARTIAL | Close watery bite/target effect; tracking a previously wounded target not demonstrated. |
| 092 | [Suiton: Satsugai Naiō: Killing Depths](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/092-suiton-satsugai-nai-killing-depths.mp4) · `NF_KillingDepths` | PARTIAL | Blue area fill and repeated target effects; deep water texture weak. |
| 093 | [Same Kyōran: Shark Frenzy](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/093-same-ky-ran-shark-frenzy.mp4) · `NF_SharkFrenzy` | UNVERIFIABLE | Red aura and melee; strength/speed/bloodthirst not measurable. |
| 094 | [Doken Tsuiseki (Earthen Tracking Hounds)](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/094-doken-tsuiseki-earthen-tracking-hounds.mp4) · `NF_Anbu_Hounds` | VISUAL MISMATCH | Orange jagged glyph tether links caster and target; recognizable hounds emerging from the ground and holding the victim are not visible. |
| 095 | [Chiato (Blood Trail)](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/095-chiato-blood-trail.mp4) · `NF_Anbu_BloodTrail` | PARTIAL | Red target marker is suitable blood-trail cue; actual tracking unverified. |
| 096 | [Kowadori (Voice Capture)](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/096-kowadori-voice-capture.mp4) · `NF_Anbu_VoiceCapture` | UNVERIFIABLE | Target silence/status cue; speech suppression cannot be checked in silent recording. |
| 097 | [Raihō (Thunder Cannon)](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/097-raih-thunder-cannon.mp4) · `NF_Anbu_ThunderCannon` | VISUAL MATCH | Straight blue lightning beam projects forward and hits targets in its line. |
| 098 | [Rairō (Lightning Cage)](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/098-rair-lightning-cage.mp4) · `NF_Anbu_LightningCage` | PARTIAL | Faint pale-blue cage posts are visible on close inspection behind the STUN marker. Improve contrast and enclosure readability; six pillars cannot be confidently counted. Do not report cage as absent. |
| 099 | [Seihaku Rai (Pale Bolt)](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/099-seihaku-rai-pale-bolt.mp4) · `NF_Anbu_PaleBolt` | VISUAL MISMATCH | Dominant flash is a vertical sky-to-target lightning strike around 2.2 s; a caster-target electrical line follows. This obscures the specified fingertip origin. |
| 100 | [Seijaku no Maru (Silence Dome)](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/100-seijaku-no-maru-silence-dome.mp4) · `NF_Anbu_SilenceDome` | PARTIAL | Large enclosing dark disc and silence cues; sound confinement untestable in silent clip. |
| 101 | [Otomaku (Sound Veil)](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/101-otomaku-sound-veil.mp4) · `NF_Anbu_SoundVeil` | UNVERIFIABLE | Self buff cue; suppressed movement sounds not testable in silent clip. |
| 102 | [Kodama Obiki (Echo Lure)](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/102-kodama-obiki-echo-lure.mp4) · `NF_Anbu_EchoLure` | UNVERIFIABLE | Area ripple and target confusion cues; replayed voice untestable in silent clip. |
| 103 | [Jishinken (Earthquake Fist)](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/103-jishinken-earthquake-fist.mp4) · `NF_Anbu_Quake` | PARTIAL | Radial ground-colored pulse and impacts; earth heaving/punch pose not clearly resolved. |
| 104 | [Kijishaku Wana (Chakra Magnet Trap)](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/104-kijishaku-wana-chakra-magnet-trap.mp4) · `NF_Anbu_MagnetTrap` | PARTIAL | Patch marker and enemy status; sticky ground appearance weak. |
| 105 | [Kitoride (Chakra Bulwark)](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/105-kitoride-chakra-bulwark.mp4) · `NF_Anbu_Bulwark` | PARTIAL | Blue round shield around user; described frontal bulwark represented as bubble. |
| 106 | [Sōheki (Twin Barrier)](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/106-s-heki-twin-barrier.mp4) · `NF_Anbu_TwinBarrier` | VISUAL MISMATCH | One oversized blue swirling bubble/disc dominates the recording; two distinct linked barriers are not clearly communicated. |
| 107 | [Kakure Ashi (Unseen Step)](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/107-kakure-ashi-unseen-step.mp4) · `NF_Anbu_UnseenStep` | PARTIAL | Caster fades to faint outline; unseen state visible, sounds untestable. |
| 108 | [Senbon Sōsa (Senbon Control)](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/108-senbon-s-sa-senbon-control.mp4) · `NF_Anbu_Senbon` | PARTIAL | Blue needle-like fan/streak and hit; single needle needs dense review. |
| 109 | [Wana Kakushi (Trap Concealment)](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/109-wana-kakushi-trap-concealment.mp4) · `NF_Anbu_TrapConceal` | NOT DEMONSTRATED | Target flashes and damage; no clearly staged concealed caltrop spread or trigger. |
| 110 | [Yakusō no Chie (Herbal Lore)](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/110-yakus-no-chie-herbal-lore.mp4) · `NF_Anbu_HerbalLore` | UNVERIFIABLE | Green self buff cue; improved wound tending not demonstrated. |
| 111 | [Iyashi no Ki (Healing Aura)](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/111-iyashi-no-ki-healing-aura.mp4) · `NF_Anbu_HealAura` | PARTIAL | Green healing aura/cross visible; wound healing and tiers unverified. |
| 112 | [Mamori no Ki (Protection Aura)](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/112-mamori-no-ki-protection-aura.mp4) · `NF_Anbu_ProtectAura` | PARTIAL | Blue defensive cue on target; deflection not demonstrated. |
| 113 | [Dokuyoke (Poison Ward)](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/113-dokuyoke-poison-ward.mp4) · `NF_Anbu_PoisonWard` | PARTIAL | Green cleansing cue; poison/disease removal not demonstrated. |
| 114 | [Kanzen Yōkai (Complete Meltdown)](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/114-kanzen-y-kai-complete-meltdown.mp4) · `NF_Anbu_Meltdown` | VISUAL MISMATCH | Remote mental tether and purple target marker dominate; rapid close strikes, neck jab and five readable ANBU afterimages are not shown clearly. |
| 115 | [Fūmin (Confined Sleep)](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/115-f-min-confined-sleep.mp4) · `NF_Anbu_ConfinedSleep` | PARTIAL | Wave/ring-like pulse at close range; ordered limb sleep not visible. |
| 116 | [Kekkai Kurai no Honō (Barrier-Eating Flames)](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/116-kekkai-kurai-no-hon-barrier-eating-flames.mp4) · `NF_Anbu_EatingFlames` | PARTIAL | Pale purple flame-like points appear around target; no barrier shown being consumed. |
| 117 | [Shinkeitō (Nerve Blade)](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/117-shinkeit-nerve-blade.mp4) · `NF_Anbu_NerveBlade` | PARTIAL | Blue close-contact strike and blade-like streak; wrist blade weakly legible. |
| 118 | [Shōgeki no Shinjitsu (Shocking Truth)](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/118-sh-geki-no-shinjitsu-shocking-truth.mp4) · `NF_Anbu_ShockingTruth` | PARTIAL | Close blue electrical contact cue; nerve pain/mechanics unverified. |
| 119 | [Shinshō (Stun Palm)](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/119-shinsh-stun-palm.mp4) · `NF_AnbuU_StunPalm` | PARTIAL | Close strike and blue flash; palm electricity readable only broadly. |
| 120 | [Dokushin (Mind Reading)](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/120-dokushin-mind-reading.mp4) · `NF_Anbu_MindReading` | UNVERIFIABLE | Close mental effect; no prisoner resistance UI before/after. |
| 121 | [Kioku Keshi (Manual Amnesia)](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/121-kioku-keshi-manual-amnesia.mp4) · `NF_AnbuU_Amnesia` | UNVERIFIABLE | Self mental cue; no memory list before/after. |
| 122 | [Noroi Ningyō (Curse Doll)](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/122-noroi-ningy-curse-doll.mp4) · `NF_AnbuU_CurseDoll` | NOT DEMONSTRATED | Purple remote status effect visible; clay doll preparation/use is not staged. Doll could be an offscreen prerequisite, so this alone does not prove incorrect implementation. |
| 123 | [Kanashibari](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/123-kanashibari.mp4) · `NF_AnbuU_Paralysis` | PARTIAL | Tether and immobilization cue; freezing broadly readable. |
| 124 | [Kyōonpa (Violent Sound Wave)](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/124-ky-onpa-violent-sound-wave.mp4) · `NF_AnbuU_SoundWave` | PARTIAL | Forward cone of pulses hits several targets; clap motion not clear, audio absent. |
| 125 | [Kan'on (Shrill Tone)](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/125-kan-on-shrill-tone.mp4) · `NF_AnbuU_ShrillTone` | PARTIAL | Large radial sound-like rings and status effects; deafening unverified. |
| 126 | [Kinawa Shibari (Chakra Rope Binding)](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/126-kinawa-shibari-chakra-rope-binding.mp4) · `NF_AnbuU_Rope` | PARTIAL | Blue tether connects target; rope winding around limbs not clear. |
| 127 | [Bōkyaku no Ori (Cage of the Forgotten)](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/127-b-kyaku-no-ori-cage-of-the-forgotten.mp4) · `NF_AnbuU_Cage` | PARTIAL | Blue cage lattice with thin red diamond-like outlines is visible on close inspection. Strengthen the red diamond seal silhouette; do not report enclosure as absent. |
| 128 | [Kitejō (Chakra Cuffs)](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/128-kitej-chakra-cuffs.mp4) · `NF_AnbuU_ChakraCuffs` | CANDIDATE MISMATCH | Blue bubble/target sparkle; hands behind back in chakra cuffs not legible. |
| 129 | [Guren Kadama (Crimson Fireball)](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/129-guren-kadama-crimson-fireball.mp4) · `NF_AnbuU_Fireball` | PARTIAL | Orange burning target/impact; travelling fiery orb needs dense review. |
| 130 | [Sōao Hōkiboshi (Twin Blue Comets)](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/130-s-ao-h-kiboshi-twin-blue-comets.mp4) · `NF_AnbuU_TwinComets` | VISUAL MISMATCH | Paired brown/olive rod-like projectiles cross the lane at about 2.0–3.1 s; they do not read as blue fire comets. |
| 131 | [Yōkai Kiri (Dissolving Mist)](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/131-y-kai-kiri-dissolving-mist.mp4) · `NF_AnbuU_DissolvingMist` | CANDIDATE MISMATCH | Area ring, large central blob and blue-white impacts; continuous corrosive mist not obvious. |
| 132 | [Shitai Shobun (Body Disposal)](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/132-shitai-shobun-body-disposal.mp4) · `NF_AnbuU_Disposal` | NOT DEMONSTRATED | Generic blue/white target effect; no clear corpses engulfed in blue flames and removed. |
| 133 | [Shitai Hozon (Body Conservation)](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/133-shitai-hozon-body-conservation.mp4) · `NF_AnbuU_Conservation` | NOT DEMONSTRATED | Blue pulse around caster; nearby corpses and their protective shells not staged. |
| 134 | [Kanpeki Nage (Perfect Throw)](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/134-kanpeki-nage-perfect-throw.mp4) · `NF_AnbuU_PerfectThrow` | UNVERIFIABLE | Self-buff marker; no thrown weapon with guiding threads. |
| 135 | [Tsuiseki no Jutsu (Tracking Technique)](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/135-tsuiseki-no-jutsu-tracking-technique.mp4) · `NF_AnbuU_Tracking` | NOT DEMONSTRATED | Self pulse only; revealing enemies at long distance not demonstrated. |
| 136 | [Don the Mask](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/136-don-the-mask.mp4) · `NF_ANBU_Mask` | PARTIAL | Buff activation/melee; mask appearance subtle, day-long buff unverified. |
| 137 | [Smoke Escape](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/137-smoke-escape.mp4) · `NF_ANBU_Smoke` | PARTIAL | White smoke-like cloud and fading user visible; bright central burst dominates. |
| 138 | [Shadow Stealth](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/138-shadow-stealth.mp4) · `NF_ANBU_Stealth` | PARTIAL | Caster fades slightly with dark aura; melting into shadow weak. |
| 139 | [Shadow Squad](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/139-shadow-squad.mp4) · `NF_ANBU_Squad` | PARTIAL | Large shadow area and caster fading; affected friends not clearly distinguished. |
| 140 | [Tanto Flash](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/140-tanto-flash.mp4) · `NF_ANBU_Tanto` | PARTIAL | Dash/afterimage line through target; short blade itself hard to resolve. |
| 141 | [Silent Kill](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/141-silent-kill.mp4) · `NF_ANBU_Silent` | PARTIAL | Single close strike and target falls; vital strike/health threshold unverified. |
| 142 | [Burning Legs](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/142-burning-legs.mp4) · `NF_RedLeg_Leg` | PARTIAL | Orange heat cue during melee; burning legs and kicks not clearly distinguished in overview. |
| 143 | [Searing Shin](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/143-searing-shin.mp4) · `NF_RedLeg_Shin` | PARTIAL | Close red-hot impact; shin motion needs dense review. |
| 144 | [Flaming Axe Kick](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/144-flaming-axe-kick.mp4) · `NF_RedLeg_Axe` | PARTIAL | Close fiery swing/impact; downward heel action needs dense review. |
| 145 | [Burning Sky Step](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/145-burning-sky-step.mp4) · `NF_RedLeg_Skywalk` | PARTIAL | Fiery dash into target; air kick and line-through-enemies movement need dense review. |
| 146 | [Burning Whirl](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/146-burning-whirl.mp4) · `NF_RedLeg_Whirl` | PARTIAL | Circular fiery attack affects nearby enemies; kick body motion needs dense review. |
| 147 | [Crimson Inferno Kick](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/147-crimson-inferno-kick.mp4) · `NF_RedLeg_Inferno` | PARTIAL | Strong red-hot single impact; distinct kick needs dense review. |
| 148 | [Battōjutsu (Art of Drawing the Blade)](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/148-batt-jutsu-art-of-drawing-the-blade.mp4) · `NF_Arch_Busosen_Draw` | PARTIAL | Close slash and hit; unsheathing/draw motion hard to read at overview scale. |
| 149 | [Hanabira Surasshu (Petal Slash)](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/149-hanabira-surasshu-petal-slash.mp4) · `NF_Arch_Busosen_PetalSlash` | PARTIAL | Pink slash arc and follow-up hits; quick forward cuts broadly fit. |
| 150 | [Kagenui (Shadow Stitch)](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/150-kagenui-shadow-stitch.mp4) · `NF_Arch_Busosen_ShadowStitch` | PARTIAL | Caster dashes to victim with afterimage; behind-target relation needs closer check. |
| 151 | [Shidensen (Purple Lightning Flash)](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/151-shidensen-purple-lightning-flash.mp4) · `NF_Arch_Busosen_PurpleFlash` | PARTIAL | Purple electrified close cut and STUN indicator visibly fit. |
| 152 | [Sakura Tsuisutā (Sakura Twister)](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/152-sakura-tsuisut-sakura-twister.mp4) · `NF_Arch_Busosen_SakuraTwister` | PARTIAL | Circular slash effects reach nearby enemies; spinning draw-cut not fully resolved. |
| 153 | [Fureā (Flare)](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/153-fure-flare.mp4) · `NF_Arch_Busosen_Flare` | PARTIAL | Circular orange attack/target hits; spiral cut obscured by fire-like particles. |
| 154 | [Gosei Ryuu: Wisdom Dragon Stance](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/154-gosei-ryuu-wisdom-dragon-stance.mp4) · `NF_Kenseijin_StanceGosei` | UNVERIFIABLE | Blue stance glyph; damage matchup and exclusivity unverified. |
| 155 | [Genkai Ryuu: Courage Dragon Stance](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/155-genkai-ryuu-courage-dragon-stance.mp4) · `NF_Kenseijin_StanceGenkai` | UNVERIFIABLE | Gold stance glyph; damage matchup and exclusivity unverified. |
| 156 | [Tsuyosa Ryuu: Power Dragon Stance](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/156-tsuyosa-ryuu-power-dragon-stance.mp4) · `NF_Kenseijin_StanceTsuyosa` | UNVERIFIABLE | Red stance glyph; damage matchup and exclusivity unverified. |
| 157 | [Genkai Ryuu: Jinsokugeiru (Rapid Gale)](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/157-genkai-ryuu-jinsokugeiru-rapid-gale.mp4) · `NF_Kenseijin_GenkaiGale` | PARTIAL | Close slash visible; opposing double-slash timing needs dense review. |
| 158 | [Genkai Ryuu: Herumukatsu (Crown Splitter)](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/158-genkai-ryuu-herumukatsu-crown-splitter.mp4) · `NF_Kenseijin_GenkaiCrown` | PARTIAL | Close blade arcs and victim collapse are visible; leap height and descending head strike remain difficult to read. |
| 159 | [Genkai Ryuu: Issen (Flash)](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/159-genkai-ryuu-issen-flash.mp4) · `NF_Kenseijin_GenkaiIssen` | PARTIAL | Blue defensive ring and close cut; counter trigger and lethal power unverified. |
| 160 | [Tsuyosa Ryuu: Gufuukakou (Tornado Drop)](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/160-tsuyosa-ryuu-gufuukakou-tornado-drop.mp4) · `NF_Kenseijin_TsuyosaDrop` | PARTIAL | Close circular motion, rotated pawns and victim collapse are visible. Grab, lift and ground-drive phases need clearer separation; do not claim there is no spinning motion. |
| 161 | [Tsuyosa Ryuu: Kaisoku (Quick of Foot)](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/161-tsuyosa-ryuu-kaisoku-quick-of-foot.mp4) · `NF_Kenseijin_TsuyosaDisarm` | NOT DEMONSTRATED | Close blue strike; no clear weapon flying free or target becoming unarmed. |
| 162 | [Tsuyosa Ryuu: Nijuu no Kiwami (Twofold Strike)](https://cassiegiang.github.io/NFRP-Anim/clans-and-styles/162-tsuyosa-ryuu-nijuu-no-kiwami-twofold-strike.mp4) · `NF_Kenseijin_TsuyosaTwofold` | PARTIAL | Close repeated impact cues; simultaneous paired blows need dense review; armour bypass untestable visually. |
