import tkinter as tk
from tkinter import filedialog, messagebox
from tkinterdnd2 import TkinterDnD, DND_FILES
import os
import datetime
import subprocess

# --- Helper Functions -------------------------------------------------------

# Mock function to get PDF metadata
def get_mock_pdf_metadata(file_path):
    size = os.path.getsize(file_path)
    size_kb = f"{size // 1024} KB"
    pages = "N/A"  # Placeholder; swap in PyPDF2 if you need real counts
    modified = datetime.datetime.fromtimestamp(
        os.path.getmtime(file_path)
    ).strftime("%Y-%m-%d %H:%M")
    return size_kb, pages, modified

def add_pdf_to_list(file_path):
    var = tk.BooleanVar()
    size, pages, modified = get_mock_pdf_metadata(file_path)
    filename = os.path.basename(file_path)

    row_frame = tk.Frame(listbox_frame, bg="white")
    row_frame.pack(fill=tk.X, padx=5, pady=2)

    checkbox = tk.Checkbutton(
        row_frame, variable=var, bg="white", fg="black", selectcolor="lightgray"
    )
    checkbox.var = var
    checkbox.pack(side=tk.LEFT)

    # Serial #
    tk.Label(
        row_frame, text=f"{len(checkboxes)+1}", width=4,
        anchor="w", bg="white"
    ).pack(side=tk.LEFT)

    # Marquee filename
    marquee_label = tk.Label(
        row_frame, text=filename, width=25,
        anchor="w", bg="white", fg="black"
    )
    marquee_label.pack(side=tk.LEFT)
    def marquee():
        txt = marquee_label.cget("text")
        marquee_label.config(text=txt[1:] + txt[0])
        marquee_label.after(150, marquee)
    marquee()

    # Metadata columns
    tk.Label(row_frame, text=size, width=10, anchor="w", bg="white").pack(side=tk.LEFT)
    tk.Label(row_frame, text=pages, width=8, anchor="w", bg="white").pack(side=tk.LEFT)
    tk.Label(row_frame, text=modified, width=20, anchor="w", bg="white").pack(side=tk.LEFT)

    checkboxes.append((checkbox, row_frame))

def add_pdf_files():
    file_paths = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
    for fp in file_paths:
        add_pdf_to_list(fp)

def on_drop(event):
    for fp in root.tk.splitlist(event.data):
        if fp.lower().endswith(".pdf"):
            add_pdf_to_list(fp)

def clear_list():
    for cb, row in checkboxes[:]:
        row.destroy()
    checkboxes.clear()

def remove_selected_files():
    for cb, row in checkboxes[:]:
        if cb.var.get():
            row.destroy()
            checkboxes.remove((cb, row))

def highlight_all():
    all_selected = all(cb.var.get() for cb, _ in checkboxes)
    for cb, _ in checkboxes:
        if all_selected:
            cb.deselect()
        else:
            cb.select()

def browse_destination():
    folder = filedialog.askdirectory()
    if folder:
        destination_entry.delete(0, tk.END)
        destination_entry.insert(0, folder)

def save_input_name():
    messagebox.showinfo("Save", f"Input file name: {input_entry.get()}")

def go_back():
    # find menu_ui.py in the same directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    menu_path = os.path.join(script_dir, "menu_ui.py")
    subprocess.Popen(["python", menu_path])
    root.destroy()

# --- Build UI ---------------------------------------------------------------

root = TkinterDnD.Tk()
root.title("PDF Manager")
root.geometry("700x500")
root.configure(bg="white")
root.drop_target_register(DND_FILES)
root.dnd_bind("<<Drop>>", on_drop)

# Back‐button at top
top_bar = tk.Frame(root, bg="white")
top_bar.pack(fill=tk.X, pady=(5,0), padx=5)
tk.Button(
    top_bar, text="⬅ Back", command=go_back,
    bg="white", fg="black"
).pack(side=tk.LEFT)

# Table headers
listbox_frame = tk.Frame(root, bd=2, relief=tk.SUNKEN, bg="white")
listbox_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
header_frame = tk.Frame(listbox_frame, bg="white")
header_frame.pack(fill=tk.X)

headers = ["", "#", "Name", "Size", "Pages", "Date Modified"]
widths  = [2, 4, 25, 10, 8, 20]
for text, w in zip(headers, widths):
    tk.Label(
        header_frame, text=text, bg="white", fg="black",
        font=("Arial", 10, "bold"), width=w, anchor="w"
    ).pack(side=tk.LEFT)

checkboxes = []

# Action buttons
button_frame = tk.Frame(root, bg="white")
button_frame.pack(pady=5)
for (label, cmd) in [
    ("Add PDFs", add_pdf_files),
    ("Clear", clear_list),
    ("Remove Selected", remove_selected_files),
    ("Highlight All", highlight_all),
]:
    tk.Button(
        button_frame, text=label, command=cmd,
        bg="white", fg="black"
    ).pack(side=tk.LEFT, padx=5)

# Destination / filename entry
file_path_frame = tk.Frame(root, pady=10, padx=10, bg="white")
file_path_frame.pack(fill=tk.X)
tk.Label(file_path_frame, text="Destination File:", bg="white", fg="black")\
    .grid(row=0, column=0, sticky="w")
destination_entry = tk.Entry(file_path_frame, bg="white", fg="black")
destination_entry.grid(row=0, column=1, sticky="ew", padx=5)
tk.Button(
    file_path_frame, text="Browse", command=browse_destination,
    bg="white", fg="black"
).grid(row=0, column=2)

tk.Label(file_path_frame, text="Input File Name:", bg="white", fg="black")\
    .grid(row=1, column=0, sticky="w", pady=5)
input_entry = tk.Entry(file_path_frame, bg="white", fg="black")
input_entry.grid(row=1, column=1, sticky="ew", padx=5)
tk.Button(
    file_path_frame, text="Save", command=save_input_name,
    bg="white", fg="black"
).grid(row=1, column=2)
file_path_frame.grid_columnconfigure(1, weight=1)

root.mainloop()
