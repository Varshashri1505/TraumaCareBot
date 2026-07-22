import joblib
from config import DEBUG, VOICE_MODE
from voice_input import listen
from context_detector import detect_context
from response_generator import get_response
from memory import remember, get_history

# Load saved vectorizer
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

# Load saved model
model = joblib.load("models/emotion_model.pkl")


print("=== TraumaCare Bot ===")
print("Type 'exit' to quit.\n")

while True:

    if VOICE_MODE:
        text = listen()

        # If speech wasn't recognized, listen again
        if text == "":
            continue
    else:
        text = input("You: ")

    if text.lower() == "exit":
        print("TraumaCare Bot: Take care and have a good day!")
        break

    text_vector = vectorizer.transform([text])

    emotion = model.predict(text_vector)[0]

    probabilities = model.predict_proba(text_vector)[0]

    confidence = max(probabilities) * 100

    context = detect_context(text)


    if DEBUG:
        print("\nDetected Emotion:", emotion)

        print("Confidence:",
            round(confidence, 2), "%")

        print("Detected Context:", context)

    history = get_history()

    reply = get_response(
        emotion,
        context,
        history
    )

    print("TraumaCare Bot:", reply)

    remember(
        text,
        emotion,
        context
    )