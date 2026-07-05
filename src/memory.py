conversation_history = []

def remember(message):

    conversation_history.append(message)
    
def get_history():

    return conversation_history