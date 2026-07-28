<div align="center">

# 🤖 TraumaCare Bot

### NLP-Based Emotional and Physical Recovery Companion Robot

*An AI-powered companion robot designed to support trauma patients through emotional care, intelligent conversations, personalized recovery guidance, and voice-based assistance.*

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--learn-orange)
![NLP](https://img.shields.io/badge/NLP-Natural%20Language%20Processing-green)
![Robotics](https://img.shields.io/badge/Robotics-Raspberry%20Pi-red)
![Status](https://img.shields.io/badge/Status-Under%20Development-yellow)

</div>

---

# 📖 About the Project

TraumaCare Bot is an AI-powered Emotional and Physical Recovery Companion Robot developed to support patients recovering from accidents, surgeries, fractures, burns, and emotionally challenging situations.

Unlike conventional healthcare chatbots, TraumaCare Bot is envisioned as an intelligent stationary companion robot capable of understanding patient emotions, maintaining personalized conversations, monitoring recovery progress, providing medication reminders, and offering continuous emotional support through natural voice interaction.

The project combines **Artificial Intelligence (AI), Natural Language Processing (NLP), Machine Learning, Voice Technologies, IoT, and Robotics** to bridge the gap between traditional healthcare and continuous patient assistance.

---

# 🎯 Objectives

- Provide continuous emotional support to trauma patients.
- Assist patients during physical recovery.
- Detect user emotions using Natural Language Processing.
- Conduct daily recovery check-ins.
- Provide medication reminders.
- Maintain conversation memory for personalized interactions.
- Encourage healthy recovery habits.
- Reduce caregiver workload.
- Improve patient independence.
- Deliver intelligent voice-based assistance.

---

# ✨ Key Features

## 🤖 Intelligent Companion Robot

- AI-powered stationary healthcare companion
- Interactive LCD face display
- Voice-controlled communication
- Context-aware conversations
- Personalized patient interaction

---

## 🧠 Artificial Intelligence

- Emotion Detection
- Natural Language Processing
- Context Detection
- Conversation Memory
- Personalized Response Generation

---

## 🎤 Voice Assistant

- Speech-to-Text
- Text-to-Speech
- Hands-free Voice Interaction
- Natural Conversations

---

## ❤️ Patient Care

- Medication Reminder System
- Daily Recovery Check-ins
- Emotional Support
- Recovery Guidance
- Motivational Conversations
- Calming Music Support

---

## 🚨 Safety Features

- Crisis Detection
- Distress Identification
- Intelligent Recovery Assistance
- Caregiver Notification *(Future Enhancement)*

---

# 🏗️ Proposed System Architecture

```text
                           Patient
                               │
                      Voice / Text Input
                               │
                               ▼
                   Speech Recognition Module
                               │
                               ▼
                 Natural Language Processing
                               │
          ┌────────────────────┼────────────────────┐
          │                    │                    │
          ▼                    ▼                    ▼
 Emotion Detection      Context Detection   Conversation Memory
          │                    │                    │
          └────────────────────┼────────────────────┘
                               │
                               ▼
                    Intelligent Decision Engine
                               │
        ┌───────────────┬───────────────┬───────────────┐
        │               │               │
        ▼               ▼               ▼
 Medication       Daily Check-in   Calming Music
 Reminder
        │
        ▼
                  Personalized Voice Response
                               │
                               ▼
                         Speaker Output
```

---

# 🤖 Robot Hardware Architecture

```text
                    TraumaCare Bot
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
 Raspberry Pi        LCD Touch Display     Speaker
        │                  │
        ▼                  ▼
 USB Microphone      Robot Face Interface
        │
        ▼
 Built-in Wi-Fi
        │
        ▼
 Future Expansion
        │
        ▼
ESP32 + IoT Devices (Optional)
```

---

# 🔧 Hardware Requirements

| Component | Description |
|-----------|-------------|
| Raspberry Pi 5 | Main controller running AI, NLP, voice assistant, and robot logic |
| USB Microphone | Captures patient voice commands |
| Speaker | Delivers voice responses, reminders, and calming music |
| 5–7 inch LCD Touch Display | Displays facial expressions, reminders, and robot status |
| Wi-Fi Module (Built-in) | Provides internet connectivity and cloud communication |
| Rechargeable Battery / Power Adapter | Powers the robot during operation |
| Robot Enclosure | Houses all hardware components in a companion robot body |
| ESP32 *(Future Expansion)* | Supports additional IoT devices and peripheral integration |

---

# 💻 Software Requirements

| Software | Purpose |
|----------|---------|
| Python 3.11+ | Core programming language |
| Scikit-learn | Emotion detection and NLP model development |
| SpeechRecognition | Converts speech into text |
| Edge-TTS | Converts text into natural speech |
| Visual Studio Code | Development environment |
| Git & GitHub | Version control and collaboration |
| Raspberry Pi OS | Operating system for robot deployment |

---

# 🧠 Core Modules

- Emotion Detection Module
- NLP Processing Engine
- Context Detection Module
- Conversation Memory Module
- Voice Assistant Module
- Medication Reminder Module
- Daily Recovery Check-in Module
- Calming Music Module
- Crisis Detection Module
- Robot Interface Module

---

# ⚙️ System Workflow

```text
Patient
   │
   ▼
Voice Input
   │
   ▼
Speech Recognition
   │
   ▼
Emotion Detection
   │
   ▼
Context Analysis
   │
   ▼
Conversation Memory
   │
   ▼
Decision Engine
   │
   ├────────► Medication Reminder
   │
   ├────────► Daily Check-in
   │
   ├────────► Calming Music
   │
   └────────► Emotional Support
               │
               ▼
        Text-to-Speech
               │
               ▼
            Speaker
               │
               ▼
            Patient
```

---

# 🛠️ Technologies Used

### Programming Language

- Python

### Artificial Intelligence

- Machine Learning
- Scikit-learn
- TF-IDF Vectorizer
- Logistic Regression / LinearSVC

### Natural Language Processing

- NLP
- Emotion Detection
- Context Detection
- Conversation Memory

### Voice Technologies

- SpeechRecognition
- Edge-TTS

### Robotics

- Raspberry Pi
- LCD Touch Display
- USB Microphone
- Speaker

### Development Tools

- Visual Studio Code
- Git
- GitHub

# 📂 Project Structure

```text
TraumaCareBot/
│
├── data/
│   ├── conversations.json
│   ├── reminders.json
│   └── emotion_dataset.csv
│
├── features/
│   ├── emotion_detection.py
│   ├── context_detection.py
│   ├── conversation_memory.py
│   ├── medication_reminder.py
│   ├── daily_checkin.py
│   ├── crisis_detection.py
│   ├── voice.py
│   └── music_player.py
│
├── models/
│   ├── emotion_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── hardware/
│   ├── raspberry_pi/
│   ├── esp32/
│   └── sensors/
│
├── utils/
│
├── main.py
├── config.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

# ⚙️ Installation

## Clone the Repository

```bash
git clone https://github.com/Varshashri1505/TraumaCareBot.git
```

Move into the project directory

```bash
cd TraumaCareBot
```

Install the required dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python main.py
```

---

# ▶️ Usage

After launching the application, users can interact with TraumaCare Bot using voice or text.

Example interactions include:

- Emotional support conversations
- Medication reminders
- Daily recovery check-ins
- Recovery guidance
- General healthcare assistance

---

# 💬 Example Conversation

```text
👤 User:
I feel anxious today.

🤖 TraumaCare Bot:
I'm sorry you're feeling anxious.
Would you like to talk about what happened today?

--------------------------------------------------

👤 User:
Remind me to take my medicine.

🤖 TraumaCare Bot:
Which medicine would you like me to remind you about?

👤 User:
Paracetamol

🤖 TraumaCare Bot:
At what time should I remind you?

👤 User:
6 PM

🤖 TraumaCare Bot:
How often should I remind you?

👤 User:
Every 8 hours

🤖 TraumaCare Bot:
Great! I'll remind you to take Paracetamol every 8 hours starting at 6 PM.
```

---

# 🤖 Robot Capabilities

The TraumaCare Bot is designed to function as a companion healthcare robot capable of:

- Understanding natural conversations
- Detecting patient emotions
- Remembering previous interactions
- Providing personalized emotional support
- Delivering medication reminders
- Conducting daily recovery check-ins
- Encouraging rehabilitation activities
- Playing calming music
- Responding using natural speech
- Supporting trauma recovery in home and hospital environments

---

# 🩺 Applications

- Trauma Recovery
- Post-Surgery Care
- Burn Recovery
- Fracture Rehabilitation
- Elderly Assistance
- Rehabilitation Centres
- Home Healthcare
- Hospitals
- Mental Wellness Support

---

# 📈 Current Development Status

## ✅ Completed

- Emotion Detection
- Natural Language Processing
- Context Detection
- Conversation Memory
- Voice Input
- Voice Output
- Medication Reminder System
- Daily Recovery Check-ins
- Crisis Detection

---

## 🚧 In Progress

- Raspberry Pi Integration
- Robot User Interface
- LCD Face Display
- Voice Optimization
- Hardware Assembly

---

## 🔮 Planned Enhancements

- ESP32 Integration
- Camera-based Emotion Recognition
- IoT Health Monitoring Sensors
- Doctor Dashboard
- Caregiver Mobile Application
- Cloud Database Integration
- Emergency Contact Notifications
- Wearable Device Connectivity
- Autonomous Navigation
- Smart Hospital Integration

---

# 🎯 Future Scope

The future vision of TraumaCare Bot is to evolve into a fully autonomous healthcare companion robot capable of assisting patients in hospitals, rehabilitation centres, and homes.

Future enhancements include:

- AI-powered facial emotion recognition
- Health monitoring through IoT sensors
- Heart Rate monitoring
- SpO₂ monitoring
- Body Temperature monitoring
- Fall Detection
- Automatic emergency alerts
- Caregiver dashboard
- Doctor portal
- Cloud synchronization
- Mobile application
- Smart home integration
- Multi-language support

---

# 📊 Advantages

- Continuous emotional support
- Personalized recovery assistance
- Intelligent voice interaction
- Reduces caregiver workload
- Improves medication adherence
- Enhances patient engagement
- Promotes emotional well-being
- Supports long-term recovery

---

# 👥 Team

| Name | Roll Number |
|------|-------------|
| **N. Varshashri** | **23AG1A7245** |
| **B. Bhavana** | **23AG1A7211** |
| **G. Koushik** | **24AG5A7203** |
| **L. Yeshwanth** | **23AG1A7231** |

---

# 🎓 Academic Information

**Project Title**

TraumaCare Bot: NLP-Based Emotional and Physical Recovery Companion Robot

**Department**

Artificial Intelligence & Data Science (AI&DS)

**Institution**

ACE Engineering College

**Batch**

05

---

# 📜 License

This project is developed for educational and research purposes as part of a Final Year Major Project.

---

# 🙏 Acknowledgements

We sincerely thank:

- ACE Engineering College
- Department of Artificial Intelligence & Data Science
- Our Project Guide
- Faculty Members
- Open-source Community
- Python Community
- Scikit-learn
- Raspberry Pi Foundation
- GitHub

---

<div align="center">

## ⭐ If you found this project interesting, consider giving it a Star!

### Thank you for visiting TraumaCare Bot ❤️

**Building Intelligent Healthcare with AI, NLP & Robotics**

</div>