import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer

# Load cleaned dataset
df = pd.read_csv("dataset/cleaned_train.csv")

# Take first 5 sentences
sample_texts = df["text"].head(5)

print("Original Text:\n")
print(sample_texts)

# Create TF-IDF object
vectorizer = TfidfVectorizer()

# Convert text to numerical vectors
X = vectorizer.fit_transform(sample_texts)

print("\nTF-IDF Matrix Shape:")
print(X.shape)

print("\nVocabulary:")
print(vectorizer.get_feature_names_out())