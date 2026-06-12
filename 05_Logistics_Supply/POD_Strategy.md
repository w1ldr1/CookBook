# POD DISTRIBUTION STRATEGY
**Document Type:** Production & Distribution Reference  
**Version:** 1.0  
**Replaces:** `Production_Specs.md` (V1 binder model — archived, not deleted)  
**Status:** ACTIVE

---

## OVERVIEW

The Sustainment Operations Manual series uses a **print-on-demand (POD) model** for initial
distribution. The customer orders online, the POD publisher prints and ships directly to the
customer. No inventory is held. Setup cost is $0.

This model serves as market validation before committing capital to the premium custom wire-O
easel product (see `Production_Specs.md` for that spec when the time comes).

---

## PLATFORM 1 — Amazon KDP (Primary)

**URL:** kdp.amazon.com  
**Setup cost:** $0  
**Purpose:** Maximum Amazon reach and organic discovery. KDP lists automatically on Amazon.com.

### Specifications

| Attribute | Value |
|---|---|
| Binding | Perfect-bound softcover |
| Trim size | 7"×10" (standard cookbook format) OR 8.5"×11" |
| Interior | Black & white |
| Cover | Full color, glossy |
| Bleed | 0.125" on all sides |
| Margins | Inside: 0.75", Outside: 0.5", Top/Bottom: 0.75" |
| Resolution | 300 DPI minimum |
| Color profile | RGB for KDP (KDP handles conversion) |
| File format | PDF (interior) + PDF (cover, includes bleed) |

### Pricing model

| Variable | Value |
|---|---|
| Retail price | $24.99 |
| KDP printing cost (~150 pages B&W, 7×10) | ~$4.45 |
| Royalty rate | 60% of (retail − printing cost) |
| **Royalty per book** | **~$12.32** |

Royalty calculator: kdp.amazon.com/en_US/help/topic/G201834340

### Setup steps

1. Create an Amazon KDP account at kdp.amazon.com
2. Click "Create" → "Paperback"
3. Enter title, subtitle, author name, description, keywords
4. ISBN: KDP provides a free ISBN for KDP-published titles (or purchase your own via myidentifiers.com for $125 if you want full control)
5. Upload interior PDF and cover PDF
6. Set pricing: $24.99 USD; check "Expanded Distribution" for additional retail channels (reduces royalty slightly)
7. Submit for review — KDP approval typically takes 24–72 hours
8. Book appears on Amazon.com automatically upon approval

### Amazon listing optimization

- **Title:** "Sustainment Operations Manual — Army Edition: 50 Tactical Recipes for Men Who Cook with a Mission"
- **Keywords (7 max):** men's cookbook, military cookbook, tactical cooking, paleo recipes for men, field cooking guide, men who cook, gifts for veterans
- **Categories:** Books > Cookbooks, Food & Wine > Cooking by Ingredient > Meat > Beef; AND Books > Humor & Entertainment > Gifts
- **Description:** Use the "men find conventional cookbooks alienating" hook + the 50 SOP structure + the tactical brand identity. Mirror the landing page copy.
- **Author Central profile:** Set up at author.amazon.com — add author bio, photo, link to the series

---

## PLATFORM 2 — Lulu (Secondary, coil-bound option)

**URL:** lulu.com  
**Setup cost:** $0  
**Purpose:** "Lies flat while cooking" coil-bound format. Premium option alongside the KDP version.

### Before starting: Verify coil-bound trim size

Lulu's coil-bound product offerings change periodically. Before designing the interior for Lulu:
1. Go to lulu.com → Create a Book → select Coil-bound
2. Confirm that your target trim size is available (recommended: 8.5"×11" or 8×10")
3. Download Lulu's print guidelines PDF for that size — use those exact margin specs

### Specifications (subject to Lulu's current offerings)

| Attribute | Value |
|---|---|
| Binding | Coil-bound (spiral) |
| Trim size | 8.5"×11" (confirm availability first) |
| Interior | Black & white |
| Cover | Full color |
| Bleed | Per Lulu's current spec (download their template) |
| Resolution | 300 DPI minimum |
| Color profile | CMYK recommended for Lulu |
| File format | PDF |

### Pricing model

| Variable | Value |
|---|---|
| Retail price | $29.99 |
| Lulu printing cost (estimated ~150 pages B&W coil, 8.5×11) | ~$12–16 |
| Royalty rate | Lulu retains ~20%; remainder is your royalty |
| **Royalty per book (estimate)** | **~$10–15** |

Use Lulu's pricing calculator at lulu.com to get the exact current printing cost before setting
the final retail price. Adjust retail price to ensure minimum $8 royalty.

### Lulu Global Reach distribution

Lulu can distribute to Amazon and other booksellers via "Global Reach":
- Requires an ISBN (Lulu provides one free, or use your own)
- Takes 2–6 weeks to activate
- Amazon listing via Lulu will appear separately from the KDP listing (different ASIN, different
  format — this is fine, they serve different buyers)

### Setup steps

1. Create Lulu account at lulu.com
2. Click "Create" → "Book" → select Coil-bound
3. Select the confirmed trim size
4. Upload interior PDF and cover PDF
5. Set price using Lulu's calculator — target $29.99 retail
6. Enable Lulu storefront distribution (immediate)
7. Enable Global Reach for Amazon distribution (requires ISBN — allow 2–6 weeks)
8. **Order 1 author proof copy** (~$10–15) before making the listing public
9. Review physical proof — check coil function, print quality, readability — then approve for sale

---

## PLATFORM 3 — Gumroad (Digital Edition)

**URL:** gumroad.com  
**Setup cost:** $0 (Gumroad takes 10% per sale)  
**Purpose:** Digital PDF edition + free Mission Leak sampler for email capture.

### Products to set up

| Product | Price | Description |
|---|---|---|
| Digital Edition — Army | $14.99 | Full 50-SOP PDF, same layout as print interior |
| Mission Leak Sampler | FREE | SOP-001 + SOP-002 + SOP-013 — 3 SOPs gated behind email signup |

### Setup steps

1. Create Gumroad account at gumroad.com (free)
2. Upload the digital edition PDF → set price $14.99
3. Upload the Mission Leak 3-SOP sampler PDF → set to "pay what you want" with $0 minimum → enable "require email" — this captures the email for the mailing list
4. Add product links to the landing page (index.html)
5. Configure email integration: connect Gumroad to a free email service (Mailchimp free tier: up to 500 contacts, or ConvertKit free: up to 1,000)

---

## MULTI-EDITION WORKFLOW

Each branch edition is a new product on each platform. The process per new edition:

| Step | Task | Time | Cost |
|---|---|---|---|
| 1 | New cover design in Canva | 30–60 min | $0 |
| 2 | Commander's Intent foreword page | 60–90 min | $0 |
| 3 | Color swap in layout template (master pages) | 15–20 min | $0 |
| 4 | Export interior PDF + cover PDF | 10 min | $0 |
| 5 | New KDP project + upload | 20–30 min | $0 |
| 6 | New Lulu project + upload + order proof | 20–30 min + ~$12 proof |
| 7 | New Gumroad product (same PDF) | 10 min | $0 |
| **Total per edition** | | **~3 hours** | **~$12 (proof copy)** |

---

## FUTURE: PREMIUM WIRE-O EASEL

The original premium product spec is documented in `05_Logistics_Supply/Production_Specs.md`.
That product — landscape wire-O flip easel, die-cut tabs, waterproof synthetic paper — is a
strong long-term play.

**Trigger:** When POD sales + email list reaches 500+ customers, reactivate the Kickstarter
campaign (`06_Marketing_Comms/Kickstarter_Deployment.md` is already written). The POD customer
base is the audience for that campaign.

**AAFES (military base exchanges):** Also belongs to this phase. Requires:
- Physical inventory (not compatible with pure POD model)
- GS1 UPC barcode registration ($250 one-time + annual fee via gs1us.org)
- AAFES vendor application at aafes.com/vendor-information/
- Minimum order quantity confirmation with AAFES buyer

---

*End of POD Strategy v1.0*
