"""
Module to translate sentences between languages.
"""
from textblob import TextBlob
import webbrowser
import re
from transformers import pipeline

TRANSLATOR = pipeline("translation", model="Helsinki-NLP/opus-mt-ine-ine")


def translate(from_language, to_language, text):
    """
    Translate text from one language to another.

    It uses the textblob package under the hood.

    Parameters
    ----------
    from_language : str
        Language of the text.
        example: 'en', 'pt', 'es', 'fr', 'de', 'ro', 'ca', 'it', 'nl'

    to_language : str
        Language that the text will be translated
        example: 'en', 'pt', 'es', 'fr', 'de', 'ro', 'ca', 'it', 'nl'

    text : str
        Text to be translated

    Returns
    -------
    str
        String with the text translated in the language asked.

    See Also
    --------
    linguae.googleTranslate : Open browser and query Google translate site.
    linguae.transformerTranslation : Translate text to other language.

    Examples
    --------
    >>> linguae.translate('pt','en','Aprender idiomas é divertido.')
    'Learning languages is fun.'
    """
    try:
        blob = TextBlob(text).translate(
            to=to_language, from_lang=from_language)
    except Exception as e:
        print("Error:", e)
        return
    return str(blob)


def googleTranslate(from_language, to_language, text):
    """
    Open browser and query Google translate site.

    Parameters
    ----------
    from_language : str
        Language of the text.
        example: 'en', 'pt', 'es', 'fr', 'de', 'ro', 'ca', 'it', 'nl'

    to_language : str
        Language that the text will be translated
        example: 'en', 'pt', 'es', 'fr', 'de', 'ro', 'ca', 'it', 'nl'

    text : str
        Text to be translated

    See Also
    --------
    linguae.translate : Translate text from one language to another.
    linguae.transformerTranslation : Translate text to other language.

    Examples
    --------
    >>> linguae.googleTranslate('pt','en','Aprender idiomas é divertido.')
    https://translate.google.com.br/?sl=pt&tl=en&text=Aprender%20idiomas%20é%20divertido.&op=translate
    """
    if ' ' in text:
        text = re.sub(' ', '%20', text)
    url = 'https://translate.google.com.br/?sl=%s&tl=%s&text=%s&op=translate' % (
        from_language, to_language, text)
    print(url)
    webbrowser.open_new_tab(url)


def transformerTranslation(to_language, texts):
    """
    Translate text to other language.

    It uses the transformer package with the Helsinki-NLP machine translation model under the hood.

    Parameters
    ----------
    to_language : str
        Language that the text will be translated - 3-letters code.
        example: 'eng', 'por', 'spa', 'fre', 'deu', 'ron', 'cat', 'ita'

    text : str or list of strings
        Texts to be translated

    Returns
    -------
    str or list of strings
        String with the text translated in the language asked.

    See Also
    --------
    linguae.translate : Translate text from one language to another.
    linguae.googleTranslate : Open browser and query Google translate site.

    Examples
    --------
    >>> linguae.transformerTranslation('eng','Ich bin hier.')
    "I'm here."
    >>> linguae.transformerTranslation('eng',['Estoy listo.','Me llamo Tom.'])
    ["I'm ready.", "I'm Tom."]
    """
    if type(texts) is str:
        text_out = TRANSLATOR(">>%s<< %s" % (to_language, texts))
        text_out = text_out[0]['translation_text']
        return(text_out)
    elif type(texts) is list:
        listSentences = [">>%s<< %s" % (to_language, text) for text in texts]
        text_out = TRANSLATOR(listSentences)
        text_out = [text_out[i]['translation_text']
                    for i in range(len(listSentences))]
        return(text_out)
