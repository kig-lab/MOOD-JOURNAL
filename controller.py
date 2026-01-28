"""Controller talks to models, updates the view (connects UI nd logic) """
import tkinter as tk
from Model.data_manager import save_mood, load_moods
from Model.utils import get_weekly_summary
from Model.analysis import get_last_7days, analyze_week, plot_weekly_mood_chart

class MoodJournalController:
    def __init__(self, view):
        self.view = view
        self.bind_events()

    def bind_events(self):
        self.view.save_button.config(command=self.save_entry)
        self.view.summary_button.config(command=self.show_weekly_summary)
        self.view.chart_button.config(command=self.show_mood_chart)

    def save_entry(self):
        mood = self.view.mood_var.get()
        note = self.view.notes_text.get("1.0", tk.END).strip()

        save_mood(mood, note)
        self.view.notes_text.delete("1.0", tk.END)

        self.view.status_label.config(
            text="Thanks for checking in today ❤ Be kind to yourself ❤",
            fg="#2e7d32"
        )

        self.view.root.after(
            3000, lambda: self.view.status_label.config(text="")
        )

    def show_weekly_summary(self):
        entries = load_moods()
        summary_text = get_weekly_summary(entries)

        summary_window = tk.Toplevel(self.view.root)
        summary_window.title("Weekly Reflection 💙")
        summary_window.geometry("400x300")
        summary_window.resizable(False, False)

        tk.Label(
            summary_window,
            text="Weekly Reflection",
            font=("Helvetica", 14, "bold"),
            fg="#1976d2"
        ).pack(pady=10)

        tk.Label(
            summary_window,
            text=summary_text,
            font=("Helvetica", 10),
            wraplength=340,
            justify="left"
        ).pack(pady=10, padx=15)

        tk.Button(
            summary_window,
            text="Close",
            command=summary_window.destroy,
            width=15,
            background="#2e7d32"
        ).pack(pady=10)

    def show_mood_chart(self):
        entries = load_moods()
        week_entries = get_last_7days(entries)
        analysis_data = analyze_week(week_entries)
        plot_weekly_mood_chart(analysis_data)
