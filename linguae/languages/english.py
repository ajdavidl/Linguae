"""
English Class language
"""

from .language import Language
from ..dictionary.dictionaries import dictionary_com, thesaurus
from ..fillMask.fillMask import fillMaskBert, loadBertEnglish


class English(Language):
    """
    Class English Language to centralize functions
    """

    def __init__(self):
        Language.__init__(self, name='English', code2='en', code3='emg')
        self.BertEnglish = None

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
        if self.BertEnglish == None:
            self.BertEnglish = loadBertEnglish()
        return fillMaskBert(self.BertEnglish, maskedSentence)

    def deleteBertEnglish(self):
        """
        Delete the Bert English Language model
        """
        del self.BertEnglish
        self.BertEnglish = None
