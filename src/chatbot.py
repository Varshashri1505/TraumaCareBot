import joblib

# Load saved vectorizer
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

# Load saved model
model = joblib.load("models/emotion_model.pkl")

responses = {

    "joy":
    "That's wonderful to hear! Keep enjoying the positive moments in your day.",

    "sadness":
    "I'm sorry you're feeling this way. Remember that difficult moments pass. Would you like to talk more about it?",

    "fear":
    "It sounds like you're feeling anxious or worried. Try taking a few deep breaths and focus on one step at a time.",

    "anger":
    "I understand you're frustrated. Taking a short break and expressing your thoughts calmly may help.",

    "love":
    "That's a warm and meaningful feeling. Positive relationships can be a great source of strength.",

    "surprise":
    "That sounds unexpected! Sometimes surprising moments can teach us something new."
}

print("=== TraumaCare Bot ===")
print("Type 'exit' to quit.\n")

while True:

    text = input("You: ")

    if text.lower() == "exit":
        print("TraumaCare Bot: Take care and have a good day!")
        break

    text_vector = vectorizer.transform([text])

    emotion = model.predict(text_vector)[0]

    print("\nDetected Emotion:", emotion)
    print("TraumaCare Bot:", responses[emotion])
    print()