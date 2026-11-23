#!/usr/bin/env python3
"""
Creates one PowerPoint file per Technician subelement (T0–T9).
Correct answer is placed in a separate green box so you can easily
add “Appear on click” animation in LibreOffice Impress / PowerPoint.
"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.oxml.ns import nsmap
from collections import defaultdict
import json
import os

# ---------- CONFIG ----------
JSON_FILE   = "technician-2026-2030.json"
FIGURE_DIR  = "."                     # folder containing t-1.png, t-2.png, t-3.png
OUTPUT_DIR  = "subelement_decks"      # folder where the .pptx files will be written
CORRECT_COLOR = RGBColor(0, 140, 0)   # green
NORMAL_COLOR  = RGBColor(0, 0, 0)
# ----------------------------

os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(JSON_FILE, encoding="utf-8") as f:
    all_questions = json.load(f)

# Group by subelement (first two characters of the ID)
groups = defaultdict(list)
for q in all_questions:
    sub = q["id"][:2]          # "T1", "T0", "T7", …
    groups[sub].append(q)

print(f"Found {len(all_questions)} questions in {len(groups)} subelements")

for sub, questions in sorted(groups.items()):
    prs = Presentation()
    prs.slide_width  = Inches(13.333)   # 16:9
    prs.slide_height = Inches(7.5)
    blank = prs.slide_layouts[6]

    # ---- Title slide ----
    slide = prs.slides.add_slide(blank)
    box = slide.shapes.add_textbox(Inches(0.5), Inches(2.5), Inches(12.3), Inches(2))
    tf = box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    run = p.add_run()
    run.text = f"Technician Class 2026–2030\nSubelement {sub}"
    run.font.size = Pt(36)
    run.font.bold = True

    p = tf.add_paragraph()
    p.alignment = PP_ALIGN.CENTER
    run = p.add_run()
    run.text = f"{len(questions)} questions"
    run.font.size = Pt(24)

    # ---- One slide per question ----
    for q in questions:
        slide = prs.slides.add_slide(blank)

        # Question header + text
        qbox = slide.shapes.add_textbox(Inches(0.4), Inches(0.25), Inches(12.5), Inches(1.7))
        tf = qbox.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        run = p.add_run()
        run.text = f"{q['id']}   {q.get('refs', '')}"
        run.font.size = Pt(16)
        run.font.bold = True
        run.font.color.rgb = RGBColor(80, 80, 80)

        p = tf.add_paragraph()
        run = p.add_run()
        run.text = q["question"]
        run.font.size = Pt(22)
        run.font.bold = True

        # Four answer choices (all black)
        abox = slide.shapes.add_textbox(Inches(0.5), Inches(2.1), Inches(12.3), Inches(3.2))
        tf = abox.text_frame
        tf.word_wrap = True

        letters = ["A", "B", "C", "D"]
        for i, ans in enumerate(q["answers"]):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            p.space_before = Pt(8)
            run = p.add_run()
            run.text = f"{letters[i]}. {ans}"
            run.font.size = Pt(18)
            run.font.color.rgb = NORMAL_COLOR

        # Correct-answer box (green) – this is the one you animate
        correct_letter = q["correct_letter"]
        correct_text   = q["answers"][q["correct"]]
        cbox = slide.shapes.add_textbox(Inches(0.5), Inches(5.5), Inches(12.3), Inches(1.3))
        tf = cbox.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        run = p.add_run()
        run.text = f"Correct Answer:  {correct_letter}. {correct_text}"
        run.font.size = Pt(18)
        run.font.bold = True
        run.font.color.rgb = CORRECT_COLOR

        # Optional diagram
        fig = q.get("figure", "").strip()
        if fig:
            fig_path = os.path.join(FIGURE_DIR, fig)
            if os.path.exists(fig_path):
                # Place on the right side, smaller
                slide.shapes.add_picture(fig_path, Inches(9.8), Inches(2.2), height=Inches(3.0))

    outfile = os.path.join(OUTPUT_DIR, f"Tech_2026_{sub}.pptx")
    prs.save(outfile)
    print(f"  → {outfile}  ({len(questions)} slides)")

print("\nDone!  Open each .pptx in LibreOffice Impress,")
print("select the green “Correct Answer” box, and add an Appear / On-click animation.")
print("Then File → Save As → ODF Presentation (.odp) if you prefer pure ODP files.")