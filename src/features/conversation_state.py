print("conversation_state module loaded")
print(globals())

current_topic = None


def set_topic(topic):
    global current_topic
    current_topic = topic


def get_topic():
    return current_topic


def clear_topic():
    global current_topic
    current_topic = None

conversation_state = {
    "mode": None,
    "medicine": None,
    "time": None,
    "frequency": None
}