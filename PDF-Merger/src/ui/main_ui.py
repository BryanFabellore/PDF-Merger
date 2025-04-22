import tkinter as tk
from tkinter import filedialog, messagebox
from tkinterdnd2 import TkinterDnD, DND_FILES
import os
import datetime

# Mock function to get PDF metadata
def get_mock_pdf_metadata(file_path):
    size = os.path.getsize(file_path)
    size_kb = f"{size // 1024} KB"
    pages = "N/A"  # Placeholder for now (needs PyPDF2 for real page count)
    modified = datetime.datetime.fromtimestamp(os.path.getmtime(file_path)).strftime("%Y-%m-%d %H:%M")
    return size_kb, pages, modified

def add_pdf_to_list(file_path):
    var = tk.BooleanVar()

    size, pages, modified = get_mock_pdf_metadata(file_path)
    filename = os.path.basename(file_path)

    row_frame = tk.Frame(listbox_frame, bg="white")
    row_frame.pack(fill=tk.X, padx=5, pady=2)

    checkbox = tk.Checkbutton(row_frame, variable=var, bg="white", fg="black", selectcolor="lightgray")
    checkbox.var = var
    checkbox.pack(side=tk.LEFT)

    tk.Label(row_frame, text=f"{len(checkboxes)+1}", width=4, anchor="w", bg="white").pack(side=tk.LEFT)

    # Add Marquee Effect for Filename
    marquee_label = tk.Label(row_frame, text=filename, width=25, anchor="w", bg="white", fg="black")
    marquee_label.pack(side=tk.LEFT)

    # Start scrolling text
    def marquee():
        current_text = marquee_label.cget("text")
        marquee_label.config(text=current_text[1:] + current_text[0])
        marquee_label.after(150, marquee)  # Adjust speed here

    marquee()  # Call the marquee function to start the effect

    tk.Label(row_frame, text=size, width=10, anchor="w", bg="white").pack(side=tk.LEFT)
    tk.Label(row_frame, text=pages, width=8, anchor="w", bg="white").pack(side=tk.LEFT)
    tk.Label(row_frame, text=modified, width=20, anchor="w", bg="white").pack(side=tk.LEFT)

    checkboxes.append((checkbox, row_frame))

# File dialog add
def add_pdf_files():
    file_paths = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
    if file_paths:
        for file_path in file_paths:
            add_pdf_to_list(file_path)

# Drag and Drop handler
def on_drop(event):
    files = root.tk.splitlist(event.data)
    for file_path in files:
        if file_path.lower().endswith(".pdf"):
            add_pdf_to_list(file_path)

def clear_list():
    for checkbox, row in checkboxes[:]:
        row.destroy()
    checkboxes.clear()

def remove_selected_files():
    for checkbox, row in checkboxes[:]:
        if checkbox.var.get():
            row.destroy()
            checkboxes.remove((checkbox, row))

def highlight_all():
    if all(checkbox.var.get() for checkbox, _ in checkboxes):
        for checkbox, _ in checkboxes:
            checkbox.deselect()
    else:
        for checkbox, _ in checkboxes:
            checkbox.select()


def browse_destination():
    folder_path = filedialog.askdirectory()
    if folder_path:
        destination_entry.delete(0, tk.END)
        destination_entry.insert(0, folder_path)

def save_input_name():
    input_name = input_entry.get()
    messagebox.showinfo("Save", f"Input file name: {input_name}")

# --- Main Window ---
root = TkinterDnD.Tk()
root.title("PDF Manager")
root.geometry("700x500")
root.configure(bg="white")
root.drop_target_register(DND_FILES)
root.dnd_bind("<<Drop>>", on_drop)

# --- Top Section: Table Headers ---
listbox_frame = tk.Frame(root, bd=2, relief=tk.SUNKEN, bg="white")
listbox_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

header_frame = tk.Frame(listbox_frame, bg="white")
header_frame.pack(fill=tk.X)

headers = ["", "#", "Name", "Size", "Pages", "Date Modified"]
widths = [2, 4, 25, 10, 8, 20]

for col, w in zip(headers, widths):
    label = tk.Label(header_frame, text=col, bg="white", fg="black", font=("Arial", 10, "bold"), width=w, anchor="w")
    label.pack(side=tk.LEFT)

checkboxes = []

# --- Buttons ---
button_frame = tk.Frame(root, bg="white")
button_frame.pack(pady=5)

tk.Button(button_frame, text="Add PDFs", command=add_pdf_files, bg="white", fg="black").pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Clear", command=clear_list, bg="white", fg="black").pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Remove Selected", command=remove_selected_files, bg="white", fg="black").pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Highlight All", command=highlight_all, bg="white", fg="black").pack(side=tk.LEFT, padx=5)

# --- Destination and File Name Entry ---
file_path_frame = tk.Frame(root, pady=10, padx=10, bg="white")
file_path_frame.pack(fill=tk.X)

tk.Label(file_path_frame, text="Destination File:", bg="white", fg="black").grid(row=0, column=0, sticky="w")
destination_entry = tk.Entry(file_path_frame, bg="white", fg="black")
destination_entry.grid(row=0, column=1, sticky="ew", padx=5)
tk.Button(file_path_frame, text="Browse", command=browse_destination, bg="white", fg="black").grid(row=0, column=2)

tk.Label(file_path_frame, text="Input File Name:", bg="white", fg="black").grid(row=1, column=0, sticky="w", pady=5)
input_entry = tk.Entry(file_path_frame, bg="white", fg="black")
input_entry.grid(row=1, column=1, sticky="ew", padx=5)
tk.Button(file_path_frame, text="Save", command=save_input_name, bg="white", fg="black").grid(row=1, column=2)

file_path_frame.grid_columnconfigure(1, weight=1)

root.mainloop()
