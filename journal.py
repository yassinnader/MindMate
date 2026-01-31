import tkinter as tk
from tkinter import messagebox, filedialog
import os
from datetime import datetime

JOURNAL_FILE = "journal_entries.txt"

def open_journal_window():
    journal_win = tk.Toplevel()
    journal_win.title("📝 Journal - MindMate")
    journal_win.geometry("500x550")
    journal_win.configure(bg="#f7faff")

    # Header
    header = tk.Label(
        journal_win,
        text="📝 My Journal",
        font=("Helvetica", 22, "bold"),
        bg="#f7faff",
        fg="#325fa7",
        pady=15
    )
    header.pack()

    # Date/time stamp
    date_label = tk.Label(
        journal_win,
        text=f"Today: {datetime.now().strftime('%A, %B %d, %Y %I:%M %p')}",
        font=("Helvetica", 11, "italic"),
        bg="#f7faff",
        fg="#888"
    )
    date_label.pack()

    # Text area
    text_area = tk.Text(
        journal_win,
        wrap="word",
        font=("Helvetica", 13),
        bg="#ffffff",
        fg="#222",
        borderwidth=2,
        relief="groove"
    )
    text_area.pack(expand=True, fill="both", padx=18, pady=14)

    # Load previous entries
    if os.path.exists(JOURNAL_FILE):
        with open(JOURNAL_FILE, "r", encoding="utf-8") as f:
            text_area.insert("1.0", f.read())

    # --- Amazing features ---
    def save_entries():
        content = text_area.get("1.0", tk.END).strip()
        with open(JOURNAL_FILE, "w", encoding="utf-8") as f:
            f.write(content)
        messagebox.showinfo("Saved", "Your journal entries have been saved! 😊")

    def clear_journal():
        if messagebox.askyesno("Clear", "Are you sure you want to clear your journal?"):
            text_area.delete("1.0", tk.END)

    def export_journal():
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if file_path:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(text_area.get("1.0", tk.END).strip())
            messagebox.showinfo("Exported", f"Journal exported to {file_path}")

    def add_datetime():
        text_area.insert(tk.INSERT, f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M')}] ")

    # Button frame
    btn_frame = tk.Frame(journal_win, bg="#f7faff")
    btn_frame.pack(fill="x", pady=6)

    save_btn = tk.Button(
        btn_frame,
        text="💾 Save Journal",
        font=("Helvetica", 11, "bold"),
        bg="#4f8cff",
        fg="#fff",
        width=14,
        relief="raised",
        command=save_entries,
        cursor="hand2",
        activebackground="#2e6fd6"
    )
    save_btn.pack(side="left", padx=(18, 8), pady=2)

    export_btn = tk.Button(
        btn_frame,
        text="⬇️ Export",
        font=("Helvetica", 11, "bold"),
        bg="#8ad5b3",
        fg="#fff",
        width=10,
        relief="raised",
        command=export_journal,
        cursor="hand2",
        activebackground="#5ea37f"
    )
    export_btn.pack(side="left", padx=8, pady=2)

    date_btn = tk.Button(
        btn_frame,
        text="⏰ Timestamp",
        font=("Helvetica", 11),
        bg="#ffe066",
        fg="#444",
        width=12,
        relief="raised",
        command=add_datetime,
        cursor="hand2",
        activebackground="#ffd43b"
    )
    date_btn.pack(side="left", padx=8, pady=2)

    clear_btn = tk.Button(
        btn_frame,
        text="🗑️ Clear",
        font=("Helvetica", 11),
        bg="#ff6868",
        fg="#fff",
        width=8,
        relief="raised",
        command=clear_journal,
        cursor="hand2",
        activebackground="#d63447"
    )
    clear_btn.pack(side="right", padx=(8, 18), pady=2)

    # Footer
    footer = tk.Label(
        journal_win,
        text="All entries are private and stored locally.",
        bg="#f7faff",
        fg="#aaa",
        font=("Helvetica", 10)
    )
    footer.pack(side="bottom", pady=8)