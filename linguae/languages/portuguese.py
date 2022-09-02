"""
Portuguese Class language
"""

from .language import Language
from ..dictionary.dictionaries import sinomimos, priberam
from ..fillMask.fillMask import fillMaskBert, loadBertPortuguese


class Portuguese(Language):
    """
    Class Portuguese Language to centralize functions
    """

    def __init__(self):
        Language.__init__(self, name='Portuguese', code2='pt', code3='por')
        self.BertPortuguese = None

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
