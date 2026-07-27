import json
import os

REMINDER_FILE = "data/reminders.json"

#load remainder model
def load_reminders():

    if not os.path.exists(REMINDER_FILE):
        return []

    with open(REMINDER_FILE, "r") as file:
        return json.load(file)

#save remainder model
def save_reminders(reminders):

    with open(REMINDER_FILE, "w") as file:
        json.dump(reminders, file, indent=4)

#add a new reminder
def add_reminder(medicine, time, frequency):

    reminders = load_reminders()

    reminders.append({

        "medicine": medicine,

        "time": time,

        "frequency": frequency

    })

    save_reminders(reminders)

#create a new reminder
def create_reminder(medicine, time, frequency):

    add_reminder(
        medicine,
        time,
        frequency
    )

    return (
        f"Okay! I'll remind you to take "
        f"{medicine} every {frequency} starting at {time}."
    )

#remainder request detection
def is_medication_request(text):

    text = text.lower()

    keywords = [
        "remind me",
        "medicine",
        "medication",
        "tablet",
        "pill"
    ]

    return any(word in text for word in keywords)
