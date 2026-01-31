import tkinter as tk
from tkinter import messagebox, ttk
import json
import os
from datetime import datetime

EMOTIONS_FILE = "emotions.json"

class EmotionsTracker:
    def __init__(self):
        self.data = self.load_emotions()

    def load_emotions(self):
        if os.path.exists(EMOTIONS_FILE):
            try:
                with open(EMOTIONS_FILE, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                return []
        else:
            return []

    def save_emotions(self):
        with open(EMOTIONS_FILE, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=2)

    def add_emotion(self, emotion, note=""):
        entry = {
            "emotion": emotion,
            "note": note,
            "timestamp": self.get_timestamp()
        }
        self.data.append(entry)
        self.save_emotions()

    def get_timestamp(self):
        return datetime.now().strftime('%Y-%m-%d %H:%M')

    def get_recent_entries(self, n=5):
        return self.data[-n:] if self.data else []

def open_emotions_window():
    tracker = EmotionsTracker()

    win = tk.Toplevel()
    win.title("💖 Emotions Tracker - MindMate")
    win.geometry("400x420")
    win.configure(bg="#fafbff")

    # Header
    header = tk.Label(
        win, text="How are you feeling today?",
        font=("Helvetica", 18, "bold"),
        bg="#fafbff", fg="#4f8cff", pady=10)
    header.pack()

    tk.Label(win, text="Select your current emotion:", font=("Helvetica", 12), bg="#fafbff", fg="#222").pack(pady=5)

    emotions = [
        ("😊 Happy", "Happy"),
        ("😢 Sad", "Sad"),
        ("😠 Angry", "Angry"),
        ("😰 Anxious", "Anxious"),
        ("😌 Calm", "Calm"),
        ("🤩 Excited", "Excited"),
        ("🥱 Tired", "Tired"),
    ]
    selected_emotion = tk.StringVar(value=emotions[0][1])

    em_frame = tk.Frame(win, bg="#fafbff")
    em_frame.pack()
    for em_text, em_val in emotions:
        tk.Radiobutton(
            em_frame, text=em_text, variable=selected_emotion, value=em_val,
            font=("Helvetica", 12), bg="#fafbff", anchor="w", selectcolor="#e7f0ff",
            activebackground="#e7f0ff"
        ).pack(anchor="w", pady=2)

    tk.Label(win, text="Add a note (optional):", font=("Helvetica", 11), bg="#fafbff", fg="#444").pack(pady=(10, 2))
    note_entry = tk.Text(win, height=4, font=("Helvetica", 11), bg="#fff", fg="#333", relief="groove")
    note_entry.pack(fill="x", padx=20)

    def save_emotion():
        emotion = selected_emotion.get()
        note = note_entry.get("1.0", "end").strip()
        tracker.add_emotion(emotion, note)
        messagebox.showinfo("Saved", "Your emotion has been recorded! 💖")
        win.destroy()

    btn = tk.Button(
        win, text="Save Emotion", command=save_emotion,
        font=("Helvetica", 12, "bold"), bg="#4f8cff", fg="#fff", width=18,
        activebackground="#2e6fd6", relief="raised", cursor="hand2"
    )
    btn.pack(pady=14)

    # Recent emotions history
    def show_history():
        history = tracker.get_recent_entries(5)
        if not history:
            messagebox.showinfo("Recent Emotions", "No emotions recorded yet.")
        else:
            msg = ""
            for entry in reversed(history):
                emoji = next((e[0][0] for e in emotions if e[1] == entry["emotion"]), "")
                msg += f"{emoji} {entry['emotion']} @ {entry['timestamp']}\n"
                if entry["note"]:
                    msg += f"  Note: {entry['note']}\n"
            messagebox.showinfo("Recent Emotions", msg)

    hist_btn = tk.Button(
        win, text="Show Recent Emotions", command=show_history,
        font=("Helvetica", 10), bg="#e7f0ff", fg="#325fa7", relief="flat", cursor="hand2"
    )
    hist_btn.pack(pady=7)

    # Footer
    footer = tk.Label(
        win, text="Tracking your emotions helps you understand your mind better.",
        font=("Helvetica", 9), bg="#fafbff", fg="#888"
    )
    footer.pack(side="bottom", pady=8)