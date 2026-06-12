# BRANCH DESIGN SYSTEM
**Document Type:** Multi-Edition Brand Reference  
**Version:** 1.0  
**Status:** ACTIVE

This document defines the color palette, typography application, cover direction, and terminology
notes for each of the 6 military branch editions of the Sustainment Operations Manual series.

The interior content (all 50 SOPs) is **identical across all editions**. What changes per edition:
- Cover design (color, imagery, branch name)
- Master page color variables in the layout template
- Commander's Intent foreword page (1 page, branch-specific)

---

## SHARED DESIGN CONSTANTS (all editions)

These elements are fixed across every branch edition.

| Element | Spec |
|---|---|
| Interior | B&W only (no color in interior pages) |
| Display font | Black Ops One / Stencilia (headlines, SOP titles) |
| Body font | Roboto Mono / Courier New (body text) |
| Data font | DIN Condensed / Bahnschrift (stats, macros) |
| Header bar | Full-width black bar across top of each SOP page |
| Section labels | Bold caps, e.g. INTELLIGENCE / HARDWARE / SUPPLIES / EXECUTION / AAR |
| Icons | `[!]` Danger, `[T]` Timing, `[R]` Rank, `[H]` Hardware |
| Page border | Heavy black rule, 1pt minimum |
| Rank system | Private → Recruit → Corporal → Sergeant → Commander |
| Execution phases | INFIL (Prep) → ENGAGEMENT (Cook) → EXFIL (Plate/Clean) |
| Footer | "SUSTAINMENT OPERATIONS MANUAL // VOL 1: FOUNDATIONS" |

---

## TRADEMARK RULE (applies to all editions)

Every US military branch holds federally registered trademarks on its official insignia:
- **Army**: Gold star emblem and eagle design
- **Marines**: Eagle, Globe and Anchor
- **Navy**: Fouled anchor design
- **Air Force**: Wing and star emblem
- **Coast Guard**: Racing stripe, torch and shield
- **Space Force**: Delta emblem

**Covers must NOT use or trace any official seal, crest, emblem, or insignia.**

Safe to use on covers: branch-inspired color palettes, branch names (e.g., "ARMY EDITION"),
generic tactical imagery (soldier silhouettes, generic anchors, generic wings, camo textures,
stars, aircraft silhouettes). No "officially endorsed by..." language anywhere.

---

## EDITION 1 — ARMY

**Series title:** Sustainment Operations Manual — Army Edition

| Element | Value |
|---|---|
| Primary (header bars, rules, accents) | OD Green `#4B5320` |
| Secondary (call-out boxes, backgrounds) | Coyote Tan `#A59C82` |
| Accent (warnings, critical temps, timers) | Safety Orange `#FF6600` |
| Text | Charcoal `#333333` |
| Background / reverse text | Stencil White `#F2F2F2` |

**Cover direction:** OD Green background. Stencil typography. Woodland camouflage texture or
generic combat boot close-up. Tactical line-art or soldier silhouette (no official Army star
emblem). "ARMY EDITION" in Safety Orange stencil beneath the series title.

**Commander's Intent foreword:** Written in the voice of a veteran senior NCO. Emphasis on
feeding the unit, provider mentality, logistics as combat power. Reference the Army's "sustainment"
doctrine language — which already mirrors the product name.

**File:** `01_Intelligence/Commanders_Intent_Army.md` *(already exists as `The_Commanders_Intent.md`)*

---

## EDITION 2 — MARINE CORPS

**Series title:** Sustainment Operations Manual — Marine Corps Edition

| Element | Value |
|---|---|
| Primary | Scarlet `#CC0000` |
| Secondary | Gold `#FFB300` |
| Accent | Black `#000000` |
| Text | Black `#1A1A1A` |
| Background / reverse text | White `#FFFFFF` |

**Cover direction:** Scarlet background with gold typography. Aggressive, bold layout — minimal
ornamentation. Generic EGA-inspired imagery WITHOUT the official Eagle, Globe and Anchor (use a
globe silhouette with generic wings + anchor separately). "MARINE CORPS EDITION" in bold gold
stencil. Semper Fidelis motto may be used (it is not a trademarked phrase).

**Commander's Intent foreword:** Short, direct, aggressive tone. Every Marine is a rifleman first —
every Marine can feed themselves and their unit. Emphasis on self-sufficiency, toughness, and
the combat kitchen as another field where Marines do not accept failure.

**File to create:** `01_Intelligence/Commanders_Intent_Marines.md`

---

## EDITION 3 — NAVY

**Series title:** Sustainment Operations Manual — Navy Edition

| Element | Value |
|---|---|
| Primary | Navy Blue `#003087` |
| Secondary | Gold `#B8860B` |
| Accent | White `#FFFFFF` |
| Text | `#1A1A1A` |
| Background / reverse text | White `#FFFFFF` |

**Cover direction:** Navy blue background with gold typography. Nautical texture (rope pattern,
water distress texture). Generic anchor silhouette (not the official fouled anchor design —
use a clean stock anchor or rope coil). "NAVY EDITION" in gold stencil. Clean, authoritative
aesthetic — the Navy's culinary tradition is real (Navy cooks/culinary specialists are a formal
rate). Lean into the "Galley" language.

**Terminology note:** The word "kitchen" can become "galley" on the Commander's Intent page
and any branch-specific intro text. The SOP interior content does not need to change.

**Commander's Intent foreword:** Reference the Navy's culinary specialist (CS) rating and the
tradition of the ship's galley as operational lifeblood. At sea, the galley is mission-critical
logistics. Every sailor feeds the mission.

**File to create:** `01_Intelligence/Commanders_Intent_Navy.md`

---

## EDITION 4 — AIR FORCE

**Series title:** Sustainment Operations Manual — Air Force Edition

| Element | Value |
|---|---|
| Primary | Air Force Blue `#00308F` |
| Secondary | Silver `#A2AAAD` |
| Accent | White `#FFFFFF` |
| Text | `#1A1A1A` |
| Background / reverse text | White `#FFFFFF` |

**Cover direction:** Air Force blue with silver/white typography. Clean, technical, precise
aesthetic — Air Force brand is the most "corporate military" of the branches. Generic jet
silhouette or abstract airframe lines. "AIR FORCE EDITION" in clean stencil. The Air Force has
the most culturally approachable reputation — lean into the technical precision angle (calibrated
cooking, precision temps, dialing in macros like a flight engineer).

**Terminology note:** "Squadron" instead of "unit" works well in the foreword. "Sortie" for a
cooking session is an option. Keep it light — Air Force humor skews self-aware.

**Commander's Intent foreword:** Reference Air Force "Warrior Airmen" culture. Fuel for the
mission — whether the mission is a 14-hour sortie or a 14-hour brisket. Precision and execution
are Air Force values that transfer directly to the kitchen.

**File to create:** `01_Intelligence/Commanders_Intent_AirForce.md`

---

## EDITION 5 — COAST GUARD

**Series title:** Sustainment Operations Manual — Coast Guard Edition

| Element | Value |
|---|---|
| Primary | Dark Blue `#003366` |
| Secondary | Safety Orange `#FF6600` |
| Accent | White `#FFFFFF` |
| Text | `#1A1A1A` |
| Background / reverse text | White `#FFFFFF` |

**Cover direction:** Dark blue and Safety Orange (the Coast Guard's rescue orange). Maritime
texture — waves, rope, water-worn surfaces. Generic lighthouse silhouette or generic cutter
silhouette (not the official racing stripe design). "COAST GUARD EDITION" in orange stencil
on dark blue. The rescue/preparedness angle is strong — feeding yourself and your crew is part
of operational readiness.

**Note:** Coast Guard operators are some of the most adaptable service members — they do law
enforcement, search and rescue, and maritime operations. The "improvise, adapt, overcome" angle
plays well for this audience.

**Commander's Intent foreword:** Semper Paratus ("Always Ready") — the Coast Guard motto (not
trademarked as a phrase). Operational readiness includes nutritional readiness. In remote
deployments (cutters, stations), the galley is everything. Every Coast Guardsman feeds the mission.

**File to create:** `01_Intelligence/Commanders_Intent_CoastGuard.md`

---

## EDITION 6 — SPACE FORCE

**Series title:** Sustainment Operations Manual — Space Force Edition

| Element | Value |
|---|---|
| Primary | Space Black `#1B1B2F` |
| Secondary | Delta Blue `#1E3A5F` |
| Accent | Metallic Silver `#C0C0C0` |
| Text | Silver `#D0D0D0` (light on dark) |
| Background / reverse text | Space Black `#1B1B2F` |

**Cover direction:** Dark background with star field or abstract orbital-grid texture. Metallic
silver typography. The most futuristic and modern of all covers. Generic satellite or astronaut
silhouette (no official Space Force delta emblem). "SPACE FORCE EDITION" in metallic stencil.
This edition has the highest meme/viral potential — lean into the absurdist contrast of space
operators needing to cook real food. "The orbital kitchen."

**Terminology note:** The Space Force is new (est. 2019) and leans heavily into sci-fi aesthetic
in its official branding. The foreword can be more creative and humor-forward than other editions.
"Guardians" is the official Space Force member title (not trademarked as a generic term).

**Commander's Intent foreword:** The most futuristic foreword in the series. In a world of
extended missions, remote deployments, and the precision demands of space operations, food is
fuel and fuel is mission-critical. Whether you're at a command center in Colorado or stationed
globally, your operational effectiveness starts at 0600 with what you put in your body. The
orbital kitchen runs the same physics as every other kitchen — just with higher stakes.

**File to create:** `01_Intelligence/Commanders_Intent_SpaceForce.md`

---

## PRODUCTION WORKFLOW PER NEW EDITION

When a new branch edition is ready to produce:

1. **Cover** — Duplicate the Army Canva cover file → apply branch color scheme → update branch
   name text → swap imagery to branch-appropriate generic art → export PDF for print
   
2. **Foreword page** — Write `01_Intelligence/Commanders_Intent_[Branch].md` (~200–300 words,
   same tactical voice) → flow into the layout as the first interior page after the TOD

3. **Interior color swap** — In Affinity Publisher (or Canva), open the master page template →
   change the primary color variable to the branch primary → export new interior PDF
   *(Note: B&W interior means only section header shading/rules change — minimal visual change
   between editions. The main differentiation is the cover.)*

4. **Upload** — Create new KDP project, upload interior + cover, set price ($24.99) → publish.
   Repeat for Lulu ($29.99 coil-bound).

5. **Trademark review** — Confirm no official insignia on cover before submitting to KDP/Lulu.

---

*End of Branch Design System v1.0*
