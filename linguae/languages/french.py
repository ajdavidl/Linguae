"""
French Class language
"""

from .language import Language
from ..sentiment.sentiment import *


class French(Language):
    """
    Class French Language to centralize functions

    Attributes
    ----------
        Sentiment_ : dict
            python dictionary with the French Lexicon
    """

    def __init__(self):
        Language.__init__(self, name='French', code2='fr', code3='fre')
        self.Sentiment_ = None

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
