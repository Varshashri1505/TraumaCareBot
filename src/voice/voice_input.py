import speech_recognition as sr

recognizer = sr.Recognizer()

def listen():

    with sr.Microphone() as source:

        print("🎤 Listening...")

        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        try:
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=10
            )
        except sr.WaitTimeoutError:
            print("No speech detected.")
            return ""

    try:

        text = recognizer.recognize_google(audio)

        print("You:", text)

        return text.lower()

    except sr.UnknownValueError:

        print("Sorry, I couldn't understand.")
        return ""

    except sr.RequestError:

        print("Speech service unavailable.")
        return ""