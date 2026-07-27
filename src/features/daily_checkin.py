import random


greetings = [

    "Hello! I'm glad to see you again. How has your recovery been today?",

    "Welcome back. How are you feeling today?",

    "It's nice to talk with you again. How has your day been so far?",

    "Hello! I hope you're doing well. How has your recovery been today?"
]


def daily_check_in():

    return random.choice(greetings)