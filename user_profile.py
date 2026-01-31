import json
import os
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

PROFILE_FILE = "user_profile.json"

class UserProfile:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.level = 1
        self.mood = None
        self.last_active = None
        self.achievements = []
        self.load_profile()

    def update_score(self, points):
        self.score += points
        self.check_level_up()
        self.save_profile()

    def check_level_up(self):
        next_level_score = self.level * 50
        if self.score >= next_level_score:
            self.level += 1
            achievement = f"Level {self.level} unlocked on {datetime.now().strftime('%Y-%m-%d %H:%M')}"
            self.achievements.append(achievement)
            print(f"🎉 Congrats {self.name}, you reached level {self.level}! Achievement unlocked!")
            self.save_profile()

    def set_mood(self, mood):
        self.mood = mood
        self.last_active = datetime.now().strftime('%Y-%m-%d %H:%M')
        self.save_profile()

    def get_mood(self):
        return self.mood

    def add_achievement(self, achievement):
        self.achievements.append(achievement)
        self.save_profile()

    def reset_profile(self):
        self.score = 0
        self.level = 1
        self.mood = None
        self.last_active = None
        self.achievements = []
        self.save_profile()

    def save_profile(self):
        data = {
            "name": self.name,
            "score": self.score,
            "level": self.level,
            "mood": self.mood,
            "last_active": self.last_active,
            "achievements": self.achievements,
        }
        try:
            with open(PROFILE_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"Error saving profile: {e}")

    def load_profile(self):
        if not os.path.exists(PROFILE_FILE):
            return
        try:
            with open(PROFILE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            if data.get("name") == self.name:
                self.score = data.get("score", 0)
                self.level = data.get("level", 1)
                self.mood = data.get("mood")
                self.last_active = data.get("last_active")
                self.achievements = data.get("achievements", [])
        except Exception as e:
            print(f"Error loading profile: {e}")

    def profile_summary(self):
        summary = (
            f"🧑 Name: {self.name}\n"
            f"⭐ Score: {self.score}\n"
            f"🏆 Level: {self.level}\n"
            f"😊 Mood: {self.mood if self.mood else 'Not set'}\n"
            f"⏰ Last Active: {self.last_active if self.last_active else 'Never'}\n"
            f"🎖️ Achievements:\n"
        )
        if self.achievements:
            for a in self.achievements:
                summary += f"   • {a}\n"
        else:
            summary += "   (No achievements yet)\n"
        return summary

# ---- ADD THIS FUNCTION ----
def show_user_profile():
    # You can customize the username source as needed
    user = UserProfile("Yassin")

    win = tk.Toplevel()
    win.title("👤 My Profile - MindMate")
    win.geometry("420x350")
    win.configure(bg="#f7faff")

    header = tk.Label(win, text="My Profile", font=("Helvetica", 18, "bold"), bg="#f7faff", fg="#4f8cff")
    header.pack(pady=(18, 10))

    summary = user.profile_summary()
    profile_text = tk.Text(win, height=12, width=44, bg="#fff", fg="#222", font=("Helvetica", 12), wrap="word", borderwidth=2, relief="groove")
    profile_text.insert("1.0", summary)
    profile_text.config(state="disabled")
    profile_text.pack(padx=18, pady=8)

    def reset():
        if messagebox.askyesno("Reset Profile", "Are you sure you want to reset your profile?"):
            user.reset_profile()
            profile_text.config(state="normal")
            profile_text.delete("1.0", tk.END)
            profile_text.insert("1.0", user.profile_summary())
            profile_text.config(state="disabled")
            messagebox.showinfo("Reset", "Profile has been reset.")

    reset_btn = tk.Button(win, text="Reset Profile", command=reset, bg="#ff6868", fg="#fff", font=("Helvetica", 11, "bold"), width=14)
    reset_btn.pack(pady=8)

    footer = tk.Label(win, text="Your data is private and stays on your device.", bg="#f7faff", fg="#888", font=("Helvetica", 9))
    footer.pack(side="bottom", pady=8)