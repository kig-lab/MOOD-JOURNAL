#Tiny and clean
import tkinter as tk
from view import MoodJournalView
from controller import MoodJournalController

def main():
    root = tk.Tk()
    view = MoodJournalView(root)
    MoodJournalController(view)
    root.mainloop()

if __name__ == "__main__":
    main()
