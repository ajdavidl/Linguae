from textblob import TextBlob

def translate(from_language, to_language, text):
    blob = TextBlob(text).translate(to=to_language, from_lang=from_language)
    return str(blob)