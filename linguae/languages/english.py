"""
English Class language
"""

from .language import Language
from ..dictionary.dictionaries import dictionary_com, thesaurus


class English(Language):
    """
    Class English Language to centralize functions
    """

    def __init__(self):
        Language.__init__(self, name='English', code2='en', code3='emg')

    def dictionary_com(self, word):
        """
        Open browser and query the English dictionary.com

        Parameters
        ----------
        word : str
            word

        """
        return dictionary_com(word)

    def thesaurus(self, word):
        """
        Open browser and query the English Thesaurus dictionary

        Parameters
        ----------
        word : str
            word

        """
        return thesaurus(word)
