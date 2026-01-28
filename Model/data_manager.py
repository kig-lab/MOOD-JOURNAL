#Core code for saving and loading moods
import csv
from datetime import date

FILE_NAME = "moods.csv"

def save_mood(mood, notes):  #Sends data to the file
    """
    Save the mood and notes to a CSV file with the current date.
    """
    today = date.today().isoformat()

    #Append to CSV
    with open(FILE_NAME, "a", newline= "", encoding = "utf-8") as file: # With keyword is context manager that makes sure your file is closed even if forgotten
        writer = csv.writer(file)
        writer.writerow([today, mood, notes])

def load_moods(): # Brings data back into python so you can use it, like a printing history of your moods
    """
    Load all saved mood entries from the CSV file
    Returns a list of [date, mood, notes] entries.

    """
    moods = []

    try:
        with open(FILE_NAME, "r", newline = "", encoding = "utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                moods.append(row)  #Each row is a list [date, mood, notes] which is appended to the moods list

    except FileNotFoundError:
        #If the file does not exist, return an empty list
        pass
    return moods



  