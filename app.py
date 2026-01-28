# CREATION OF MAIN WINDOW USING TKINTER(UI)
import tkinter as tk
from tkinter import messagebox
from Model.utils import get_weekly_summary
from Model.analysis import get_last_7days, analyze_week, plot_weekly_mood_chart

#IMPORT PHASE 1 LOGIC
from Model.data_manager import save_mood, load_moods

#--------------------------------------------------------------CREATE MAIN WINDOW----------------------------------------
root = tk.Tk()   #Creates the main window object
root.title("Mood Journal 💙")
root.geometry("420x450")
root.resizable(False, False)

title_label = tk.Label(
    root,
    text = "Daily Mood Journal",
    font = ("Helvetica", 16, "bold")
)
title_label.pack(pady = 10)

subtitle_label = tk.Label(
    root,
    text = "How are you feeling today?",
    font = ("Helvetica", 12)
)
subtitle_label.pack(pady = 5)

#-----------------------------------------------MOOD SELECTION BY USING A DROPDOWN MENU-------------------------------
mood_var = tk.StringVar()
mood_var.set("😊 Happy") #default mood

moods = [
    "😊 Happy",
    "😢 Sad",
    "😠 Angry",
    "😨 Anxious",
    "😐 Neutral",
    "😴 Tired",
    "🤒 Sick"
]
mood_menu = tk.OptionMenu(root, mood_var, *moods)
mood_menu.pack(pady = 8)

#NOTES TEXT BOX
notes_label = tk.Label(root, text = "Notes(optional):")
notes_label.pack()

notes_text = tk.Text(root, height = 6, width = 45)
notes_text.pack(pady = 8)

#SAVE BUTTON; CONNECTS THE data_manager(phase1)
def save_entry():
    mood = mood_var.get()
    note = notes_text.get("1.0", tk.END).strip()
    save_mood(mood, note)

    notes_text.delete("1.0", tk.END)  # Clear notes box after saving
    status_label.config(text="Thanks for checking in today❤Be kind to yourself❤", fg="#2e7d32")
    #MAKE MESSAGE DISAPPEAR AFTER 3000 MILLISECONDS
    root.after(3000, lambda: status_label.config(text = "")) # lambda(for quick, oneoff tasks esp in tkinter) is an anonymous function that allows you to pass a function with arguments to after method

save_button = tk.Button(
    root,
    text = "Save Entry",
    command = save_entry,
    width = 25
)
save_button.pack(pady = 10)



status_label = tk.Label(root, text = "", font = ("Helvetica", 10), fg="green")
status_label.pack(pady=5)

#-------------------------------------------------WEEKLY SUMMARY BUTTON---------------------------------------
def show_weekly_summary():
    """This function contains widgets such as labels and buttons to show the weekly summary in a new temporary window.
    """
    entries = load_moods()
    summary_text = get_weekly_summary(entries)
    summary_window = tk.Toplevel(root)
    summary_window.title("Weekly Reflection 💙")
    summary_window.geometry("400x300")
    summary_window.resizable(False, False)

    title = tk.Label(
    summary_window,
    text = "Weekly Reflection",
    font = ("Helvetica", 14, "bold"), 
    fg = "#1976d2"
    )

    title.pack(pady=10)

    close_button = tk.Button(
        summary_window,
        text = "Close",
        command = summary_window.destroy,
        width = 15,
        background= "#2e7d32"
    )

    close_button.pack(pady = 10)
    

    summary_label = tk.Label(
        summary_window,
        text = summary_text,
        font = ("Helvetica", 10),
        wraplength = 340,
        justify = "left"
    )
    summary_label.pack(pady=10, padx=15)
    #--- This widget 'button' is ouside the function as it belongs to the main window(root), clicking it calls the function
summary_button = tk.Button(
    root,
    text = "View Weekly Summary",
    command = show_weekly_summary,  # will create this function later
    width = 20,
    fg = "#1976d2"
    )
summary_button.pack(pady = 5)
    
#---------------------------------------------MOOD CHART BUTTON-----------------------------------------
def show_mood_chart():
    """The below lines shows functions passing each other data to finally plot the chart using matplotlib"""
    entries = load_moods()
    week_entries = get_last_7days(entries)
    analysis_data = analyze_week(week_entries)
    plot_weekly_mood_chart(analysis_data)
chart_button = tk.Button(
        root,
        text = "View Mood Chart",
        command = show_mood_chart,
        width = 20
    )
chart_button.pack(pady = 5)

#------------------------------------------------ETHICAL DISCLAIMER---------------------------------------
disclaimer = tk.Label(
    root,
    text = "This app supports emotional awareness. \n Not a medical tool",
    font = ("Helvetica", 8),
    fg = "gray"
)
disclaimer.pack(side = "bottom", pady = 20)

root.mainloop()  #Starts the Tkinter event loop, which waits for user interaction