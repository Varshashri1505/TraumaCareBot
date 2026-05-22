import pandas as pd

texts = []
emotions = []

with open("dataset/train.txt", "r", encoding="utf-8") as file:
    for line in file:

        line = line.strip()

        if ";" not in line:
            continue

        text, emotion = line.rsplit(";", 1)

        texts.append(text)
        emotions.append(emotion)

df = pd.DataFrame({
    "text": texts,
    "emotion": emotions
})

print("\n===== FIRST 5 RECORDS =====")
print(df.head())

print("\n===== DATASET SHAPE =====")
print(df.shape)

print("\n===== EMOTION DISTRIBUTION =====")
print(df["emotion"].value_counts())

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== DUPLICATE RECORDS =====")
print(df.duplicated().sum())