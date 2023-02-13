"""
Module to give the word frequency of a word.
"""
from wordfreq import word_frequency


def wordFreq(language, word):
    """
    Get the frequency of word in the language with code language.

    It uses the wordfreq package under the hood.

    Parameters
    ----------
    language : str
        Language of the word.
        example: 'en', 'pt', 'es', 'fr', 'de', 'ro', 'it'

    word : str
        word to be queried.

    Returns
    -------
    str
        String with with the number of frequency.

    Examples
    --------
    >>> linguae.wordFreq('en', 'the')
    '0.0537'
    >>> linguae.wordFreq('en', 'language')
    '0.000126'
    >>> linguae.wordFreq('pt', 'de')
    '0.0479'
    >>> linguae.wordFreq('pt', 'idioma')
    '1.95e-05'
    """
    freq = word_frequency(word=word, lang=language)
    return str(freq)
