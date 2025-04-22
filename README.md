# 📁 PDF-Merger

> An offline desktop app to clean, sort, and merge PDF files from multiple folders using a simple GUI.

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Tkinter GUI](https://img.shields.io/badge/GUI-Tkinter-brightgreen)
![Offline](https://img.shields.io/badge/Offline-Yes-critical)

---

## ✨ Features

| Feature               | Description |
|------------------------|-------------|
| 🧹 **PDF Cleaning**     | Removes duplicate metadata and optimizes PDFs using `PyPDF2`. |
| 📁 **Folder Scanning**  | Automatically scans up to 4 folders and saves to `cleaned_pdfs/`. |
| 🔠 **Alphabetical Sort**| Orders PDFs by filename before merging. |
| 📎 **Folder Merge**     | Merges each folder’s PDFs into `combined_<foldername>.pdf`. |
| 📦 **Master Merge**     | Merges all combined PDFs into one file under `merged_pdfs/Last Output/`. |
| 🧾 **Logging System**   | Tracks actions in CSV logs (`outputs/logs/`). |
| 🖥️ **GUI Interface**    | Simple, no-CLI tkinter GUI. |
| 🚫 **Offline Ready**    | Fully functional without internet using `PyInstaller`. |

---

## 🛠️ Tech Stack

| Purpose         | Technology   |
|------------------|--------------|
| GUI              | `tkinter`    |
| PDF Handling     | `PyPDF2`     |
| Packaging        | `PyInstaller`|
| Logging          | CSV / TXT    |
| Version Control  | `Git`        |

---

<details>
<summary>📂 File Structure</summary>

```plaintext
PDF-Merger/
├── main.py
├── requirements.txt
├── README.md
│
├── config/
│   └── settings.py
│
├── src/
│   ├── __init__.py
│   ├── ui/
│   │   └── main_ui.py
│   ├── utils/
│   │   ├── pdf_handler.py
│   │   ├── logger.py
│   │   ├── pdf_merger.py
│   │   └── file_handler.py
│   └── services/
│       └── pdf_info.py
│
├── assets/
│   └── icons/
│
└── outputs/
    ├── merged_pdfs/
    └── logs/


