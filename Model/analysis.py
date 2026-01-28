#DATA ANALYSIS TOOL
from datetime import date, timedelta
from collections import Counter
import matplotlib.pyplot as plt

def get_last_7days(entries):
    """
    returns entries from the last 7 days
    """
    today = date.today()
    last_week = []  #list to hold entries from last 7 days which is currently empty

    for entry in entries:  #Loop to filter through the days within last 7 days
        if len(entry) < 2: #skip bad/incomplete entries
            continue
        try:
            entry_date = date.fromisoformat(entry[0])
        except ValueError:
            continue  #skip entries with invalid date format
        if today - timedelta(days=7) <= entry_date <= today:
            last_week.append(entry)
        
    return last_week

def analyze_week(entries):
    """
    Returns structured data(dictionary)for  further processing
    Meant to be used by other functions
    """
    if not entries:
        return None
    
    moods = [entry[1] for entry in entries]  # entry[1] meaning the mood from the entries [date, mood, notes] 
    mood_counts = Counter(moods)  # Creates a Counter like: {"😊 Happy": 3, "😢 Sad": 2}

    most_common = mood_counts.most_common(1)  # Returns a list of 1 tuple that is the most common mood
    most_common_mood = most_common[0][0] if most_common else "No Data" # Accesses the first element of the tuple which is the key mood name i.e 'happy'

    return{
        "days_logged": len(entries),
        "mood_counts": mood_counts,
        "most_common_mood": most_common_mood
    }

def plot_weekly_mood_chart(analysis_data):
    """
    Displays a bar chart of weekly mood count
    """
    if not analysis_data:
        return # No data to plot
    
    moods = list(analysis_data["mood_counts"].keys())
    counts = list(analysis_data["mood_counts"].values())

    plt.figure()
    plt.bar(moods, counts, color='skyblue')
    plt.title("Weekly Mood Distribution")
    plt.xlabel("Moods")
    plt.ylabel("Days")
    plt.tight_layout()
    plt.show()