#HELPERS(SUMMARY TEXT GENERATOR)
from datetime import date, timedelta
from collections import Counter
"""
Counter is a special dictionary in which it automatically counts occurrences of each item in a list.
"""

def get_weekly_summary(entries):
    """
    entries: list of[date, mood, notes]
    returns a reflection string summarizing the week's moods for UI.
    """
    today = date.today()
    one_week_ago = today - timedelta(days=7)

    weekly_moods = []
    for entry in entries:
        if len(entry) < 2:  # Skip malformed entries but should be able to take in entries(mood, date) notes can be an exception
            continue
        entry_date = date.fromisoformat(entry[0])
        if entry_date >= one_week_ago:
            weekly_moods.append(entry[1])

    if not weekly_moods:
        return "No mood entries found for the past week.🌱"
    
    mood_counts = Counter(weekly_moods)
    most_common_mood, count = mood_counts.most_common(1)[0]

    return (
        f"Weekly Reflection 💙\n\n"
        f"You logged {len(weekly_moods)} entries this week.\n"
        f"Your most frequent emotion was:\n\n"
        f"{most_common_mood} ({count} times)\n\n"
        f"Thank you for taking time to check in with yourself 🌸"
    )
