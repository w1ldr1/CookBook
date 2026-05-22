import os
import re

# CONFIG
BASE_DIR = r'Z:\Terminal\Projects\CookBook'
SOURCE_DIR = os.path.join(BASE_DIR, '03_SOP_Recipes')
OUTPUT_DIR = os.path.join(BASE_DIR, '03_SOP_Recipes_V2')

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def safe_search(pattern, text, default="DATA PENDING"):
    match = re.search(pattern, text, re.MULTILINE | re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return default

def extract_section(text, start_marker, end_marker):
    # Flexible matching for headers
    pattern = f"{re.escape(start_marker)}.*?\n(.*?)(?=\n##|$)"
    match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return "SECTION PENDING"

def refactor_to_v2(filename, content):
    # 1. Extract Metadata with Safe Search
    title = safe_search(r"^# (.*?)$", content, default=filename)
    rank = safe_search(r"\*\*Rank:\*\* (.*?)$", content)
    # Search for Time (handles "Total Mission Time" or just "Time")
    time = safe_search(r"Time:\*\* (.*?)$", content)
    # Search for Macros
    macros = safe_search(r"Macros.*?\*\* (.*?)$", content)
    
    # 2. Extract Sections
    # We use numbering-only search to be more robust
    hardware = extract_section(content, "2. HARDWARE", "3. SUPPLIES")
    supplies = extract_section(content, "3. SUPPLIES", "4. EXECUTION")
    execution = extract_section(content, "4. EXECUTION", "5. AFTER ACTION REPORT")
    aar = extract_section(content, "5. AFTER ACTION REPORT", "---")
    
    # 3. Template for V2 Landscape (Dashboard Layout)
    v2_template = f"""# {title}
**Rank:** {rank} | **Time:** {time} | **Macros:** {macros}
**V2.0 RIFLEMAN ISSUE // VOL 1: FOUNDATIONS**

---
## [ COLUMN 1: INTEL & SUPPLIES ]
### HARDWARE
{hardware}

### SUPPLIES
{supplies}

---
## [ COLUMN 2: EXECUTION ]
{execution}

---
## [ COLUMN 3: VISUAL & AAR ]
### FIELD INTEL & OBJECTIVES
{aar}

![{title} Hero Image](../../04_Design_Assets/Images/{filename.replace('.md', '.jpg')})
---
"""
    return v2_template

# RUN PROCESS
print("="*60)
print("REFACTORING MISSION: V1.0 -> V2.0 RIFLEMAN ISSUE")
print("="*60)

for root, dirs, files in os.walk(SOURCE_DIR):
    # Skip the V2 folder itself if it's inside source
    if '03_SOP_Recipes_V2' in root:
        continue
        
    for file in files:
        # Only process original SOP files
        if file.endswith(".md") and "SOP-" in file and "-V2" not in file:
            with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                v1_content = f.read()
                try:
                    v2_content = refactor_to_v2(file, v1_content)
                    out_path = os.path.join(OUTPUT_DIR, file.replace(".md", "-V2.md"))
                    with open(out_path, 'w', encoding='utf-8') as out_f:
                        out_f.write(v2_content)
                    print(f"[+] Deployed: {file}")
                except Exception as e:
                    print(f"[!] Critical Failure on {file}: {e}")

print("\n" + "="*60)
print(f"MISSION COMPLETE. FILES STORED IN: {OUTPUT_DIR}")
print("="*60)