"""
English Class language
"""

from .language import Language
from ..dictionary.dictionaries import dictionary_com, thesaurus, wordReference
from ..fillMask.fillMask import fillMaskBert, loadBertEnglish
from ..textGeneration.textGeneration import loadGPTEnglish, generateText
from ..sentiment.sentiment import *


class English(Language):
    """
    Class English Language to centralize functions
    """

    def __init__(self):
        Language.__init__(self, name='English', code2='en', code3='eng')
        self.BertEnglish = None
        self.GPTEnglish = None
        self.Sentiment_ = None

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

    def wordReference(self, word):
        """
        Open browser and query the WordReference dictionary

        Parameters
        ----------
        word : str
            word

        """
        return wordReference(self.code2, word)

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

    def generateTextGPTEnglish(self, textSeed, textSize=80):
        """
        Generate texts using the English GPT language model.

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
        if self.GPTEnglish == None:
            self.GPTEnglish = loadGPTEnglish()
        return generateText(self.GPTEnglish, textSeed, textSize)

    def deleteGPTEnglishModel(self):
        """
        Delete the English GPT Language model
        """
        del self.GPTEnglish
        self.GPTEnglish = None

    def wordSentiment(self, word):
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

    def sentenceSentiment(self, sentence):
        """
        Get the sentiment associated to a sentence.

        It loads TextBlob sentiment analysis model and prints the polarity and subjectivity of a sentence.

        Parameters
        ----------
        sentence : str
            String with a sentence to be analysed.

        Returns
        -------
        Prints the polarity and subjectivity of a word.
        """
        sentenceSentiment(sentence)
