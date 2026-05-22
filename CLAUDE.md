# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

CookBook is a **content-only project** — there is no code, build system, or runtime. It produces a physical printed product: a modular, waterproof, tactical-themed 3-ring easel binder for men learning to cook. All content is Markdown.

The brand identity is a military field-guide: cooking is framed as operational missions, recipes are SOPs (Standard Operating Procedures), and every term follows tactical nomenclature.

## Content Workflow

There is no build or test command. Content management is entirely Git + Markdown:

- **Add a recipe:** Copy `03_SOP_Recipes/SOP_TEMPLATE.md` → fill in all 5 sections → place in the correct subdirectory (`Quick_Strike/`, `Heavy_Lift/`, `Field_Rations/`, or `Morale_Boosters/`) → commit.
- **Update existing content:** Edit the relevant `.md` file and commit.
- **Design compliance:** All new content must conform to `04_Design_Assets/Style_Guide.md` before it is considered ready.

## Repository Structure

```
00_Table_of_Distribution.md  # Master index — all 50 SOPs logged
01_Intelligence/             # Nutrition, Safety, Battle Rhythm, Recon, Field Repair, Sanitation
02_Hardware_Specs/           # Armory Kit, Blade Maintenance, Cast Iron Restoration
03_SOP_Recipes/
  ├── Quick_Strike/          # 15-min meals (31 SOPs)
  ├── Heavy_Lift/            # Slow-cook / large roasts (14 SOPs)
  ├── Field_Rations/         # Meal prep / bulk cooking (4 SOPs)
  └── Morale_Boosters/       # Beverages (SOP-048)
04_Design_Assets/            # Style Guide, Tab Specs
05_Logistics_Supply/         # Production costs, Easel Binder specs
06_Marketing_Comms/          # Kickstarter plan, Funnel logic, Launch checklist
```

## SOP Template (Mandatory Structure)

Every recipe file must follow the exact 5-section format in `03_SOP_Recipes/SOP_TEMPLATE.md`:

1. **Intelligence** — Stats block: difficulty rank, time, servings, macros (P/C/F/Cal)
2. **Hardware** — Checklist of tools with `[ ]` format
3. **Supplies** — Ingredient list (called "consumables")
4. **Execution** — Three phases: Infil (prep) → Engagement (cooking) → Exfil (cleanup/plating)
5. **After Action Report (AAR)** — Field notes, variations, storage

File naming convention: `SOP-[NNN]-Operation-[Codename].md`

## Terminology Reference

| Casual term | Tactical term used in this project |
|---|---|
| Recipe | SOP / Mission |
| Prep | Infil |
| Cooking | Thermal Dwell / Engagement |
| Cleanup | Exfil |
| Cooking notes | After Action Report (AAR) |
| Tools | Hardware |
| Ingredients | Supplies / Consumables |
| Difficulty | Rank (Private → Commander) |
| Family/team | The Unit |

Never use casual cooking language in SOP content — always use the tactical equivalent.

## Design Constraints

From `04_Design_Assets/Style_Guide.md` — these apply to any visual or layout output:

- **Brand colors:** OD Green `#4B5320`, Coyote Tan `#A59C82`, Safety Orange `#FF6600`, Charcoal `#333333`, Stencil White `#F2F2F2`
- **Fonts:** Stencilia / Black Ops One (headlines), Roboto Mono / Courier (body), DIN Condensed (data/stats)
- **Layout:** Heavy black borders, redaction bars, SOP ID in top-right corner of each page
- **Photography:** High-contrast action shots only — no soft-focus food styling
- **Iconography:** `[!]` Danger, `[T]` Timing, `[R]` Rank, `[H]` Hardware

## Physical Product Constraints

Content is formatted for waterproof synthetic paper (Rite in the Rain / REVLAR / YUPO) in **5.5"×8.5" or 8.5"×11"** format. Every SOP must be **self-contained** — legible and complete as a single removable page, usable standalone or inside the full binder.

Retail target: $55–$75. Build cost: $25.50–$35.50.
