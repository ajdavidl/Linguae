"""
Portuguese Class language
"""

from .language import Language
from ..dictionary.dictionaries import sinomimos, priberam
from ..fillMask.fillMask import fillMaskBert, loadBertPortuguese
from ..textGeneration.textGeneration import loadGPTPortuguese, generateText
from ..sentiment.sentiment import *
from ..stemming.stemming import stem


class Portuguese(Language):
    """
    Class Portuguese Language to centralize functions

    Attributes
    ----------
        BertPortuguese : a Pipeline object from the transformers package with the Bloom model loaded
        GPTPortuguese : a Pipeline object from the transformers package with the Bloom model loaded
        Sentiment_ : dict
            python dictionary with the Portuguese Lexicon
    """

    def __init__(self):
        Language.__init__(self, name='Portuguese', code2='pt', code3='por')
        self.BertPortuguese = None
        self.GPTPortuguese = None
        self.Sentiment_ = None

    def priberam(self, word):
        """
        Open browser and query the Portuguese Priberam dictionary

        Parameters
        ----------
        word : str
            word

        """
        return priberam(word)

    def sinonimos(self, word):
        """
        Open browser and query the Portuguese Sinonimos dictionary

        Parameters
        ----------
        word : str
            word

        """
        return sinomimos(word)

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
        if self.BertPortuguese == None:
            self.BertPortuguese = loadBertPortuguese()
        return fillMaskBert(self.BertPortuguese, maskedSentence)

    def deleteBertPortuguese(self):
        """
        Delete the Bert Portuguese Language model
        """
        del self.BertPortuguese
        self.BertPortuguese = None

    def generateTextGPTPortuguese(self, textSeed, textSize=80):
        """
        Generate texts using the Portuguese GPT language model.

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
        if self.GPTPortuguese == None:
            self.GPTPortuguese = loadGPTPortuguese()
        return generateText(self.GPTPortuguese, textSeed, textSize)

    def deleteGPTPortugueseModel(self):
        """
        Delete the Portuguese GPT Language model
        """
        del self.GPTPortuguese
        self.GPTPortuguese = None

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

    def stem(self, token):
        """
        Stem a given token.

        Parameters
        ----------
        token : str
            The word to be used in the task.

        Returns
        -------
        str
            String with the root of the token.
        """
        return stem(self.code2, token)
