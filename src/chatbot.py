import joblib
from config import DEBUG, VOICE_MODE
from voice.voice_output import speak
from voice.voice_input import listen
from ai.context_detector import detect_context
from ai.response_generator import get_response
from ai.memory import remember, get_history

# Load saved vectorizer
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

# Load saved model
model = joblib.load("models/emotion_model.pkl")


print("═══════════════════════════════════════")
print("🤖 TraumaCare Recovery Companion")
print("I'm here to support you during your recovery.")
print("═══════════════════════════════════════")


while True:

    if VOICE_MODE:
        text = listen()
        print("DEBUG - Returned from listen():", text)

        # If speech wasn't recognized, listen again
        if text == "":
            continue
    else:
        text = input("You: ")

    if text.lower() == "exit":
        goodbye = "Take care and have a good day! I wish you a smooth recovery."

        print("TraumaCare Bot:", goodbye)
        speak(goodbye)

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
    speak(reply)

    remember(
        text,
        emotion,
        context
    )

    print("Loop completed.")