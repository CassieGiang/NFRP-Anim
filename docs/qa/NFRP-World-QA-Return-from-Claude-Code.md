# NFRP World QA: return from Claude Code

Reply to `NFRP-World-QA-Handoff-for-Claude-Code.md` · 22 October 2026 · NFRP-World `main`.
Fix commit: `10fe397`. The fix commit's parent is `0cd7ee9`, the revision that was reviewed. All findings applied at that revision.

Runtime status: the C# builds and both IL reference checks pass. Nothing below has been run in game yet. These fixes ship in the next install (u175), and the in-game acceptance cases are still open.

| QA | Applies | Changed files | Before → after | Verified by |
|---|---|---|---|---|
| QA01 mission XP targeting | yes | `src/NFMissions.cs` | Before: every loaded site map paid out, narrowing to the enemy faction only when one matched. After: only the mission's own site pays out. The site comes from the signal's SUBJECT, otherwise from the quest's `QuestPart_SpawnWorldObject`. If that site map is gone, nothing is paid and a log line says so. There is no fallback. XP and fame use the same crew. Idempotency (`xpGiven`) is unchanged and is saved. | Build only. The in-game cases (two sites of the same faction, an unrelated site, save/load, a double signal) are still to run. |
| QA02 gate approves partial runs | yes | `tools/gate.py` | Before: no FAIL rows meant "OK to install". After: a run with skipped checks prints `PARTIAL ... not an install approval` and shows passed, failed, warned and skipped counts. With `--release`, any skipped check exits 1 and the skipped checks are named. | `python3 tools/gate.py --mod mod` prints PARTIAL with 7 passed, 0 failed, 9 skipped. |
| QA03 duplicate defNames | yes | `tools/rules/data.py` (`duplicates()`), `tools/gate.py` (`d) unique defNames`) | Before: later duplicates overwrote earlier ones silently. After: duplicates fail and list every file involved. The key is the full XML tag, so the same name on different def types is allowed. | New self-test mutation: a second file holding `KZ_ClanKazeraikou` is KILLED. The real data is clean. |
| QA04 material cache cap | partly | `src/NFRes.cs` (comment, policy) | Kept as a documented soft cap. Past the cap, each new texture+shader pair gets exactly one material, and every later tint of that pair reuses its nearest one. Growth is therefore bounded by the number of distinct pairs, which is finite because the mod's textures are fixed. Eviction was rejected because it could destroy a material that a queued draw still uses. `Overflow` counts these allocations. | Code reasoning. Disagree here if you think hard eviction is worth the risk. |
| QA05 reuse test | yes | `src/NFTestResources.cs` | Before: the test passed even with one allocation per request. After: 20 fixed tints are asked for twice, and any growth on the second pass FAILs. The random-tint count is now information only. | Build only (in-game test). |
| QA06 pycache crash | yes | `tools/gate.py` (`check_tools`, self-test cleanup) | Before: generated directories were hashed and crashed the gate. After: only regular files are hashed, and `.pyc` files and `__pycache__` are ignored. The self-test now cleans its temporary copies in a `finally` block. | `compileall` followed by `--self-test` no longer crashes. |
| Giddy-Up | yes | `tools/gate.py` | It is now RECOMMENDED, matching `About.xml`, where it appears only in loadAfter. A mod list without it passes. If it is present, it must load before NFRP World. | Self-test: the control case without Giddy-Up passes, and Giddy-Up loading after NFRP World is KILLED. |
| Self-test prerequisites | yes | `tools/gate.py` | The weapon-angle art mutation prints `NOT RUN` when there are no textures, instead of SURVIVED. The def-count baseline was refreshed from 162 to 183 files; the stale baseline is why the hediff-removal mutation survived. | `--self-test`: 9 of 9 caught, with 1 art mutation not run (no textures). |
| IL tools | yes | `tools/il/check_refs.py`, `check_refs17.py` | A disassembler failure or empty output exits 2. Zero inspected references exits 3. Neither prints a clean result. | `build.sh` still passes both IL checks. |

Not done:
- GitHub Actions.
- `build.sh` portability: the paths are still machine-specific.

The animation handout (`NFRP-Anim-Visual-QA-for-Claude-Code.md`) is being merged with Claude's own frame review of the 4K recording, 24 frames per clip. The fixes will be returned with before/after clips.
