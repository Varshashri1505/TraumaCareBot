
# Stores conversation history

conversation_history = []


def remember(message, emotion, context):

    conversation_history.append({

        "message": message,

        "emotion": emotion,

        "context": context

    })


def get_history():

    return conversation_history