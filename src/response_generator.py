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

    "depression":
    "I'm sorry you're going through such a difficult time. You do not have to face these feelings alone. Consider talking with someone you trust or a mental health professional.",

    "anxiety":
    "Feeling anxious can be overwhelming. Try taking slow deep breaths and focus on one step at a time.",

    "surgery":
    "It is completely normal to feel nervous before surgery. Many people experience anxiety before medical procedures.",

    "hospital":
    "Hospital situations can be emotionally stressful. Stay in touch with the medical team, support your loved one if applicable, and remember to take care of yourself during this difficult time.",

    "injury":
    "Recovering from an injury takes time. Be patient with yourself and follow the recommended treatment plan.",

    "recovery":
    "Recovery is a journey. Every small step forward is progress and should be appreciated.",

    "pain":
    "It sounds like you're experiencing pain. If it becomes severe or doesn't improve, please consult a healthcare professional and take proper rest."
}

def get_response(emotion, context, history):

    # If current context is general,
    # use the last meaningful context

    if context == "general":

        for item in reversed(history):

            if (
                item["context"] != "general" and item["context"] in context_responses
            ):

                return (
                    "Based on what you shared earlier, " + context_responses[item["context"]]
                )
    # Context-based response

    if context in context_responses:

        return context_responses[context]

    # Emotion-based response

    return responses.get(
        emotion,
        "I'm here to listen and support you."
    )