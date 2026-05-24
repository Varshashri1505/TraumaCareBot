# Trauma-related keywords

trauma_keywords = {

    "crisis": [
        "kill myself",
        "suicide",
        "end my life",
        "want to die",
        "self harm"
    ],

    "depression": [
        "depressed",
        "depression",
        "hopeless",
        "worthless",
        "empty",
        "lonely"
    ],

    "anxiety": [
        "anxiety",
        "anxious",
        "panic",
        "worried",
        "nervous",
        "tense",
        "scared"
    ],

    "surgery": [
        "surgery",
        "operation",
        "procedure"
    ],

    "hospital": [
        "hospital",
        "doctor",
        "nurse",
        "clinic",
        "ward"
    ],

    "injury": [
        "injury",
        "wound",
        "fracture",
        "bleeding",
        "burn"
    ],

    "pain": [
        "pain",
        "hurt",
        "aching",
        "sore"
    ],

    "recovery": [
        "recovery",
        "healing",
        "rehabilitation"
    ],

    "accident": [
        "accident",
        "crash",
        "fall",
        "collision"
    ],

    "medication": [
        "medicine",
        "medication",
        "tablet",
        "drug"
    ]
}


def detect_context(text):

    text = text.lower()

    for category, words in trauma_keywords.items():

        for word in words:

            if word in text:
                return category

    return "general"


"""# Testing

user_text = input("Enter sentence: ")

context = detect_context(user_text)

print("Detected Context:", context)"""