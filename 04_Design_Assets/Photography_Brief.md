# PHOTOGRAPHY BRIEF: SUSTAINMENT OPERATIONS MANUAL
**Subject:** AI-Generated Hero Image Production — Volume 1 Foundations
**Objective:** Produce a minimum of 10 publication-ready hero images for SOP page layouts and marketing.

---

## 1. VISUAL DOCTRINE

Every image must read as a **tool photograph, not a food photo.** The reference aesthetic is 1960s–1980s U.S. Army field manuals crossed with a modern equipment catalog. No lifestyle props. No soft focus. No garnishes. No napkins.

**The test:** If the image could appear in a Williams-Sonoma catalog, it fails. If it looks like it belongs in a technical manual, it passes.

---

## 2. MASTER STYLE PROMPT

Use this block as the foundation for every Midjourney prompt. Append the shot-specific details from Section 4.

```
[SHOT-SPECIFIC DESCRIPTION], overhead tactical angle, high-contrast lighting,
harsh directional key light from upper-left at 45 degrees, deep shadows,
matte black or dark concrete surface, no tablecloth,
cast iron or carbon steel cookware, military field guide aesthetic,
desaturated color grade with warm orange highlight preservation,
no soft focus, no bokeh, grain-forward film emulation,
no decorative props, no garnish sprigs, no napkins,
OD Green accent element where possible, shot on 35mm film —ar 3:2
```

**Midjourney parameters to append:**
- `--style raw` — disables Midjourney's beautification
- `--chaos 10` — slight variation between generations
- `--no flowers, napkins, tablecloth, soft focus, bokeh, garnish` — hard exclusions

**Platform (free options first):**
- **DALL-E 3** — free via ChatGPT (chatgpt.com); good prompt adherence; use for drafts and secondary shots
- **Adobe Firefly** — free tier (firefly.adobe.com); best commercial licensing; good clean editorial output
- **Canva AI** — free tier; lower detail; usable for background/brand shots
- **Midjourney** — paid ($10/mo); highest quality for the grain-forward tactical aesthetic; recommended for the 10 priority hero shots

---

## 3. TECHNICAL SPECS

| Parameter | Specification |
|-----------|---------------|
| Aspect ratio | 3:2 landscape (for SOP right column) |
| Resolution | 1800×1200px minimum |
| Color mode | RGB (convert to CMYK at layout stage) |
| File format | PNG or TIFF, no JPEG compression |
| Grain | Light grain overlay acceptable — no noise |
| Color grade | Desaturated base, preserve warm food tones |

---

## 4. PRIORITY SHOT LIST (10 Minimum Before Layout)

### SHOT 01 — SOP-001: Primal Sear (Butter Basting Action)
**SOP:** SOP-001-Primal-Sear.md
**Scene:** A ribeye steak in a cast iron skillet, actively being basted. A large spoon is mid-scoop, carrying amber clarified butter with visible foam. The steak has a deep mahogany crust — Maillard browning is the hero, not red meat.

**Midjourney prompt:**
```
A thick ribeye steak in a black cast iron skillet being basted with a large spoon,
molten amber butter with white foam visible on the spoon mid-pour,
deep mahogany sear crust on the steak, smoke wisps rising,
overhead tactical angle, high-contrast lighting, harsh directional key light from upper-left at 45 degrees,
deep shadows, matte black surface, military field guide aesthetic,
desaturated color grade with warm orange highlight preservation,
no soft focus, grain-forward film emulation, no decorative props --ar 3:2 --style raw --chaos 10
--no flowers, napkins, tablecloth, soft focus, bokeh, garnish, herbs on top
```

---

### SHOT 02 — SOP-003: Tri-Tip Grain Direction Diagram
**SOP:** SOP-003-Operation-Hostage-Rescue.md
**Scene:** A sliced tri-tip on a dark cutting board. One half is sliced WITH the grain (long, stringy fibers visible); the other half sliced AGAINST the grain (short, clean cross-sections). A tactical ruler or simple white line overlay marks the grain direction. This is a **diagram image** — clarity over mood.

**Midjourney prompt:**
```
A sliced tri-tip roast on a dark matte cutting board, two sections visible —
one sliced with the grain showing long stringy muscle fibers,
one sliced against the grain showing clean short cross-sections,
flat-lay overhead shot, harsh even lighting to maximize fiber texture detail,
tactical cutting board, matte black surface, military field guide aesthetic,
high-contrast desaturated with warm meat tone preservation,
no garnish, no props, technical document style --ar 3:2 --style raw --chaos 5
--no flowers, napkins, soft focus, bokeh, garnish
```
**Post-production note:** Add white arrow overlay with "CUT DIRECTION" label in Roboto Mono at layout stage.

---

### SHOT 03 — SOP-007: Spatchcock Bird (Pre-Cook)
**SOP:** SOP-007-Operation-High-Value-Bird.md
**Scene:** A whole chicken, backbone removed and flattened (spatchcocked), pressed flat on a dark sheet pan. The structure should be clearly visible — wings out, bird flat. No seasoning hiding the geometry.

**Midjourney prompt:**
```
A raw whole chicken with backbone removed, pressed completely flat spatchcock style,
top-down overhead view on a dark matte rimmed sheet pan,
pale raw skin stretched flat showing the opened spine area,
high contrast even lighting to show the structural geometry clearly,
dark concrete surface, military field guide aesthetic,
desaturated with natural meat tones preserved,
technical diagram style, no garnish, no seasoning visible --ar 3:2 --style raw --chaos 5
--no flowers, herbs on top, garnish, soft focus, bokeh, tablecloth
```

---

### SHOT 04 — SOP-013: Brisket Bark (Probe Thermometer Flat-Lay)
**SOP:** SOP-013-Operation-Texas-Black-Gold.md
**Scene:** A sliced brisket flat-lay. The black bark crust is the hero. A digital probe thermometer is inserted into the point, reading ~203°F on its display. The smoke ring is visible in the cross-section.

**Midjourney prompt:**
```
A thick cross-section of smoked beef brisket flat-lay on dark slate surface,
jet black bark crust on the exterior, deep red smoke ring visible inside,
a stainless steel digital probe thermometer inserted into the meat reading 203°F on its display,
overhead tactical shot, high-contrast harsh directional lighting,
matte dark surface, military field guide aesthetic,
desaturated color grade with warm orange and red meat tone preservation,
no garnish, no BBQ sauce on top, no props --ar 3:2 --style raw --chaos 10
--no flowers, napkins, tablecloth, soft focus, bokeh, garnish, sauce poured over
```

---

### SHOT 05 — SOP-039: Pancake Bubble Stage
**SOP:** SOP-039-Operation-Morning-Stack.md
**Scene:** A single pancake in a cast iron griddle or flat skillet, viewed from a low angle (not overhead). The batter surface shows active bubbling — the bubbles have formed but NOT yet popped, indicating the exact moment to flip. The edges are just beginning to set.

**Midjourney prompt:**
```
A single pancake cooking in a matte black cast iron griddle, viewed from a low 20-degree angle,
batter surface showing dozens of active bubbles just formed but not yet popped,
edges beginning to turn matte and set while center still wet,
harsh side lighting to cast shadows inside the bubbles and show surface texture,
dark matte surface, military field guide aesthetic,
high-contrast, desaturated with warm golden batter tones preserved,
no toppings, no syrup, no butter on top --ar 3:2 --style raw --chaos 10
--no flowers, napkins, garnish, soft focus, bokeh, toppings
```
**Post-production note:** This is a timing diagram. Consider a white arrow overlay labeling "FLIP POINT" at layout.

---

### SHOT 06 — SOP-002: Ground Combat Bowl (Overhead)
**SOP:** SOP-002-Ground-Combat-Bowl.md
**Scene:** An overhead shot of a ground beef rice bowl in a dark military-style mess tin or deep enamel bowl. Rice base, ground beef on top, minimal garnish (maybe chopped green onion only). The composition should read as "fuel," not "food styling."

**Midjourney prompt:**
```
Overhead shot of a ground beef rice bowl in a matte black military mess tin,
white jasmine rice base topped with seasoned browned ground beef,
tiny amount of sliced green onion only as the single topping,
harsh directional lighting from above-left, deep shadows on the far edge of the bowl,
dark concrete surface, military field guide aesthetic,
desaturated color grade, warm food tones preserved,
no garnish sprigs, no sauce drizzle, no lifestyle props --ar 3:2 --style raw --chaos 10
--no flowers, napkins, tablecloth, soft focus, bokeh, decorative garnish
```

---

### SHOT 07 — SOP-005/006: Chicken Thigh Sear (Action)
**SOP:** SOP-005-Operation-Morning-Recon.md / SOP-006-Operation-Green-Cover.md
**Scene:** Chicken thighs skin-side down in a cast iron skillet, actively searing. Visible fat rendering and spattering. Deep golden skin starting to crisp at the edges. A pair of tongs holds one thigh, hovering just above the pan.

**Midjourney prompt:**
```
Three chicken thighs skin-side down in a black cast iron skillet, active searing,
rendered golden fat pooling and spattering in the pan,
tongs gripping one thigh, the skin deeply browned and crisping at edges,
harsh top-down 45-degree angle, high-contrast lighting,
dark concrete surface, military field guide aesthetic,
desaturated with warm golden-brown skin tone preserved,
no garnish, no sauce, no props beside the pan --ar 3:2 --style raw --chaos 10
--no flowers, napkins, tablecloth, soft focus, bokeh, garnish, herbs
```

---

### SHOT 08 — SOP-010: Pasta Finish (Sauce Cling)
**SOP:** SOP-010-Operation-Iron-Griddle.md
**Scene:** Pasta being tossed in a skillet — the moment of emulsification. Tongs lift a nest of pasta, and the sauce clings to the strands in a glossy sheen. Sauce visible in the pan below.

**Midjourney prompt:**
```
Tongs lifting a nest of pasta from a stainless steel skillet, the pasta coated in glossy clinging sauce,
sauce visible pooling in the pan below, emulsified and silky not oily,
high-contrast overhead-angle shot, harsh directional lighting,
dark matte surface, military field guide aesthetic,
desaturated color grade with warm pasta and sauce tones preserved,
no garnish on top, no parmesan shaved over, no props --ar 3:2 --style raw --chaos 10
--no flowers, napkins, tablecloth, soft focus, bokeh, garnish
```

---

### SHOT 09 — BRAND HERO: Cast Iron + Thermometer + Cutting Board
**SOP:** N/A — product brand shot
**Scene:** A flat-lay "equipment still life" — cast iron skillet, digital probe thermometer, tactical cutting board, and tongs arranged on a dark concrete surface. This is the product/brand hero for the Kickstarter, social media, and book cover reference. No food.

**Midjourney prompt:**
```
Flat-lay overhead arrangement of a matte black cast iron skillet,
a stainless steel digital probe thermometer,
a dark wood or black composite cutting board,
and a pair of stainless tongs,
all arranged on dark concrete, military field equipment arrangement style,
harsh even lighting with no shadows obscuring tools,
military field guide aesthetic, technical catalog style,
desaturated high-contrast, OD Green or Coyote Tan surface optional,
no food, no seasoning, no props --ar 3:2 --style raw --chaos 5
--no flowers, food, napkins, tablecloth, garnish, soft focus, bokeh
```

---

### SHOT 10 — BRAND HERO: Manual Open on Counter (Lifestyle)
**SOP:** N/A — product lifestyle shot
**Scene:** The physical binder standing open on a kitchen counter in easel mode. A cast iron skillet visible in the background (blurred or sharp — tactical style means sharp). A man's forearm or hand visible reading the page, nothing else of the person visible.

**Midjourney prompt:**
```
A tactical green military-style wire-bound flip manual standing open in easel position on a dark kitchen counter,
OD green cover, a man's forearm visible reaching toward it,
a black cast iron skillet in the background slightly out of focus,
product photography style but with military field guide aesthetic,
harsh directional lighting from the left, dark matte granite counter surface,
desaturated color grade with OD green cover fully saturated,
no lifestyle props, no food on the counter, no decorative items --ar 3:2 --style raw --chaos 10
--no flowers, napkins, garnish, soft focus, bokeh
```

---

## 5. SECONDARY SHOTS (Post-Launch Priority)

These are not required before launch but should be produced for Vol. 1 upgrades and marketing:

| Priority | SOP | Subject |
|----------|-----|---------|
| 11 | SOP-007 | Membrane removal diagram on raw ribs — line art overlay required |
| 12 | SOP-049 | Prime rib cross-section showing no grey ring |
| 13 | SOP-050 | Dutch oven of Sunday sauce from above, wooden spoon submerged |
| 14 | SOP-016 | Dark chili in cast iron pot, top-down, surface texture focus |
| 15 | SOP-019 | No-knead bread loaf being torn open, steam visible |
| 16 | SOP-048 | Old Fashioned cocktail with large ice cube, overhead, dark background |
| 17 | SOP-044 | Spatchcocked chicken + roasted tomatoes on a dark sheet pan |
| 18 | SOP-031 | Rack of ribs with bark, flat-lay, sliced |
| 19 | SOP-023 | Pulled pork shredded with two forks in Dutch oven |
| 20 | SOP-046 | Linguine with clams in skillet, tongs lifting a clam |

---

## 6. IMAGE STORAGE & NAMING

Place all generated images in: `04_Design_Assets/Images/`

File naming convention: `SOP-NNN-[Codename]-Hero.png`

Brand shots: `Brand-Hero-Equipment.png`, `Brand-Hero-Manual.png`

---

## 7. POST-PRODUCTION CHECKLIST

For each image before layout placement:
- [ ] Resize to 1800×1200px minimum
- [ ] Convert to CMYK (layout software stage)
- [ ] Confirm no visible soft-focus blur in key subject area
- [ ] Confirm no lifestyle props are visible
- [ ] Confirm food tones are warm (not blue-shifted)
- [ ] Add grain overlay if not already present (5–8% Overlay layer in Photoshop)
- [ ] Test at print scale: 3"×2" at 300dpi — detail must hold

---

**Brief Version:** 1.0
**Last Updated:** 2026-05-24
**Status:** Ready for AI generation
