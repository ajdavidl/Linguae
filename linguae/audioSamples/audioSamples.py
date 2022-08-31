"""
Module to search audio on internet
"""

import webbrowser
import re


def forvo(language, word):
    """
        Open browser and query Forvo audios

        Parameters
        ----------
        language : str
            Language of the word.
            example: 'en', 'pt', 'es', 'fr', 'de', 'ro', 'ca', 'it', 'nl'

        word : str
            word to be queried.

        """
    if ' ' in word:
        word = re.sub(' ', '+', word)
    url = 'https://forvo.com/search/%s/%s/' % (word, language)
    print(url)
    webbrowser.open_new_tab(url)
