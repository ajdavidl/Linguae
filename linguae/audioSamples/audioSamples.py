"""
Module to search audio on internet
"""

import webbrowser
import re


def forvo(language, word):
    """
    Open browser and query audio samples from Forvo site (https://forvo.com).

    Parameters
    ----------
    language : str
        Language of the word.
        example: 'en', 'pt', 'es', 'fr', 'de', 'ro', 'ca', 'it', 'nl'
    word : str
        word to be queried.

    See Also
    --------
    linguae.googleImages : Open browser and query Google Images.
    linguae.duckduckGoImages : Open browser and query Duckduckgo images.
    linguae.tts : Convert text to speech.

    Examples
    --------
    >>> linguae.forvo('en','language')
    https://forvo.com/search/language/en/
    >>> linguae.forvo('pt','idioma')
    https://forvo.com/search/idioma/pt/
    """
    if ' ' in word:
        word = re.sub(' ', '+', word)
    url = 'https://forvo.com/search/%s/%s/' % (word, language)
    print(url)
    webbrowser.open_new_tab(url)
