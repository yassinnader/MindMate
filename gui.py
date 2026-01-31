import tkinter as tk
from tkinter import messagebox
from journal import open_journal_window
from emotions import open_emotions_window
from ai_core import open_ai_assistant
from user_profile import show_user_profile

BUTTON_BG = "#4f8cff"
BUTTON_FG = "#ffffff"
BUTTON_HOVER_BG = "#2e6fd6"
BUTTON_FONT = ("Helvetica", 14, "bold")
TITLE_FONT = ("Helvetica", 28, "bold")
BG_COLOR = "#f0f0f0"

def on_enter(e):
    e.widget['background'] = BUTTON_HOVER_BG

def on_leave(e):
    e.widget['background'] = BUTTON_BG

def make_button(root, text, command):
    btn = tk.Button(
        root,
        text=text,
        width=20,
        height=2,
        bg=BUTTON_BG,
        fg=BUTTON_FG,
        font=BUTTON_FONT,
        command=command,
        relief=tk.RAISED,
        bd=3,
        activebackground=BUTTON_HOVER_BG,
        activeforeground=BUTTON_FG,
        cursor="hand2"
    )
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    return btn

def start_mindmate_gui():
    root = tk.Tk()
    root.title("MindMate - Your Smart Mind Companion")
    root.geometry("420x520")
    root.configure(bg=BG_COLOR)
    # Optional: set your own icon file
    # root.iconbitmap("icon.ico")

    title = tk.Label(root, text="MindMate 🧠", font=TITLE_FONT, bg=BG_COLOR, pady=30, fg="#222")
    title.pack(pady=(20, 10), anchor="center")

    btn_journal = make_button(root, "📝 Journal", open_journal_window)
    btn_journal.pack(pady=12)

    btn_emotions = make_button(root, "💭 Emotions", open_emotions_window)
    btn_emotions.pack(pady=12)

    btn_ai = make_button(root, "🤖 AI Assistant", open_ai_assistant)
    btn_ai.pack(pady=12)

    btn_profile = make_button(root, "👤 My Profile", show_user_profile)
    btn_profile.pack(pady=12)

    footer = tk.Label(root, text="Made with ❤️ by MindMate Team", bg=BG_COLOR, fg="#888", font=("Helvetica", 10))
    footer.pack(side="bottom", pady=20)

    root.mainloop()

if __name__ == "__main__":
    start_mindmate_gui()