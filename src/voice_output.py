import pyttsx3

engine = pyttsx3.init()

# Voice settings
engine.setProperty("rate", 165)      # Speaking speed
engine.setProperty("volume", 1.0)    # Volume (0.0 to 1.0)

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Hello, I am TraumaCare Bot. Nice to meet you.")