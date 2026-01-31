import random
from datetime import datetime
import tkinter as tk

class AICore:
    def __init__(self):
        self.responses = {
            "default": [
                "I'm here with you—tell me anything, I'm listening. 💬",
                "How are you feeling right now? Your thoughts matter to me.",
                "Let's think about it together. You are not alone. 🤝",
                "Tell me more about what's on your mind, I'm all ears.",
                "Every feeling is valid. Want to share a little more?",
                "I'm proud of you for checking in with yourself today."
            ],
            "happy": [
                "That's wonderful! Happiness is contagious—spread it around! 😄",
                "Your joy lights up the room. What made you happy today?",
                "I'm so glad to hear you're feeling good! Care to tell me more?",
                "Yay, happiness! Let's celebrate the small wins together. 🎉"
            ],
            "sad": [
                "It's okay to feel sad sometimes. You are stronger than you know. 💙",
                "I'm here for you. Would you like to talk about what's making you sad?",
                "Sadness comes and goes, but you're not alone in it.",
                "Sending you a virtual hug. Take all the time you need."
            ],
            "anxious": [
                "Anxiety can be tough. Let's try a deep breath together. 🌬️",
                "You're not alone—many people feel this way sometimes.",
                "Would you like a calming exercise or to talk it through?",
                "Remember, even small steps forward count. I'm with you."
            ],
            "angry": [
                "Anger is a natural emotion. Would you like to vent or find a way to cool off?",
                "It's okay to be upset. I'm here to help you process it.",
                "Let's take some deep breaths together. What triggered this feeling?",
                "You can always talk to me about what's making you angry."
            ],
            "calm": [
                "I'm glad you're feeling calm. Maybe reflect on what brought you peace. 🕊️",
                "A calm mind is a powerful thing. Want to share your secret?",
                "Enjoy this peaceful moment—it's well deserved.",
                "Let's savor the calm together. Tell me about your day."
            ],
            "excited": [
                "Excitement is contagious! What's got you buzzing? 🚀",
                "That sounds awesome! Want to tell me more?",
                "I'm thrilled for you! Let's channel this energy into something fun.",
                "Keep the excitement going! I'm all ears."
            ],
            "tired": [
                "Taking breaks is important. Maybe a quick rest would help. 💤",
                "It's okay to feel tired. Rest and self-care matter.",
                "You've done a lot already. Want to talk or just relax?",
                "Remember to be kind to yourself when you're low on energy."
            ]
        }

    def get_response(self, emotion=None):
        emotion = (emotion or "default").strip().lower()
        return random.choice(self.responses.get(emotion, self.responses["default"]))

    def get_time_based_greeting(self):
        hour = datetime.now().hour
        if 5 <= hour < 12:
            return "Good morning! ☀️"
        elif 12 <= hour < 18:
            return "Good afternoon! 😊"
        elif 18 <= hour < 22:
            return "Good evening! 🌙"
        else:
            return "Hello, night owl! 🌌"

    def chat(self, user_input, emotion=None):
        greeting = self.get_time_based_greeting()
        ai_msg = self.get_response(emotion)
        return f"{greeting}\n{ai_msg}\n\nYou said: \"{user_input}\""

# --- GUI Function for MindMate ---
def open_ai_assistant():
    ai = AICore()

    win = tk.Toplevel()
    win.title("🤖 MindMate AI Assistant")
    win.geometry("500x400")
    win.configure(bg="#f8faff")

    chat_history = tk.Text(win, state="disabled", bg="#fff", fg="#222", font=("Helvetica", 12), wrap="word")
    chat_history.pack(expand=True, fill="both", padx=12, pady=8)

    entry = tk.Entry(win, font=("Helvetica", 12))
    entry.pack(fill="x", padx=12, pady=(0,8))

    def send_message(event=None):
        user_input = entry.get().strip()
        if not user_input:
            return
        entry.delete(0, tk.END)
        chat_history.config(state="normal")
        chat_history.insert(tk.END, f"You: {user_input}\n")
        # Optionally, detect emotion here or let user pick
        ai_msg = ai.get_response()
        chat_history.insert(tk.END, f"AI: {ai_msg}\n\n")
        chat_history.config(state="disabled")
        chat_history.see(tk.END)

    entry.bind("<Return>", send_message)

    send_btn = tk.Button(win, text="Send", command=send_message, bg="#4f8cff", fg="#fff", font=("Helvetica", 11, "bold"))
    send_btn.pack(pady=(0,8))

    entry.focus()

# Optional: for direct script testing
if __name__ == "__main__":
    import tkinter as tk
    root = tk.Tk()
    root.withdraw()
    open_ai_assistant()
    root.mainloop()