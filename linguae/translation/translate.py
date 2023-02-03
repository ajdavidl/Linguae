"""
Module to translate sentences between languages.
"""
from textblob import TextBlob
import webbrowser
import re


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

    Examples
    --------
    >>> linguae.translate('pt','en','Aprender idiomas é divertido.')
    'Learning languages is fun.'
    """
    blob = TextBlob(text).translate(to=to_language, from_lang=from_language)
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
