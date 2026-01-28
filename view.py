#No logic, No file imports, No data access

import tkinter as tk

class MoodJournalView:
    def __init__(self, root):
        self.root = root
        self.root.title("Mood Journal 💙")
        self.root.geometry("420x450")
        self.root.resizable(False, False)

        self.mood_var = tk.StringVar(value="😊 Happy")

        self.build_ui()

    def build_ui(self):
        tk.Label(
            self.root,
            text="Daily Mood Journal",
            font=("Helvetica", 16, "bold")
        ).pack(pady=10)

        tk.Label(
            self.root,
            text="How are you feeling today?",
            font=("Helvetica", 12)
        ).pack(pady=5)

        moods = [
            "😊 Happy", "😢 Sad", "😠 Angry",
            "😨 Anxious", "😐 Neutral",
            "😴 Tired", "🤒 Sick"
        ]

        tk.OptionMenu(self.root, self.mood_var, *moods).pack(pady=8)

        tk.Label(self.root, text="Notes (optional):").pack()
        self.notes_text = tk.Text(self.root, height=6, width=45)
        self.notes_text.pack(pady=8)

        self.save_button = tk.Button(self.root, text="Save Entry", width=25)
        self.save_button.pack(pady=10)

        self.summary_button = tk.Button(self.root, text="View Weekly Summary", width=20)
        self.summary_button.pack(pady=5)

        self.chart_button = tk.Button(self.root, text="View Mood Chart", width=20)
        self.chart_button.pack(pady=5)

        self.status_label = tk.Label(self.root, text="", font=("Helvetica", 10))
        self.status_label.pack(pady=5)
