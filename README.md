# 🩺 TraumaCare Bot

## NLP-Based Emotional and Physical Recovery Companion Robot

### Major Project – Artificial Intelligence & Data Science

---

# 📌 Project Overview

TraumaCare Bot is an intelligent AI-powered companion designed to provide emotional support and assistance during physical and psychological recovery. The project combines Natural Language Processing (NLP), Machine Learning, context detection, and conversation memory to understand user emotions and trauma-related situations and generate supportive responses.

Unlike a traditional emotion classifier, TraumaCare Bot analyzes both the user's emotional state and the conversation context to deliver more meaningful and personalized interactions. The long-term vision is to integrate this system into a voice-enabled companion robot for trauma care and rehabilitation.

---

# 🎯 Objectives

- Detect emotions from user text using Machine Learning.
- Identify trauma-related contexts such as injury, surgery, anxiety, depression, crisis, and recovery.
- Generate context-aware and emotionally supportive responses.
- Maintain short-term conversation memory for follow-up interactions.
- Build a foundation for future voice-enabled robotic assistance.

---

# 🛠 Technologies Used

## Programming Language

- Python

## Machine Learning & NLP

- Scikit-Learn
- TF-IDF Vectorization
- Logistic Regression
- LinearSVC (Best Model)

## Data Processing

- Pandas
- NumPy

## Model Storage

- Joblib

## Development Tools

- VS Code
- Git
- GitHub

---

# 📂 Dataset

Emotion Classification Dataset

### Emotion Classes

- Joy
- Sadness
- Fear
- Anger
- Love
- Surprise

### Dataset Size

- 16,000 Samples

---

# 📁 Project Structure

```
TraumaCareBot/
│
├── dataset/
├── docs/
├── models/
├── presentation/
├── reports/
├── src/
│   ├── preprocess.py
│   ├── eda.py
│   ├── train_svm.py
│   ├── save_model.py
│   ├── emotion_detector.py
│   ├── context_detector.py
│   ├── response_generator.py
│   ├── memory.py
│   └── chatbot.py
│
├── tests/
├── requirements.txt
├── .gitignore
└── README.md
```

---

# ✅ Current Progress

## Data Processing

- ✔ Dataset Collection
- ✔ Exploratory Data Analysis (EDA)
- ✔ Data Cleaning & Preprocessing

---

## Machine Learning

- ✔ TF-IDF Feature Extraction
- ✔ Logistic Regression Model
- ✔ LinearSVC Model
- ✔ Model Evaluation
- ✔ Model Saving using Joblib

### Best Performing Model

**LinearSVC**

**Accuracy:** **88.94%**

---

## Emotion Detection

The chatbot can identify six emotions:

- Joy
- Sadness
- Fear
- Anger
- Love
- Surprise

---

## Context Detection

Implemented rule-based trauma context detection using medical and emotional keywords.

Supported contexts include:

- Anxiety
- Depression
- Crisis
- Surgery
- Hospital
- Injury
- Recovery

---

## Response Generation

Implemented intelligent response generation based on:

- Predicted Emotion
- Detected Context

Trauma-related contexts are prioritized over emotion prediction to provide more appropriate responses.

---

## Conversation Memory

Implemented short-term conversation memory.

The chatbot stores:

- User Message
- Predicted Emotion
- Detected Context

This enables the chatbot to remember previous conversation topics and provide context-aware follow-up responses.

Example:

```
User:
I have surgery tomorrow.

User:
What should I do?

Bot:
Based on what you shared earlier...
```

---

## Interactive Console Chatbot

Implemented an end-to-end chatbot capable of:

- Accepting user input
- Detecting emotion
- Detecting trauma context
- Generating intelligent responses
- Remembering previous conversation

---

# 📊 Machine Learning Pipeline

```
User Input
        │
        ▼
Text Preprocessing
        │
        ▼
TF-IDF Vectorization
        │
        ▼
LinearSVC Emotion Detection
        │
        ▼
Context Detection
        │
        ▼
Conversation Memory
        │
        ▼
Response Generator
        │
        ▼
Final Chatbot Response
```

---

# 🚀 Features Implemented

- Emotion Detection
- Context Detection
- Context-Aware Responses
- Crisis Detection
- Depression Detection
- Surgery & Hospital Support
- Injury & Recovery Support
- Conversation Memory
- Interactive Console Chatbot

---

# 🔮 Future Development

- Persistent Conversation Memory
- Voice Input (Speech-to-Text)
- Voice Output (Text-to-Speech)
- Graphical User Interface (GUI)
- Robotic Integration
- Real-Time Voice Conversation
- Healthcare Sensor Integration
- Cloud Deployment
- Personalized Recovery Assistance

---

# 👩‍💻 Author

**Varshashri Nagapuri**

B.Tech – Artificial Intelligence & Data Science

Major Project: **TraumaCare Bot – NLP-Based Emotional and Physical Recovery Companion Robot**
