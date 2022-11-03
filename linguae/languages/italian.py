"""
Italian Class language
"""

from .language import Language
from ..dictionary.dictionaries import wordReference
from ..sentiment.sentiment import *


class Italian(Language):
    """
    Class Italian Language to centralize functions

    Attributes
    ----------
        Sentiment_ : dict
            python dictionary with the Italian Lexicon
    """

    def __init__(self):
        Language.__init__(self, name='Italian', code2='it', code3='ita')
        self.Sentiment_ = None

    def wordReference(self, word):
        """
        Open browser and query the WordReference dictionary

        Parameters
        ----------
        word : str
            word

        """
        return wordReference(self.code2, word)

    def sentiment(self, word):
        """
        Get the sentiment associated to a word.

        Parameters
        ----------
        word : string
            String with the word to be queried.

        Returns
        -------
        Print the polarity of a word.
        """
        if self.Sentiment_ == None:
            self.Sentiment_ = loadSentiment(self.code2)
        return polarity(self.Sentiment_, word)
