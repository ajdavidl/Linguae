"""
Module with functions that queries dictionaries
"""

import webbrowser
import re


def priberam(word):
    """
        Open browser and query the Portuguese Priberam dictionary

        Parameters
        ----------
        word : str
            word

        """
    if ' ' in word:
        word = re.sub(' ', '-', word)
    url = 'https://dicionario.priberam.org/%s' % word
    print(url)
    webbrowser.open_new_tab(url)


def sinomimos(word):
    """
        Open browser and query the Portuguese Sinonimos dictionary

        Parameters
        ----------
        word : str
            word

        """
    word = re.sub(' ', '-', word)
    word = re.sub('ç', 'c', word)
    word = re.sub('á', 'a', word)
    word = re.sub('ã', 'a', word)
    word = re.sub('â', 'a', word)
    word = re.sub('é', 'e', word)
    word = re.sub('ê', 'e', word)
    word = re.sub('í', 'i', word)
    word = re.sub('ó', 'o', word)
    word = re.sub('õ', 'o', word)
    word = re.sub('ô', 'o', word)
    word = re.sub('ú', 'u', word)
    url = 'https://www.sinonimos.com.br/%s/' % word
    print(url)
    webbrowser.open_new_tab(url)


def linguee(from_language, to_language, word):
    """
        Open browser and query the multilingual Linguee dictionary

        Parameters
        ----------
        from_language : str
            Language of the text.
            examples: 'english', 'portuguese', 'spanish', 'french'

        to_language : str
            Language that the text will be translated
            examples: 'english', 'portuguese', 'spanish', 'french'

        word : str
            word

        """
    url = 'https://www.linguee.com/%s-%s/search?source=%s&query=%s' % (
        from_language, to_language, from_language, word)
    print(url)
    webbrowser.open_new_tab(url)


def glosbe(from_language, to_language, word):
    """
        Open browser and query the multilingual Glosbe dictionary

        Parameters
        ----------
        from_language : str
            Language of the text.
            examples: 'en', 'pt', 'es', 'fr'

        to_language : str
            Language that the text will be translated
            examples: 'en', 'pt', 'es', 'fr'

        word : str
            word

        """
    url = 'https://glosbe.com/%s/%s/%s' % (from_language, to_language, word)
    print(url)
    webbrowser.open_new_tab(url)


def dictionary_com(word):
    """
        Open browser and query the English dictionary.com

        Parameters
        ----------
        word : str
            word

        """
    url = 'https://www.dictionary.com/browse/%s' % word
    print(url)
    webbrowser.open_new_tab(url)


def thesaurus(word):
    """
        Open browser and query the English thesaurus dictionary

        Parameters
        ----------
        word : str
            word

        """
    url = 'https://www.thesaurus.com/browse/%s' % word
    print(url)
    webbrowser.open_new_tab(url)


def pons(from_language, to_language, word):
    """
        Open browser and query the multilingual Pons dictionary

        Parameters
        ----------
        from_language : str
            Language of the text.
            examples: 'english', 'portuguese', 'spanish', 'french', 'german'  

        to_language : str
            Language that the text will be translated
            examples: 'english', 'portuguese', 'spanish', 'french', 'german' 

        word : str
            word

        """
    url = 'https://en.pons.com/translate/%s-%s/%s' % (
        from_language, to_language, word)
    print(url)
    webbrowser.open_new_tab(url)


def dlerae(word):
    """
        Open browser and query the Diccionario de la lengua española

        Parameters
        ----------
        word : str
            word

        """
    if ' ' in word:
        word = re.sub(' ', '-', word)
    url = 'https://dle.rae.es/%s?m=form' % word
    print(url)
    webbrowser.open_new_tab(url)
