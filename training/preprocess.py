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

# Remove duplicate rows
df = df.drop_duplicates()

# Convert text to lowercase
df["text"] = df["text"].str.lower()

# Remove extra spaces
df["text"] = df["text"].str.strip()

print(df.head())

print("\nRows after cleaning:", len(df))

df.to_csv("dataset/cleaned_train.csv", index=False)

print("\nCleaned dataset saved successfully!")