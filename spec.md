# SUSTAINMENT OPERATIONS MANUAL — MASTER SPEC
**Document Type:** Project Specification & Implementation Roadmap  
**Version:** 1.0  
**Date:** 2026-05-24  
**Status:** ACTIVE — Pre-Production

---

## 1. EXECUTIVE SUMMARY

**What it is:** A physical tactical cooking manual for men — 50 standard operating procedures (SOPs) for cooking real food, written in military field-guide language. Every recipe is a mission. Every technique is a maneuver. Every tool is hardware.

**Why it wins:** No other cooking product combines hands-free counter utility (wire-O flip easel), kitchen-proof materials (waterproof synthetic paper), and a brand identity that speaks directly to men who find conventional cookbooks alienating. It is a premium gift product and a daily-use kitchen tool simultaneously.

**The product:**
- Format: Landscape wire-O flip easel (9.0" × 5.5" cover, 8.5" × 5.5" pages)
- 50 recipe SOPs across 4 mission categories
- 5-bank die-cut tab navigation (INTEL / QUICK / HEAVY / FIELD / SUPPLY)
- OD Green cover, silver wire-O binding, waterproof synthetic pages
- Full-color CMYK print

**Financials (V1.0 estimate — to be revised for wire-O format):**
- Retail: $55–$75
- Build cost: $25.50–$35.50 per unit (500-unit bulk)
- Target margin: 50–60%

**Current completion:** All 50 SOP files exist. Quality varies; ~20 are fully polished and production-ready. All infrastructure (style guide, design specs, tab system, marketing strategy) is complete.

**Mission for this phase:** Quality-audit and standardize all 50 SOPs, complete any thin content, fix 7 known critical errors, source AI photography, and produce a print-ready V2 layout.

---

## 2. PRODUCT DEFINITION

### 2.1 Physical Format

| Attribute | Spec |
|---|---|
| Binding | Wire-O coil, top-bound (pages flip back over the top, desk-calendar style) |
| Cover dimensions | 9.0" (W) × 5.5" (H) |
| Page dimensions | 8.5" (W) × 5.5" (H) |
| Cover material | 110pt chipboard, OD Green matte poly wrap |
| Stand | Back cover scored/folded as self-standing easel — hands-free counter use |
| Pages | Waterproof synthetic (REVLAR / YUPO / Rite in the Rain), 100–120lb cover weight |
| Print | Full-color CMYK, 240% TAC max for synthetic stock |
| Wire color | Silver/chrome |

> **⚠ Production_Specs.md (05_Logistics_Supply) is V1.0 and describes a 3-ring D-ring binder — it is superseded by this spec and the prototype (Prototype2.png). A revised RFQ and updated cost model for wire-O format is required.**

### 2.2 Page Layout (V2 — 3-Column Dashboard)

Per prototype (`04_Design_Assets/Production_Photos/Prototype2.png`):

```
┌──────────────────────────────────────────────────────────────────────┐
│  COOKING OPERATIONS          SOP-NNN: [MISSION NAME]                 │
├──────────────┬───────────────────────────────┬──────────────────────┤
│  INTEL       │  EXECUTION                    │  [HERO PHOTO]        │
│  ─────────── │  ──────────────────────────── │                      │
│  Rank: X     │  INFIL (Prep)                 │  (dish photo,        │
│  Time: X     │  1. Step                      │   high-contrast,     │
│  P/C/F/Cal   │  2. Step                      │   tactical style)    │
│              │                               │                      │
│  SUPPLIES    │  ENGAGEMENT (Cook)            │  NOTES / AAR         │
│  ─────────── │  3. Step                      │  ─────────────────── │
│  □ item      │  4. Step                      │  Field notes,        │
│  □ item      │                               │  substitutions,      │
│  □ item      │  EXFIL (Plate/Clean)          │  storage, Secondary  │
│              │  5. Step                      │  Objective           │
│              │                               │                      │
├──────────────┴───────────────────────────────┴──────────────────────┤
│  SUSTAINMENT OPERATIONS MANUAL // VOL 1: FOUNDATIONS  V2.0 RIFLEMAN │
└──────────────────────────────────────────────────────────────────────┘
```

### 2.3 Tab Navigation System

5-bank die-cut stagger system. Tabs are contained fully within the cover footprint — **tabs must not extend beyond the 9.0" outer cover edge.**

| Tab | Category | Page position (from top) | Color |
|-----|----------|--------------------------|-------|
| INTEL | Intelligence docs | 0.0"–1.0" | Coyote Tan |
| QUICK | Quick Strike SOPs | 1.1"–2.0" | Safety Orange |
| HEAVY | Heavy Lift SOPs | 2.1"–3.0" | Coyote Tan |
| FIELD | Field Rations SOPs | 3.1"–4.0" | Safety Orange |
| SUPPLY | Supply / Pantry | 4.1"–5.0" | Coyote Tan |

- Die-cut shifts down 1" every 10 SOPs creating the staircase visible effect
- Tab typography: vertical text, Stencilia or Roboto Mono Bold, black on tab color
- Source: `04_Design_Assets/Step_Tab_Layout_Guide.md`

### 2.4 Brand Identity

| Element | Spec |
|---|---|
| Primary colors | OD Green `#4B5320`, Coyote Tan `#A59C82`, Safety Orange `#FF6600`, Charcoal `#333333`, Stencil White `#F2F2F2` |
| Display font | Stencilia / Black Ops One (headlines, SOP titles) |
| Body font | Roboto Mono / Courier (body text) |
| Data font | DIN Condensed / Bahnschrift (stats, macros) |
| Iconography | `[!]` Danger, `[T]` Timing, `[R]` Rank, `[H]` Hardware |
| Photography | High-contrast, grain-forward, dark concrete surface, harsh directional lighting — no soft-focus food styling |
| Layout rules | Heavy black borders, redaction bars, SOP ID top-right corner, grid-based, no curves |

Full brand spec: `04_Design_Assets/Style_Guide.md`

### 2.5 Cover Design

- **Front cover (also serves as easel back):** OD Green chipboard
  - Left panel: "SUSTAINMENT / OPERATIONS / MANUAL" stacked, large
  - Bottom left: "V2.0 / RIFLEMAN ISSUE"
- **Section dividers:** Tab pages with full-bleed color per section (OD Green for INTEL, etc.)

---

## 3. CONTENT STATUS — ALL 50 SOPS

### 3.1 Status Key

| Symbol | Meaning |
|---|---|
| ✅ | Production-ready (fully written, format-compliant, reviewed) |
| ⚠ | Written but has a known critical error (see §4) |
| 🔍 | File exists — needs quality audit before production |
| ❌ | File confirmed thin/stub — full content write required |

### 3.2 Quick Strike (32 SOPs)

| ID | Mission Name | Rank | Time | Status |
|---|---|---|---|---|
| 001 | Operation Primal Sear (Steak) | Corporal* | 50m | ⚠ Rank fix needed |
| 002 | Operation Ground Combat (Bowl) | Recruit | 15m | ✅ |
| 005 | Operation Morning Recon (Eggs) | Recruit | 10m | ✅ |
| 006 | Operation Green Cover (Broccoli) | Recruit | 20m | ✅ |
| 008 | Operation Silver Scale (Salmon) | Sergeant | 15m | ⚠ Adhesion timing fix |
| 010 | Operation Iron Griddle (Burgers) | Sergeant | 15m | ✅ |
| 014 | Operation Coastal Infil (Tacos) | Recruit | 20m | ✅ |
| 015 | Operation Cold Payload (Salad) | Recruit | 10m | 🔍 |
| 018 | Operation Yogurt Armor (Cake) | Recruit | 45m | 🔍 |
| 020 | Operation Cornbread | Recruit | 30m | 🔍 |
| 021 | Operation Flaky Biscuit | Sergeant | 25m | 🔍 |
| 022 | Operation Whiteout (Sausage Gravy) | Recruit | 15m | 🔍 |
| 024 | Operation Mud-Bug (Etouffee) | Commander | 40m | 🔍 |
| 025 | Operation Coastal Extract (Shrimp) | Recruit | 15m | 🔍 |
| 026 | Operation Green Harvest (Zucchini) | Recruit | 1.2h | 🔍 |
| 027 | Operation Overripe Recovery (Banana) | Recruit | 1.1h | 🔍 |
| 029 | Operation Southern Comfort (Pudding) | Recruit | 20m | 🔍 |
| 030 | Operation Lean Strike (Pork) | Sergeant | 25m | 🔍 |
| 032 | Operation Starch Support (Mash) | Recruit | 30m | 🔍 |
| 033 | Operation Force Multiplier (Sauce) | Sergeant | 5m | 🔍 |
| 034 | Operation Green Perimeter (Beans) | Recruit | 10m | 🔍 |
| 035 | Operation Red Sauce (Pasta) | Recruit | 20m | 🔍 |
| 036 | Operation Liquid Fuel (Coffee) | Recruit | 10m | 🔍 |
| 037 | Operation Global Sear (Stir-Fry) | Sergeant | 20m | ⚠ Toss duration fix |
| 038 | Operation Aerial Assault (Wings) | Sergeant | 35m | ✅ |
| 039 | Operation Morning Stack (Pancakes) | Recruit | 20m | ⚠ Buttermilk math fix |
| 040 | Operation Tuber Load (Potato) | Recruit | 1h | ✅ |
| 042 | Operation Iron-Seared Thighs | Recruit | 35m | 🔍 |
| 043 | Operation Root Fortification | Recruit | 35m | ⚠ Missing Cal count |
| 046 | Operation Deep-Sea Recovery (Clams) | Sergeant | 20m | 🔍 |
| 047 | Operation High-Heat Curry | Recruit | 20m | ⚠ Protein timing fix |
| 048 | Hostage Rescue Beverages | Recruit | 5m | ✅ |

### 3.3 Heavy Lift (14 SOPs)

| ID | Mission Name | Rank | Time | Status |
|---|---|---|---|---|
| 003 | Operation Hostage Rescue (Tri-Tip) | Sergeant | 2h | ⚠ Ghost ingredients fix |
| 007 | Operation High-Value Bird (Chicken) | Sergeant | 1.2h | ✅ |
| 011 | Operation Overwatch Broth | Recruit | 12h | 🔍 |
| 013 | Operation Texas Black-Gold (Brisket) | Commander | 14h | ✅ |
| 016 | Operation Iron-Clad Chili | Sergeant | 3h | 🔍 |
| 017 | Operation Sweet Ransom (Flan) | Commander | 4h | 🔍 |
| 023 | Operation Delta Slow (Red Beans) | Sergeant | 6h | 🔍 |
| 028 | Operation Salvage Rations (Pudding) | Recruit | 1.5h | 🔍 |
| 031 | Operation Rack-and-File (Ribs) | Commander | 6h | 🔍 |
| 041 | Operation The Command Loaf | Sergeant | 1.2h | ⚠ Glaze-prep step fix |
| 044 | Operation Iberian Shore (Paella) | Commander | 1h | 🔍 |
| 045 | Operation Mediterranean Strike | Commander | 2.5h | 🔍 |
| 049 | Operation Prime Directive (Roast) | Commander | 5h | ✅ |
| 050 | Operation Eternal Simmer (Ragù) | Commander | 8h | ✅ |

### 3.4 Field Rations (4 SOPs)

| ID | Mission Name | Rank | Time | Status |
|---|---|---|---|---|
| 004 | Operation Bulk Sustainment (Pork) | Sergeant | 8h | ✅ |
| 009 | Operation Grain Silo (Rice) | Recruit | 25m | ✅ |
| 012 | Operation Oats and Ammo | Recruit | 5m | ✅ |
| 019 | Operation Daily Bread (No-Knead) | Sergeant | 18h | 🔍 |

### 3.5 Morale Boosters (1 SOP)

| ID | Mission Name | Rank | Time | Status |
|---|---|---|---|---|
| 048 | Hostage Rescue Beverages | Recruit | 5m | ✅ |

> **Note:** SOP-048 appears in both Quick Strike and Morale Boosters. Confirm final placement.

---

## 4. CRITICAL FIXES — PRE-PRODUCTION BLOCKERS

These 7 errors must be corrected before layout begins. Source: `EDITORIAL_EVALUATION.md`.

| # | SOP | Error | Fix |
|---|---|---|---|
| 1 | **SOP-039** | Buttermilk substitute math: produces 1 cup, recipe needs 2 cups | Change to: `2 tbsp lemon juice + 2 cups whole milk, wait 5 min` |
| 2 | **SOP-003** | Ghost ingredients: butter, garlic, thyme appear in Execution but not Supplies | Add to Supplies: `4 tbsp Unsalted Butter, 3 cloves Garlic (smashed), 2 sprigs Fresh Thyme` |
| 3 | **SOP-001** | Ranked Recruit; butter basting and pull-temp judgment are Corporal-level skills | Reclassify: Rank → Corporal, Difficulty → 3/5 |
| 4 | **SOP-047** | "Simmer 8–10 min with protein/veggies" — unclear whether protein goes in raw | Clarify step: specify whether protein is pre-cooked or raw, and add visual doneness cue |
| 5 | **SOP-037** | "Rapid toss" has no duration or visual cue | Add: `Rapid toss 3–4 min until vegetables show slight char at edges` |
| 6 | **SOP-008** | Adhesion timing not specified; cooks will force the fish | Add: `Do not move. After 4 min, attempt gentle release. If resistance, wait 60 sec more.` |
| 7 | **SOP-041** | Glaze prep missing from Infil phase; reader encounters it mid-Engagement | Add glaze-prep step to Infil: `Mix glaze ingredients in small bowl and set aside` |

**SOP-001 risk note:** Recruiting a Recruit with a steak as their first mission and having them fail due to misjudged difficulty is the single highest churn risk in the product. Fix this before any demo or marketing content is created.

---

## 5. STANDARDIZATION PASS

Apply uniformly across all 50 SOPs before layout:

### 5.1 Macro Block Format
Every SOP must use exactly this format — no exceptions:
```
P:Xg | C:Xg | F:Xg | ~XXX Cal
```
SOPs currently missing calories: SOP-037, SOP-043, SOP-047.

### 5.2 Rank & Difficulty Fields
Every SOP must include both:
```
Rank: [Private / Recruit / Corporal / Sergeant / Commander]
Difficulty: X/5
```
Rank-to-difficulty mapping:
| Rank | Difficulty |
|---|---|
| Private | 1/5 |
| Recruit | 2/5 |
| Corporal | 3/5 |
| Sergeant | 4/5 |
| Commander | 5/5 |

### 5.3 Secondary Objective Placement
Always placed in the **AAR section**. Remove any standalone post-Execution Secondary Objective blocks. This is the canonical location across all 50 SOPs.

### 5.4 Baking SOP Weight Additions
SOPs 039, 040, 041 — add gram weights in parentheses for all dry/liquid ingredients:
```
2 cups (240g) all-purpose flour
1 cup (240ml) buttermilk
```

### 5.5 Hardware Checklist Format
All tools listed with `[ ]` checkbox format:
```
[ ] 12" Cast iron skillet
[ ] Instant-read thermometer
```

---

## 6. AI PHOTOGRAPHY WORKFLOW

### 6.1 Tools
- **Primary:** Midjourney v6+ (best for high-contrast editorial food photography)
- **Alternatives:** Adobe Firefly (better commercial licensing), DALL-E 3

### 6.2 Master Style Prompt
```
Overhead tactical food shot, [dish name], high-contrast photography, 
grain-forward film aesthetic, dark concrete or slate surface, cast iron cookware, 
harsh single-direction lighting from upper-left, no soft focus, no lifestyle props, 
OD green color accent, desaturated with warm orange highlight on food surface, 
military field manual reference photo — 16:9 landscape crop
```

### 6.3 Priority Shot List (10 minimum before layout)

| Priority | SOP | Shot description |
|---|---|---|
| 1 | SOP-001 | Butter basting ribeye in cast iron — action shot, steam visible |
| 2 | SOP-013 | Brisket bark with probe thermometer reading 203°F — flat-lay |
| 3 | SOP-003 | Sliced tri-tip showing grain direction — arrow overlay acceptable |
| 4 | SOP-007 | Chicken thighs skin-side down in pan — pre-flip, skin rendering |
| 5 | SOP-039 | Pancake surface showing bubble stage — overhead, precise timing |
| 6 | SOP-031 | Rack of ribs cross-section showing smoke ring — Commander showpiece |
| 7 | SOP-002 | Assembled protein bowl overhead — ingredient separation visible |
| 8 | SOP-008 | Salmon fillet skin-side down — non-stick release moment |
| 9 | BRAND | Cast iron + thermometer + tactical cutting board — product hero shot |
| 10 | BRAND | Manual open on kitchen counter in easel position — product lifestyle |

### 6.4 Diagram Shots (Line Art)
SOP-007 (rib membrane removal) and SOP-003 (tri-tip grain direction) require line-art overlays. Generate base photo, then add arrows/labels in a vector tool (Illustrator, Figma, or Canva).

### 6.5 Photography Style Notes
- No plating garnishes (parsley, microgreens) — tactical realism only
- No white plates — dark surfaces, cast iron, sheet pans only
- Every image must read clearly at the 2.5"–3" column width of the V2 layout
- Grain/noise filter applied post-generation to unify AI-generated images

---

## 7. V2 FORMAT FINALIZATION

### 7.1 Source vs. Output
- **Content source:** `03_SOP_Recipes/` (V1 files — portrait format, fully written)
- **Production output:** `03_SOP_Recipes_V2/` (landscape 3-column — in progress)
- V1 files are authoritative for content; V2 files are the layout target

### 7.2 V2 Audit Checklist (per file)
For each of the 50 files in `03_SOP_Recipes_V2/`:
- [ ] "DATA PENDING" markers replaced with actual content
- [ ] Column 2 (Execution) populated with all 3 phases (Infil / Engagement / Exfil)
- [ ] Column 1 (Intel + Supplies) matches V1 source exactly
- [ ] Column 3 (Photo + AAR) has image placeholder at correct dimensions
- [ ] Header strip: "COOKING OPERATIONS" label present
- [ ] Footer: "SUSTAINMENT OPERATIONS MANUAL // VOL 1: FOUNDATIONS V2.0 RIFLEMAN ISSUE"

### 7.3 Long SOP Handling
SOPs-003, 007, and 013 have been flagged as potentially exceeding one landscape spread. Decision required:
- **Option A:** Two-page spread (fold-out or consecutive pages) — premium feel, complex print
- **Option B:** Compressed field-card format — tighter margins, smaller type, fits one page
- **Option C:** Remove AAR and move to companion reference card

Recommend **Option B** for 003 and 007; **Option A** for 013 (brisket justifies the full treatment as a Commander-level showpiece).

---

## 8. DISTRIBUTION STRATEGY

### 8.1 Primary Channel — Kickstarter → Shopify DTC

**Phase 1: Kickstarter (demand validation + print-run funding)**

| Tier | Contents | Price |
|---|---|---|
| Digital Operator | PDF edition (same V2 layout) | $20 |
| Field Manual | Physical wire-O flip easel | $65 |
| Vanguard Kit | Physical manual + morale patch + sticker pack | $85 |
| Unit Commander | 3 manuals (gift set) | $175 |

- Campaign goal: fund minimum 500-unit print run (~$17,750 at build midpoint)
- Lead with SOP-001 and SOP-013 as demo SOPs in the campaign video
- "Mission Leak" PDF (3 free SOPs) as pre-launch email capture lead magnet

**Phase 2: Shopify DTC (post-campaign, ongoing)**
- 60–70% margin vs. 30% on Amazon
- Insert card in every physical unit drives customers to email list for warranty and Vol 2 access
- Bundle upsells: Manual + Lodge Cast Iron skillet affiliate link, Manual + Meater thermometer

### 8.2 AAFES — Military Base Exchanges

**Channel:** Army & Air Force Exchange Service — on-base retail worldwide  
**Why:** Captive audience with brand cultural alignment, disposable income, no Amazon algorithm dependency  
**Requirements:**
- UPC barcode: Register via GS1 US ($250 one-time + annual fee) — do this before any retail channel
- AAFES Supplier portal application: aafes.com/vendor-information/
- Minimum order: ~50–100 units (confirm with AAFES rep)
- Lead time post-approval: 3–6 months
- Pricing to AAFES: ~$35–40 (50% of retail, standard wholesale margin)

**Action items:**
- [ ] Register GS1 barcode immediately (required for AAFES and Amazon)
- [ ] Submit AAFES vendor application after first Kickstarter fulfillment
- [ ] Request an intro call with AAFES buyer for Men's Gift / Lifestyle category

### 8.3 Amazon FBA (post-Kickstarter, secondary)

- Use primarily as a discovery engine and review aggregator
- Target Best Seller tag in Men's Cooking and Home Reference categories
- Drive discovered customers back to Shopify via insert card
- Do not run Amazon ads until 25+ reviews accumulated

### 8.4 Wholesale — Phase 2

- Cabela's, Bass Pro Shops, tactical supply stores
- Requires a distributor relationship or direct outreach with a line sheet
- Minimum viable: 5-page PDF line sheet with retail pricing, margin, and product photos
- Not a priority until post-Kickstarter with proven demand

---

## 9. DIGITAL / PDF STRATEGY

### 9.1 PDF Edition
- Same V2 3-column layout exported as print-ready PDF
- Kickstarter digital tier: $20 (zero fulfillment cost, 100% margin)
- Post-launch standalone: $29 on Gumroad and Shopify
- Potential upgrade: interactive PDF with clickable cross-references between SOPs (e.g., SOP-001 links to SOP-032 Mashed Potatoes as a Compatible System)

### 9.2 "Mission Leak" Lead Magnet
- 3-SOP sampler PDF (recommended: SOP-001, SOP-002, SOP-013 — beginner, quick, showpiece)
- Gate behind email signup on pre-launch landing page
- Drives the Kickstarter email list before campaign goes live

### 9.3 Future Digital Products
- Vol 2: Flame & Steel digital-first release ahead of print
- Monthly "Field Dispatch" — one new SOP PDF per month, email subscriber exclusive
- QR codes in physical manual linking to technique videos (future)

---

## 10. COMMUNITY BUILDING PLAN

### 10.1 Pre-Launch (now → Kickstarter launch)

| Channel | Action |
|---|---|
| Email list ("The Unit") | Carrd.co landing page with Mission Leak PDF lead magnet |
| Reddit | Post SOP-001 and SOP-013 in r/MealPrepSunday, r/steak, r/slowcooking — organic, no spam |
| Instagram | "Operation [Name]" 60-second cook videos; 3 posts/week |
| TikTok | Same content repurposed; lean into the "men learning to cook" narrative |

### 10.2 During Kickstarter

- Daily backer updates in military briefing format ("Day 3 Sitrep: 47% funded")
- Unlock stretch goals as new SOP drops ("If we hit $20K, I'll write SOP-044 Paella live on stream")
- Backer exclusive: access to Discord "Field HQ" server

### 10.3 Post-Launch

- **Discord "Field HQ":** Open after Kickstarter closes. Channels: #mission-reports (share your cooks), #intel-drop (tips), #after-action (failures/lessons). Moderate with brand voice.
- **Weekly Brief:** Email newsletter, one recipe tip per week in mission-brief format. Tease Vol 2 SOPs.
- **Review push:** Email all Kickstarter backers at 30-day post-delivery asking for Amazon review. Include a "Review Mission" card in packaging.

---

## 11. VOLUME ROADMAP

| Volume | Title | Focus | SOPs | Status |
|---|---|---|---|---|
| Vol 1 | Foundations | Core techniques, everyday cooking | 50 | Current — pre-production |
| Vol 2 | Flame & Steel | Grilling, smoking, live-fire cooking | 40–50 | Begin TOD after Vol 1 launch |
| Vol 3 | Deep Freeze | Meal prep, bulk freeze, cold-chain logistics | 40–50 | 12 months post-launch |

### Vol 2 Prep Actions
- Begin Table of Distribution for Flame & Steel immediately after Vol 1 Kickstarter closes
- Kickstarter backers get "Vanguard Access" to 3 Vol 2 preview SOPs as a thank-you
- Vol 2 Kickstarter targets existing Vol 1 customer list — near-zero acquisition cost

### Vol 3 Notes
- Deep Freeze is the natural companion to Field Rations
- Strong opportunity for a "The Unit Meal Prep" angle (cooking for a family in tactical bulk batches)

---

## 12. MISSING INFRASTRUCTURE FILES

These files are referenced in the project but do not exist or are stub-only:

| File | Location | Priority | Action |
|---|---|---|---|
| `Pantry_Inventory_SOP.md` | `01_Intelligence/` | High | Referenced in `Weekly_Battle_Rhythm.md` — write a full inventory SOP |
| Photography shot list | `04_Design_Assets/` | High | Detailed shot list per §6.3 above |
| Kickstarter campaign copy | `06_Marketing_Comms/` | High | Headline, body, tier descriptions, FAQ |
| GS1 barcode registration checklist | `05_Logistics_Supply/` | High | Required before any retail channel |
| Updated RFQ (wire-O format) | `05_Logistics_Supply/` | High | Existing RFQ targets 3-ring binder — needs revision |
| Email templates | `06_Marketing_Comms/` | Medium | Vanguard Day, Public Day, 30-day Review Push |
| AAFES vendor application checklist | `06_Marketing_Comms/` | Medium | Step-by-step vendor portal walkthrough |
| Vol 2 Table of Distribution | Root | Low | Draft after Vol 1 launch |

---

## 13. OPEN PRODUCTION QUESTIONS

These require decisions before sending to printer:

| Question | Options | Recommendation |
|---|---|---|
| Exact trim size | 8.5"×5.5" or 10"×6.5" | Confirm from printer; 8.5"×5.5" matches style guide |
| Wire-O gauge & pitch | 3:1 or 2:1 pitch; silver chrome | 3:1 for thinner books (<100 pages), confirm with printer |
| Back panel stand engineering | Scored fold, kickstand, or built-in easel | Scored fold per prototype — get exact score placement from prototype measurement |
| Wire-O vs. 3-ring update packs | Wire-O cannot be updated like 3-ring | Accept this tradeoff; position new volumes as the "update" mechanism |
| Long SOP handling (003, 007, 013) | 2-page spread vs. compressed | 013 gets 2-page; 003 and 007 get compressed format |
| Synthetic paper cost | REVLAR vs. laminated cardstock | Test both; laminated 100lb matte cardstock is 30% cheaper if synthetic is cost-prohibitive |

---

## 14. LAUNCH READINESS CHECKLIST

### Content
- [ ] All 50 SOPs quality-audited (thin content identified and completed)
- [ ] All 7 critical fixes applied (§4)
- [ ] All 50 SOPs standardized: macro block, rank+difficulty, Secondary Objective in AAR, checkbox hardware format (§5)
- [ ] Baking SOPs (039, 040, 041) have gram weights

### Photography
- [ ] 10 minimum hero images generated and style-matched (§6)
- [ ] Diagram overlays completed for SOP-003 and SOP-007
- [ ] Brand hero shots (product open on counter, hardware flat-lay)

### Layout
- [ ] All 50 V2 files audited — DATA PENDING markers cleared
- [ ] Long SOPs (003, 007, 013) handled with confirmed format decision
- [ ] Print-ready PDF exported (CMYK, 240% TAC, 0.5pt min line weight)

### Production
- [ ] Wire-O format RFQ submitted to printer (PrintNinja or equivalent)
- [ ] Back panel easel engineering confirmed with manufacturer
- [ ] GS1 barcode registered
- [ ] 500-unit minimum order confirmed with unit cost

### Launch
- [ ] Mission Leak PDF created (3 SOPs)
- [ ] Pre-launch landing page live (Carrd.co) with email capture
- [ ] Kickstarter page copy written and reviewed
- [ ] Kickstarter campaign video scripted (features SOP-001 and SOP-013)
- [ ] AAFES vendor application submitted (post-Kickstarter fulfillment)
- [ ] Shopify store set up for DTC post-campaign

---

## 15. KEY FILE INDEX

| File | Purpose |
|---|---|
| `00_Table_of_Distribution.md` | Master index of all 50 SOPs |
| `03_SOP_Recipes/SOP_TEMPLATE.md` | Mandatory 5-section format for all SOPs |
| `04_Design_Assets/Style_Guide.md` | Brand spec (colors, fonts, photography, layout rules) |
| `04_Design_Assets/Step_Tab_Layout_Guide.md` | Die-cut tab engineering dimensions |
| `04_Design_Assets/Production_Photos/Prototype2.png` | Physical prototype reference (wire-O flip easel) |
| `05_Logistics_Supply/Production_Specs.md` | V1.0 cost model ⚠ outdated — update for wire-O |
| `06_Marketing_Comms/Launch_Strategy.md` | 5-phase deployment plan |
| `EDITORIAL_EVALUATION.md` | Manuscript critique and critical fix punch-list |
| `MISSION_CONTROL.txt` | V2.0 project status briefing |

---

*End of Spec — SUSTAINMENT OPERATIONS MANUAL Vol. 1: Foundations*  
*Next action: Quality audit pass on all 50 SOPs, beginning with ⚠ flagged files.*
