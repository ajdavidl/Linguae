"""
German Class language
"""

from .language import Language
from ..sentiment.sentiment import *


class German(Language):
    """
    Class German Language to centralize functions
    """

    def __init__(self):
        Language.__init__(self, name='German', code2='de', code3='deu')
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
