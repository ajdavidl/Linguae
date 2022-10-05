"""
Spanish Class language
"""

from .language import Language
from ..dictionary.dictionaries import dlerae, wordReference
from ..fillMask.fillMask import fillMaskBert, loadBertSpanish
from ..textGeneration.textGeneration import loadGPTSpanish, generateText
from ..sentiment.sentiment import *


class Spanish(Language):
    """
    Class Spanish Language to centralize functions
    """

    def __init__(self):
        Language.__init__(self, name='Spanish', code2='es', code3='spa')
        self.BertSpanish = None
        self.GPTSpanish = None
        self.Sentiment_ = None

    def dlerae(self, word):
        """
        Open browser and query the Diccionario de la lengua española

        Parameters
        ----------
        word : str
            word
        """
        return dlerae(word)

    def wordReference(self, word):
        """
        Open browser and query the WordReference dictionary

        Parameters
        ----------
        word : str
            word

        """
        return wordReference(self.code2, word)

    def generateTextGPTSpanish(self, textSeed, textSize=80):
        """
        Generate texts using the Spanish GPT language model.

        Parameters
        ----------
        textSeed : str
            The text to be used by the language model as a seed.

        textSize : integer
            The number of words to be generated.

        Returns
        -------
        str
            String with the seed text and all text generated.
        """
        if self.GPTSpanish == None:
            self.GPTSpanish = loadGPTSpanish()
        return generateText(self.GPTSpanish, textSeed, textSize)

    def deleteGPTSpanishModel(self):
        """
        Delete the Spanish GPT Language model
        """
        del self.GPTSpanish
        self.GPTSpanish = None

    def fillMaskBert(self, maskedSentence):
        """
        Fill the mask tag on the masked Sentence

        Parameters
        ----------
        maskedSentence : str
            The masked sentence to be used by the language model.

        Returns
        -------
        str
            String with the words that fill the mask and their score.
        """
        if self.BertSpanish == None:
            self.BertSpanish = loadBertSpanish()
        return fillMaskBert(self.BertSpanish, maskedSentence)

    def deleteBertSpanish(self):
        """
        Delete the Bert Spanish Language model
        """
        del self.BertSpanish
        self.BertSpanish = None

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
