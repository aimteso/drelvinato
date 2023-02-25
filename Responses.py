from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("salam", "hi", "slm", "hello",):
        return "Salam, Sehetiniz necedi?"

    if user_message in ("sen kimsen?", "sen kimsen", "hru", "who are you", "who are you?",):
        return "Men Sizin meslehetciniz Dr.Elvinato!"

    if user_message in ("time", "time?", "saat necedi", "saat necedi?",):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M")

        return str(date_time)

    return "Sizi anlamadim."
