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
        "lonely",
        "helpless",
        "nothing matters",
        "lost hope",
        "giving up"
    ],

    "anxiety": [
        "anxiety",
        "anxious",
        "panic",
        "panicking",
        "worried",
        "worry",
        "nervous",
        "tense",
        "afraid",
        "scared",
        "frightened"
    ],

    "surgery": [
        "surgery",
        "operation",
        "procedure",
        "operate",
        "operated",
        "surgeon",
        "stitches",
        "stitch",
        "operation theatre"
    ],

    "hospital": [
        "hospital",
        "doctor",
        "doctors",
        "nurse",
        "clinic",
        "ward",
        "icu",
        "admitted",
        "admission",
        "patient",
        "medical"
    ],

    "injury": [
        "injury",
        "injured",
        "hurt",
        "hurts",
        "pain",
        "painful",
        "fracture",
        "broken",
        "sprain",
        "cut",
        "wound",
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
       
        "recover",
        "recovery",
        "recovering",
        "healing",
        "heal",
        "better",
        "improving"
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