import tkinter as tk
from tkinter import ttk

def show_log_details(event):
    selected_index = logs_listbox.curselection()
    if selected_index:
        selected_log = logs_listbox.get(selected_index)
        merged_label.config(text=f"{selected_log} included:\n• file1.pdf\n• file2.pdf")
        output_label.config(text=f"Output File:\n{selected_log.replace('Log Entry', 'merged_output')}.pdf")

def show_merge_page():
    main_frame.grid_forget()
    merge_frame.grid(row=0, column=0, sticky="nsew")
    copyright_label.grid(
        row=1, column=0, columnspan=2, pady=(10, 5), sticky="sew"
    )

def go_back():
    merge_frame.grid_forget()
    main_frame.grid(row=0, column=0, sticky="nsew")

# --- Root Setup ---
root = tk.Tk()
root.title("PDF Merger")
root.geometry("900x600")
root.configure(bg="#f0f0f0")

style = ttk.Style()
style.configure("TButton", font=("Segoe UI", 12), padding=6)
style.configure("TLabel", font=("Segoe UI", 11))
style.configure("Header.TLabel", font=("Segoe UI", 16, "bold"))

# --- Main Page Frame ---
main_frame = ttk.Frame(root, padding=10)
main_frame.grid(row=0, column=0, sticky="nsew")

# Left Panel
logs_frame = ttk.Frame(main_frame, padding=10)
logs_frame.grid(row=0, column=0, sticky="nsw")

logs_header = ttk.Label(logs_frame, text="Previous Merged Logs", style="Header.TLabel")
logs_header.pack(anchor="w", pady=(0, 10))

listbox_container = tk.Frame(logs_frame, bg="white", bd=1, relief=tk.SOLID)
listbox_container.pack(fill=tk.X)

logs_listbox = tk.Listbox(
    listbox_container, bg="white", width=30, height=10, bd=0,
    highlightthickness=0, selectbackground="#dcdcdc"
)
logs_listbox.pack(side=tk.LEFT, fill=tk.BOTH, padx=5, pady=5)

scrollbar = ttk.Scrollbar(listbox_container, orient=tk.VERTICAL, command=logs_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
logs_listbox.config(yscrollcommand=scrollbar.set)

for i in range(1, 11):
    logs_listbox.insert(tk.END, f"Log Entry {i}")
logs_listbox.bind("<<ListboxSelect>>", show_log_details)

details_frame = ttk.LabelFrame(logs_frame, text="Details", padding=10)
details_frame.pack(pady=15, fill=tk.BOTH)

merged_label = ttk.Label(details_frame, text="Select a log to view details", wraplength=200, justify="left")
merged_label.pack(anchor="w", pady=(0, 10))

output_label = ttk.Label(details_frame, text="", wraplength=200, justify="left")
output_label.pack(anchor="w")

# Right Panel
right_frame = ttk.Frame(main_frame, padding=30)
right_frame.grid(row=0, column=1, sticky="nsew")
main_frame.grid_columnconfigure(1, weight=1)

icon_label = ttk.Label(right_frame, text="📄", font=("Segoe UI", 60))
icon_label.pack(pady=(50, 20))

title_label = ttk.Label(right_frame, text="PDF Merger", font=("Segoe UI", 20, "bold"))
title_label.pack(pady=(0, 40))

merge_button = ttk.Button(right_frame, text="Merge PDF", command=show_merge_page)
merge_button.pack()

# --- Merge Page Frame ---
merge_frame = ttk.Frame(root, padding=50)

merge_title = ttk.Label(merge_frame, text="PDF Merge Page", font=("Segoe UI", 20, "bold"))
merge_title.pack(pady=(10, 30))

merge_note = ttk.Label(merge_frame, text="(This is the second page after clicking Merge)", font=("Segoe UI", 12))
merge_note.pack(pady=5)

back_button = ttk.Button(merge_frame, text="⬅ Back", command=go_back)
back_button.pack(pady=(30, 10))

# --- Footer ---
copyright_label = ttk.Label(
    root,
    text="© 2025 by bgcfab",
    font=("Segoe UI", 9),
    background="#f0f0f0",
    anchor="center"
)
copyright_label.grid(
    row=1, column=0, columnspan=2, pady=(10, 5), sticky="sew"
)

# Layout Resizing
root.grid_rowconfigure(0, weight=1)

# Run the app
root.mainloop()
