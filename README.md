📁 PDF-Merger
An offline desktop app to clean, sort, and merge PDF files from multiple folders using a simple GUI.

⚙️ Features & Functions

Functionality Description
🧹 PDF Cleaning Removes duplicate metadata and unnecessary information from each PDF file using PyPDF2. Ensures all outputs are optimized and standardized before merging.
📁 Folder Scanning Automatically scans up to four input folders containing raw PDFs, organizes the cleaned files into corresponding cleaned*pdfs folders.
🔠 Alphabetical Sorting Sorts cleaned PDFs alphabetically by filename before combining, ensuring a structured and orderly final output.
📎 Folder-wise Merging Merges cleaned PDFs per folder and creates combined*<foldername> outputs in a separate output directory.
📦 Final Master Merge All four combined\_<foldername> PDFs are merged into a single master PDF file stored in the outputs/merged_pdfs/Last Output/ directory.
🧾 Logging System Generates a CSV-based log for every cleaned and merged file, including: filename, file type, last modified time, and the output name. Stored under outputs/logs/.
🖥️ GUI Interface Simple desktop app built with tkinter for file selection, status updates, and triggering processes without requiring command-line interaction.
🚫 Offline Use Only Entire system is designed to run locally without an internet connection. All dependencies are bundled for full offline access using PyInstaller.

# 🛠️ Tech Stack

[= Purpose | Technology =]
[= GUI | tkinter =]
[= PDF Handling | PyPDF2 =]
[= Packaging | PyInstaller =]
[= Logging | CSV / TXT =]
[= Version Control | Git =]
=====================================
📂 File Structure
PDF-Merger/
├── main.py
├── requirements.txt
├── README.md
│
├── config/
│ └── settings.py
│
├── src/
│ ├── **init**.py
│ │
│ ├── ui/
│ │ └── main_ui.py
│ │
│ ├── utils/
│ │ ├── pdf_handler.py
│ │ ├── logger.py
│ │ ├── pdf_merger.py
│ │ └── file_handler.py
│ │
│ └── services/
│ └── pdf_info.py
│
├── assets/
│ └── icons/
│
└── outputs/
├── merged_pdfs/
└── logs/
