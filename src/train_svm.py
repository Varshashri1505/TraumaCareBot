import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score, classification_report

# Load cleaned dataset
df = pd.read_csv("dataset/cleaned_train.csv")

# Input text
X = df["text"]

# Emotion labels
y = df["emotion"]

# Split raw text first (No Data Leakage)
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(
    ngram_range=(1, 2),
    min_df=2,
    max_df=0.95
)

# Learn vocabulary only from training data
X_train_tfidf = vectorizer.fit_transform(X_train)

# Apply same vocabulary to test data
X_test_tfidf = vectorizer.transform(X_test)

# Create SVM Model
model = LinearSVC(
    class_weight="balanced",
    random_state=42
)

# Train Model
model.fit(X_train_tfidf, y_train)

# Predict
predictions = model.predict(X_test_tfidf)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:", round(accuracy * 100, 2), "%")

# Classification Report
print("\nClassification Report:\n")
print(classification_report(y_test, predictions))