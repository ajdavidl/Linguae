"""
Module to give the word frequency of a word.
"""
from wordfreq import word_frequency

def wordFreq(language, word):
    """
        Get the frequency of `word` in the language with code `language`

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
        """
    freq = word_frequency(word=word, lang=language)
    return str(freq)