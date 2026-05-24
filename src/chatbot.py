import joblib
from context_detector import detect_context

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
context_responses = {

    "crisis":
    "I am very concerned about your safety. Please contact a trusted person, family member, emergency service, or crisis helpline immediately.",

    "depression":
    "I'm sorry you're going through such a difficult time. You do not have to face these feelings alone. Consider talking with someone you trust or a mental health professional.",

    "anxiety":
    "Feeling anxious can be overwhelming. Try taking slow deep breaths and focus on one step at a time.",

    "surgery":
    "It is completely normal to feel nervous before surgery. Many people experience anxiety before medical procedures.",

    "hospital":
    "Hospital visits can be stressful. Make sure to follow your doctor's advice and take care of yourself.",

    "injury":
    "Recovering from an injury takes time. Be patient with yourself and follow the recommended treatment plan.",

    "recovery":
    "Recovery is a journey. Every small step forward is progress and should be appreciated."
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

    probabilities = model.predict_proba(text_vector)[0]

    confidence = max(probabilities) * 100

    context = detect_context(text)

    print("\nDetected Emotion:", emotion)

    print("Confidence:",
        round(confidence, 2), "%")

    print("Detected Context:", context)   
    if context in context_responses:

        print("TraumaCare Bot:",
            context_responses[context])

    else:

        print("TraumaCare Bot:",
            responses[emotion])
    print()