import joblib
from config import DEBUG, VOICE_MODE
from voice.voice_output import speak
from voice.voice_input import listen
from ai.context_detector import detect_context
from ai.response_generator import get_response
from ai.memory import remember, get_history
from features.daily_checkin import daily_check_in
from features.medication_reminder import is_medication_request
from features.conversation_state import (
    set_topic,
    conversation_state
)


# Load saved vectorizer
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

# Load saved model
model = joblib.load("models/emotion_model.pkl")


print("═══════════════════════════════════════")
print("🤖 TraumaCare Recovery Companion")
print("I'm here to support you during your recovery.")
print("═══════════════════════════════════════")

greeting = daily_check_in()

print("TraumaCare Bot:", greeting)
speak(greeting)

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

    # Check if the conversation state is None and if the user is asking for a medication reminder
    if conversation_state["mode"] is None:

        if is_medication_request(text):

            conversation_state["mode"] = "medicine"
            conversation_state["medicine"] = None
            conversation_state["time"] = None
            conversation_state["frequency"] = None

            print("TraumaCare Bot: Which medicine should I remind you about?")
            speak("Which medicine should I remind you about?")

            continue

    # User is telling the medicine name
    if conversation_state["mode"] == "medicine":

        conversation_state["medicine"] = text

        conversation_state["mode"] = "time"

        print("TraumaCare Bot: What time should I remind you?")
        speak("What time should I remind you?")

        continue

    # User is telling the reminder time
    if conversation_state["mode"] == "time":

        conversation_state["time"] = text

        conversation_state["mode"] = "frequency"

        print("TraumaCare Bot: How often should I remind you? (Example: every 6 hours)")
        speak("How often should I remind you? For example, every 6 hours.")

        continue
    # User is telling the reminder frequency
    if conversation_state["mode"] == "frequency":

        conversation_state["frequency"] = text

        from features.medication_reminder import create_reminder

        reply = create_reminder(
            conversation_state["medicine"],
            conversation_state["time"],
            conversation_state["frequency"]
        )

        print("TraumaCare Bot:", reply)
        speak(reply)

        # Reset conversation state
        conversation_state["mode"] = None
        conversation_state["medicine"] = None
        conversation_state["time"] = None
        conversation_state["frequency"] = None

        continue
    
    text_vector = vectorizer.transform([text])

    emotion = model.predict(text_vector)[0]

    probabilities = model.predict_proba(text_vector)[0]

    confidence = max(probabilities) * 100

    context = detect_context(text)
    if context != "general":
        set_topic(context)


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