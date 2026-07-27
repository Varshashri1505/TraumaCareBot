import random
from features.conversation_state import get_topic

responses = {

    "joy":
    "That's wonderful to hear! Keep enjoying the positive moments in your day.",

    "sadness":
    "I'm sorry you're feeling this way. Remember that difficult moments pass. Would you like to talk more about it?",

    "fear":
    "It sounds like you're feeling anxious or worried. Try taking a few deep breaths and focus on one step at a time.",

    "anger":
    "I understand you're frustrated. Taking a short break and expressing your thoughts calmly may help.",

    "love":
    "That's a warm and meaningful feeling. Positive relationships can be a great source of strength.",

    "surprise":
    "That sounds unexpected! Sometimes surprising moments can teach us something new."

}
context_responses = {

    "crisis":
    "I am very concerned about your safety. Please contact a trusted person, family member, emergency service, or crisis helpline immediately.",

    "accident": [

        "I'm sorry to hear about your accident. I hope you're recovering well. How are you feeling today?",

        "That must have been a difficult experience. Recovery takes time, so remember to be patient with yourself. Are you experiencing any pain?",

        "Accidents can affect both your body and your emotions. If you'd like, you can tell me more about what happened."

    ],

    "depression": [

        "I'm sorry you're going through such a difficult time. You don't have to face these feelings alone.",

        "It sounds like you're having a hard time. Talking with someone you trust can really help.",

        "Remember that asking for support is a sign of strength. You deserve care and understanding."

    ],

    "anxiety": [

        "Feeling anxious can be overwhelming. Try taking slow, deep breaths and focus on one step at a time.",

        "It's okay to feel anxious sometimes. You're not alone, and talking about it can often help.",

        "Anxiety can feel difficult, but taking things one small step at a time may make it easier. Would you like to tell me what's worrying you?"

    ],

    "surgery": [

        "It is completely normal to feel nervous before surgery. Many people experience anxiety before medical procedures.",

        "Feeling anxious before surgery is completely understandable. You're not alone, and it's okay to talk about your concerns.",

        "Many people feel nervous before surgery. Taking things one step at a time and speaking openly with your healthcare team can help."

    ],

    "hospital": [

        "Hospital situations can be emotionally stressful. Stay in touch with your medical team and remember to take care of yourself too.",

        "Being in a hospital can feel overwhelming. Lean on your support system and don't hesitate to ask your healthcare team questions.",

        "Hospital visits can be challenging. Remember that seeking treatment is an important step toward recovery."

    ],

    "injury": [

        "Recovering from an injury takes time. Be patient with yourself and follow your treatment plan.",

        "Healing doesn't happen overnight. Every small improvement is a step forward in your recovery.",

        "Take your recovery one day at a time. Rest and following medical advice are important."

    ],

    "recovery": [

        "Recovery is a journey, and every small step forward matters. Keep believing in your progress.",

        "Healing takes time. Celebrate even the smallest improvements along the way.",

        "You're making progress, even if it doesn't always feel that way. Recovery happens one step at a time."

    ],

    "pain": [

        "I'm sorry you're experiencing pain. Make sure to get enough rest and follow your healthcare provider's advice.",

        "Pain can be difficult to cope with. If it becomes severe or doesn't improve, it's important to consult your healthcare provider.",

        "I understand that pain can be exhausting. Be kind to yourself and don't hesitate to seek medical advice if needed."

    ],
}

def get_response(emotion, context, history):

    # If current context is general,
    # use the last meaningful context

    if context == "general":

        topic = get_topic()

        if topic and topic in context_responses:

            previous_response = context_responses[topic]

            if isinstance(previous_response, list):
                previous_response = random.choice(previous_response)

            return (
                f"Earlier, you mentioned your {topic}. "
                + previous_response
            )

        # Fallback to history if no active topic
        for item in reversed(history):

            if (
                item["context"] != "general"
                and item["context"] in context_responses
            ):

                previous_response = context_responses[item["context"]]

                if isinstance(previous_response, list):
                    previous_response = random.choice(previous_response)

                return (
                    f"Earlier, you mentioned your {item['context']}. "
                    + previous_response
                )
    # Context-based response

    if context in context_responses:

        response = context_responses[context]

        if isinstance(response, list):
            selected = random.choice(response)
            return selected

        return response

    # Emotion-based response

    response = responses.get(
        emotion,
        "I'm here to listen and support you."
    )

    if isinstance(response, list):
        return random.choice(response)

    return response