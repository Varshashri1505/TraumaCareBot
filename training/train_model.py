import pandas as pd

from sklearn.metrics import classification_report
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load cleaned dataset
df = pd.read_csv("dataset/cleaned_train.csv")

# Inputs (sentences)
X = df["text"]

# Outputs (emotion labels)
y = df["emotion"]

# STEP 1: Split RAW TEXT first (No Data Leakage)
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# STEP 2: Create TF-IDF Vectorizer
vectorizer = TfidfVectorizer(
    ngram_range=(1, 2),
    min_df=2,
    max_df=0.95
)

# STEP 3: Learn vocabulary ONLY from training data
X_train_tfidf = vectorizer.fit_transform(X_train)

# STEP 4: Apply same vocabulary to test data
X_test_tfidf = vectorizer.transform(X_test)

# STEP 5: Create Model
model = LogisticRegression(
    max_iter=1000,
    class_weight="balanced"
)

# STEP 6: Train Model
model.fit(X_train_tfidf, y_train)

# STEP 7: Predict
predictions = model.predict(X_test_tfidf)

# STEP 8: Accuracy
accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:", round(accuracy * 100, 2), "%")

# Classification Report
print("\nClassification Report:\n")
print(classification_report(y_test, predictions))