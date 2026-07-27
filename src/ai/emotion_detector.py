import joblib

# Load saved vectorizer
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

# Load saved model
model = joblib.load("models/emotion_model.pkl")

# Take user input
text = input("Enter a sentence: ")

# Convert text to TF-IDF
text_vector = vectorizer.transform([text])

# Predict emotion
prediction = model.predict(text_vector)

print("\nPredicted Emotion:", prediction[0])