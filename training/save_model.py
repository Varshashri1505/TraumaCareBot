import pandas as pd
import joblib

from sklearn.calibration import CalibratedClassifierCV
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC

# Load cleaned dataset
df = pd.read_csv("dataset/cleaned_train.csv")

# Inputs and labels
X = df["text"]
y = df["emotion"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# TF-IDF
vectorizer = TfidfVectorizer(
    ngram_range=(1, 2),
    min_df=2,
    max_df=0.95
)

X_train_tfidf = vectorizer.fit_transform(X_train)

# Best model
base_model = LinearSVC(
    class_weight="balanced",
    random_state=42
)

model = CalibratedClassifierCV(
    estimator=base_model,
    cv=5
)

# Train
model.fit(X_train_tfidf, y_train)

# Save vectorizer
joblib.dump(
    vectorizer,
    "models/tfidf_vectorizer.pkl"
)

# Save model
joblib.dump(
    model,
    "models/emotion_model.pkl"
)

print("Model saved successfully!")