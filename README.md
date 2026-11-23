**sudo apt update && sudo apt install python3-venv**

Ign:1 http://packages.linuxmint.com zena InRelease

Hit:2 http://packages.linuxmint.com zena Release

Hit:4 https://packages.microsoft.com/repos/code stable InRelease

Hit:5 http://archive.ubuntu.com/ubuntu noble InRelease    

Hit:6 https://dl.google.com/linux/chrome-stable/deb stable InRelease

Hit:7 http://archive.ubuntu.com/ubuntu noble-updates InRelease

Hit:8 http://security.ubuntu.com/ubuntu noble-security InRelease

Hit:9 http://archive.ubuntu.com/ubuntu noble-backports InRelease

Hit:10 https://ppa.launchpadcontent.net/foldyna/qlog/ubuntu noble InRelease

Reading package lists... Done

Building dependency tree... Done

Reading state information... Done

7 packages can be upgraded. Run 'apt list --upgradable' to see them.

Reading package lists... Done

Building dependency tree... Done

Reading state information... Done

python3-venv is already the newest version (3.12.3-0ubuntu2.1).

0 upgraded, 0 newly installed, 0 to remove and 7 not upgraded.

**$ python3 -m venv .venv**

**source .venv/bin/activate**

**pip install python-pptx**


**$ ./make_subelement_slides.py**

Found 409 questions in 10 subelements
  → subelement_decks/Tech_2026_T0.pptx  (36 slides)
  → subelement_decks/Tech_2026_T1.pptx  (68 slides)
  → subelement_decks/Tech_2026_T2.pptx  (37 slides)
  → subelement_decks/Tech_2026_T3.pptx  (35 slides)
  → subelement_decks/Tech_2026_T4.pptx  (23 slides)
  → subelement_decks/Tech_2026_T5.pptx  (50 slides)
  → subelement_decks/Tech_2026_T6.pptx  (46 slides)
  → subelement_decks/Tech_2026_T7.pptx  (44 slides)
  → subelement_decks/Tech_2026_T8.pptx  (47 slides)
  → subelement_decks/Tech_2026_T9.pptx  (23 slides)

Done!  Open each .pptx in LibreOffice Impress,

select the green “Correct Answer” box, and add an Appear / On-click animation.

Then File → Save As → ODF Presentation (.odp) if you prefer pure ODP files.

Done!  Open each .pptx in LibreOffice Impress,

select the green “Correct Answer” box, and add an Appear / On-click animation.

Then File → Save As → ODF Presentation (.odp) if you prefer pure ODP files.
