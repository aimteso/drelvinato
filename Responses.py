from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hi", "hello", "hey"):
        return "Hello there!"

    if user_message in ("what is your name", "what's your name", "who are you"):
        return "My name is Bot, nice to meet you!"

    if user_message in ("time", "what time is it", "what's the time", "tell me the time"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M")

        return str(date_time)

    return "Sorry, I didn't understand what you said."
