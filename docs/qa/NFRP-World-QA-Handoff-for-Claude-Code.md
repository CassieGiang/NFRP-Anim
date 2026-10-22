# NFRP World QA handoff for Claude Code

Prepared by Codex for Claude Code and Cassie on 22 October 2026.

## Purpose and scope

We are collaborating on the quality of NFRP World. This handoff records the findings from Codex's initial source review and offline validation, and gives Claude Code concrete implementation and regression-test targets. Start by reproducing the findings against your current checkout. If the code has changed, record whether each finding still applies before changing it.

Repository: https://github.com/CassieGiang/NFRP-World

Reviewed revision: `0cd7ee9ce427cfc861d1e7aa9caa38eb9d6732c9` on `main`.

The XML data passed the checks described below. The main concerns are incomplete release validation, missing duplicate-ID detection, mission reward targeting, and material-cache behavior. This was a focused review, not an exhaustive audit of every C# execution path.

No fixes, commits, pushes, or pull requests were made during this review. This document proposes work; it does not record completed remediation.

## Evidence and test results

| Check performed | Observed result | Scope limitation |
|---|---|---|
| Parse mod XML | 231 files parsed successfully | Does not prove RimWorld can resolve every external reference |
| Duplicate definition scan | No duplicate type and defName pairs among 6,316 definition entries | Separate QA scan; the built-in gate lacks this protection |
| Internal ability tier references | 1,638 entries inspected; no missing NF or KZ targets | External framework targets excluded from missing-target checks |
| Internal ability tree references | 746 entries inspected; no missing NF or KZ targets | Same restriction |
| PawnKindDef race references | 114 entries inspected; no missing NF or KZ targets | Same restriction |
| Named XML parent cycles | None found among locally defined parents | External parents not resolved |
| Local C# type names referenced by XML | No missing names found in inspected class fields and attributes | Name-based scan, not compiled type or namespace validation |
| Python syntax compilation | All 53 Python scripts compiled | Syntax only, not full behavioral coverage |
| Shell syntax | `sh -n tools/build.sh` passed | No actual C# build |
| Offline gate | Exit 0 with 6 passing and 9 skipped checks | Printed “OK to install” despite incomplete coverage |
| Gate self-test after cache cleanup | Exit 1; 7 of 8 mutations caught | Weapon-angle mutation survived because textures were absent |
| Gate self-test after Python compilation | Crashed with IsADirectoryError | Generated tools/device/__pycache__ caused the crash |
| Duplicate-ID mutation | Gate exited 0 after inserting a duplicate KZ_ClanKazeraikou | Confirmed validator defect in a temporary copy |

Commands run from the repository root included:

```sh
python3 -m compileall -q tools
python3 tools/gate.py --mod mod
python3 tools/gate.py --mod mod --self-test
sh -n tools/build.sh
```

C# compilation and in-game tests were not executed. The environment lacked the RimWorld, Unity, Harmony, and Taran Magic Framework DLLs, the game runtime, and the excluded texture assets. Do not interpret the Python or XML results as a successful mod build or an in-game pass.

## QA01 Mission XP can reach unrelated quest sites

**Priority:** High. **Evidence:** C# code review; not reproduced in-game.

**Location:** `src/NFMissions.cs`, `QuestPart_NFBonus.GiveXP`, approximately lines 156–176.

The code initially selects every loaded non-home map whose parent is a Site. It narrows this list to maps belonging to the enemy faction only if at least one such map exists. It then gathers ninja from every selected map. Two loaded sites belonging to the same enemy faction can both contribute reward recipients. If no map matches that faction, the fallback can reward ninja at unrelated sites. Fame is also awarded to the resulting crew through NFFame.OnMission.

**Suggested fix:** Persist a reference to the specific quest site, or an explicit mission participant set, and use it for both XP and fame. Do not fall back to every loaded site. Define what happens if the site map no longer exists when the signal arrives. Set the idempotency flag consistently with the chosen completion policy.

**Acceptance checks:**

- Load two quest sites owned by the same enemy faction, with different ninja at each. Completing site A rewards only site A's eligible participants.
- Load an unrelated site while the target map is absent. Its pawns receive no mission reward.
- Save and reload before completion; attribution still identifies the intended site.
- Deliver the completion signal twice; XP, fame, and item rewards are not duplicated.
- Preserve the existing rank eligibility policy and test it explicitly.

## QA02 The release gate approves partial validation

**Priority:** High. **Evidence:** Reproduced offline.

**Location:** `tools/gate.py`, `Gate.fails`, `Gate.show`, and the CLI exit handling; approximately lines 22–26 and 377.

Running `python3 tools/gate.py --mod mod` returned exit 0 and “OK to install” with nine skipped checks. Missing coverage included game-closed status, package manifest, DLL build identity, IL references, external def references, art, wiki, device tools, and the mod list. The tool currently equates the absence of FAIL rows with readiness to install.

**Suggested fix:** Make the validation mode explicit. Offline mode may pass the checks it can perform but should clearly report partial validation. Release mode should require its relevant inputs and checks to complete. Keep optional integrations optional, and define which checks are required for each package type instead of requiring unrelated inputs universally.

**Acceptance checks:**

- A source-only run reports partial validation and never claims release readiness.
- Release mode with a missing required input exits nonzero and names the missing check.
- A fully supplied release run can pass without unrelated optional integrations.
- Output includes passed, failed, skipped, and incomplete counts suitable for CI.

## QA03 Duplicate definition IDs are silently overwritten

**Priority:** Medium. **Evidence:** Reproduced against the full offline gate.

**Location:** `tools/rules/data.py`, `load`, approximately line 31; `tools/gate.py`, `check_defs`.

The loader stores definitions in a dictionary keyed by type and defName. A later duplicate overwrites the previous entry. The gate therefore cannot reliably detect duplicate IDs through downstream checks or label checks.

**Reproduction:** In a temporary copy of `mod`, copy the `TaranMagicFramework.AbilityTreeDef` element with defName `KZ_ClanKazeraikou` from `1.6/Defs/KZ_Abilities.xml` into a new `Defs` XML file. Run the gate against the temporary mod. It reports 6,317 entries and exits 0.

**Suggested fix:** Detect duplicate keys before assignment, retain both source filenames, and emit a failing result. Keep definition type in the key so intentional name reuse across unrelated def types does not become a false positive. Consider storing definition identities in the baseline as well as per-file counts to catch same-count replacements or renames.

**Acceptance checks:** Duplicates within one file and across two files fail with both source locations. A control case using the same name for different def types follows RimWorld's actual uniqueness rules. The reviewed unmodified data remains clean.

## QA04 Material cache capacity is not a hard limit

**Priority:** Medium. **Evidence:** C# code review; not executed in Unity.

**Location:** `src/NFRes.cs`, `NFMatCache.Get`, approximately lines 195–219.

At capacity, reuse happens only if byBase already contains the texture and shader pair. A request for a new pair falls through to new Material and adds an entry even when map.Count is already at cap. The declared cache capacity therefore does not bound the entry count across new pairs. This is relevant because the cache exists to control runtime graphics allocations; this review did not prove a GPU crash or measure memory consumption.

**Suggested fix:** Define and enforce a capacity policy across texture and shader pairs. If evicting materials, account for queued draws and the existing deferred-destruction mechanism. Do not return an unrelated texture simply to meet the limit. Handle externally destroyed cached materials and exceptions during initialization deliberately.

**Acceptance checks:** Exercise more unique texture and shader pairs than the capacity; verify the agreed bound, valid rendering after eviction, eventual disposal, and stable allocations over repeated cycles. Confirm existing same-pair color reuse still works.

## QA05 Material reuse stress test accepts one allocation per request

**Priority:** Medium. **Evidence:** C# test assertion review; not executed in-game.

**Location:** `src/NFTestResources.cs`, approximately lines 35–55.

The test makes 200 random-tint requests and warns only if matsGrew is greater than 200. Allocating exactly one material per request passes, although the warning text identifies that behavior as a problem. This assertion does not demonstrate reuse or enforce capacity. The separate end-of-run cache check does not make this particular assertion effective.

**Suggested fix:** Use deterministic requests to test distinct behaviors: initial population, identical-key reuse, quantization collisions, and overflow across different texture and shader pairs. Assert deltas against measured baselines rather than expecting random colors to collide.

**Acceptance checks:** A deliberately broken cache that allocates on every identical request fails. Repeating an existing request adds zero materials. Overflow tests exercise QA04. A test that inspected no resources reports incomplete or not tested rather than a pass.

## QA06 Python cache directories crash tool comparison

**Priority:** Medium. **Evidence:** Reproduced.

**Location:** `tools/gate.py`, `check_tools`, approximately lines 228–235.

The function globs every entry under tools/device and passes entries to sha1 without checking whether they are files. Running Python syntax compilation creates tools/device/__pycache__. The gate self-test copies that directory and then fails while trying to hash it.

**Reproduction:**

```sh
python3 -m compileall -q tools
python3 tools/gate.py --mod mod --self-test
```

Observed failure: IsADirectoryError for the copied device-tools __pycache__ directory. After removing generated caches and disabling bytecode writes, the self-test completed with 7 of 8 mutations caught; the remaining art mutation lacked textures.

**Suggested fix:** Compare an explicit set of supported device scripts, or filter regular files and exclude generated directories. Required scripts should still fail clearly when missing or changed. Use cleanup in finally blocks so self-test crashes do not leave temporary mod copies behind.

**Acceptance checks:** Run with __pycache__, an unrelated directory, a stale required script, and a missing required script. Generated directories do not crash the gate; actual script mismatches still fail.

## Additional consistency and test improvements

**Giddy-Up dependency mismatch:** `mod/About/About.xml` describes Giddy-Up as recommended, but `tools/gate.py` lists memegoddess.giddyup in REQUIRED. A test ModsConfig with the documented required mods and NFRP World, without Giddy-Up, produced FAIL. Decide whether it is optional or mandatory, then align metadata, documentation, validation, and test expectations. If optional, absence should disable riding checks or report them as not applicable.

**Mutation self-test prerequisites:** The weapon-angle mutation survived in the source-only checkout because textures are omitted. Report missing prerequisites explicitly and separate data-only mutations from art-dependent mutations. Do not present an unexecuted art check as evidence that the art rule itself failed.

**IL tool robustness:** Both tools/il/check_refs.py and check_refs17.py ignore the disassembler's return code. With a simulated failing disassembler returning empty stdout, they printed “ok refs 0” and an empty MISSING result. The current outer baseline wrapper can reject the resulting none entry, so this is not evidence of an end-to-end release bypass. Explicitly reject subprocess failure and zero-inspection runs, retain stderr, and honor configurable reference paths.

**Build portability:** tools/build.sh exposes environment variables for dependencies, but its defaults and the IL scripts include machine-specific paths. Validate dependency availability early, quote all reference-path arguments, and document a reproducible setup. Do not commit proprietary game DLLs.

## Suggested implementation order

1. Reproduce QA02, QA03, and QA06 and add focused Python regression tests. Make release decisions trustworthy before using the gate to approve subsequent packages.
2. Resolve the Giddy-Up policy and art-test prerequisite reporting.
3. Fix QA01 and validate with simultaneous quest sites and save/load.
4. Fix QA04 and QA05 together; verify both rendering correctness and resource disposal in-game.
5. Add GitHub Actions for source-only checks. Run game-dependent build and integration validation only in an appropriately configured environment, with missing prerequisites visible.

## Return handoff for Codex QA

For each finding, return its QA identifier, applicability at the current revision, changed files, the behavior before and after the fix, regression-test commands and results, and any remaining limitations. Include commit IDs or a reviewable diff. Keep runtime verification separate from static reasoning and simulated subprocess tests.

Codex can then review the diff, rerun the available checks, and challenge the fixes with the acceptance cases above. This document itself does not transmit anything to Claude Code; Cassie can supply it directly in the Claude Code session.
