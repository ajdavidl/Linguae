"""
Module to return word lists of languages.
"""
import re
try:
    import importlib.resources as pkg_resources
except ImportError:
    import importlib_resources as pkg_resources

from ..data import wordLists


def wordList(language):
    """
    Return the word list of a language.

    Parameters
    ----------
    language : str
        Language of the chatbot.
        example: 'eng', 'por', 'spa', 'fre', 'deu', 'ita', 'nld'

    Examples
    --------
    >>> engList = linguae.wordList('eng')
    >>> print(len(engList))
    >>> spaList = linguae.wordList('spa')
    >>> print(len(spaList))
    """
    if language in ['por', 'eng', 'ita', 'fre', 'spa', 'deu', 'nld']:
        nameFile = '%s.txt' % language
    else:
        print("Language not supported!")
        return None
    file = pkg_resources.open_text(wordLists, nameFile)
    words = file.readlines()

    for i in range(len(words)):
        words[i] = re.sub('\n', '', words[i])

    return words
