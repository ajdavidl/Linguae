"""
Class Language
"""

from ..translation.translate import translate
from ..parsing.parse import loadSpacyModel, parseSpacy
from ..wordFrequency.wordFrequency import wordFreq
from ..wordVector.wordVector import *
from ..textGeneration.textGeneration import *
from ..concordance.concordance import concordance
from ..verbConjugation.verbConjugation import conjugation
from ..wiktionary.wiktionary import wiktionaryQuery
from ..conceptnet.conceptnet import conceptnetQuery
from ..news.news import googleNews
from ..fillMask.fillMask import *
from ..textSamples.textSamples import textSamples
from ..tatoeba.tatoeba import loadLanguageTatoeba
from ..wikipediaQuery.wikipediaQuery import wikipediaQuery
from ..syllables.syllables import *
from ..image.image import *
from ..audioSamples.audioSamples import forvo


class Language:
    """
    Class Language to centralize functions
    """

    def __init__(self, name, code2, code3):
        """
        Constructor of the class

        Parameters
        ----------
        name : str
            Name of the Language
            example: 'English', 'Portuguese', 'Spanish', 'French'

        code2 : str
            code of the language with 2 letters
            example: 'en', 'pt', 'es', 'fr', 'de', 'ro', 'ca', 'it', 'nl'

        code3 : str
            code of the language with 3 letters
            example: 'eng', 'por', 'esp', 'fra', 'deu'
        """
        self.name = name
        self.code2 = code2
        self.code3 = code3
        self.spaCyModel = None
        self.wordVectorModel = None
        self.Bloom = None
        self.mGPT = None
        self.tatoeba = None
        self.BertMultilingual = None
        self.XLMRoberta = None
        self.hyphenatorModel = None

    def translateTo(self, to_language, text):
        """
        Translate text to the informed language

        Parameters
        ----------
        to_language : str
            Language that the text will be translated
            example: 'en', 'pt', 'es', 'fr', 'de', 'ro', 'ca', 'it', 'nl'

        Returns
        -------
        str
            String with the text translated in the language asked.
        """
        return translate(self.code2, to_language, text)

    def translateFrom(self, from_language, text):
        """
        Translate text from the informed language

        Parameters
        ----------
        from_language : str
            Language that the text will be translated
            example: 'en', 'pt', 'es', 'fr', 'de', 'ro', 'ca', 'it', 'nl'

        Returns
        -------
        str
            String with the text translated in the language of the class.
        """
        return translate(from_language, self.code2, text)

    def parse(self, text):
        """
        Parse text using spaCy model

        Parameters
        ----------
        sentence : str
            Text to be parsed

        Returns
        -------
        str
            String with with the token, pos, tags and dependencies in a table format.
        """
        if self.spaCyModel == None:
            self.spaCyModel = loadSpacyModel(self.code2)
        return parseSpacy(self.spaCyModel, text)

    def wordFreq(self, word):
        """
        Get the frequency of `word`

        Parameters
        ----------

        word : str
            word to be queried.

        Returns
        -------
        str
            String with with the number of frequency.
        """
        return wordFreq(self.code2, word)

    def similarWords(self, word, otherLanguages=[]):
        """
        Give the most similar words in each word vector model.

        Parameters
        ----------
        word : str
            word to be queried.

        otherLanguages : list of gensim KeyedVectors models in other languages
            MUSE models from other languages loaded by the function loadVectors.

        Returns
        -------
        str
            String with the similar words and their scores.
        """
        if self.wordVectorModel == None:
            self.wordVectorModel = loadVectors(self.code2)
        return similar(self.wordVectorModel, word, otherLanguages)

    def deleteWordVectorsModel(self):
        """
        Delete the word vectors model
        """
        del self.wordVectorModel
        self.wordVectorModel = None

    def generateTextBloom(self, textSeed, textSize=80):
        """
        Generate texts using the Bloom language model.

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
        if self.Bloom == None:
            self.Bloom = loadBloom()
        return generateText(self.Bloom, textSeed, textSize)

    def deleteBloomModel(self):
        """
        Delete the Bloom Language model
        """
        del self.Bloom
        self.Bloom = None

    def generateTextMGPT(self, textSeed, textSize=80):
        """
        Generate texts using the mGPT language model.

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
        if self.mGPT == None:
            self.mGPT = loadmGPT()
        return generateText(self.mGPT, textSeed, textSize)

    def deleteMGPTModel(self):
        """
        Delete the mGPT Language model
        """
        del self.mGPT
        self.mGPT = None

    def concordance(self, word):
        """
        Return the concordances of a word

        Parameters
        ----------
        word : str
            word

        Returns
        -------
        str
            String with the text of the word concordances.
        """
        if self.tatoeba == None:
            self.tatoeba = loadLanguageTatoeba(self.code3)
        return concordance(self.tatoeba, word)

    def deleteTatoebaList(self):
        """
        Delete the tatoeba word list
        """
        del self.tatoeba
        self.tatoeba = None

    def conjugation(self, verb):
        """
        Conjugate a verb

        Parameters
        ----------
        verb : str
            verb to be conjugated.

        Returns
        -------
        str
            String with the verb conjugation in json format.
        """
        return conjugation(self.code2, verb)

    def wiktionary(self, word):
        """
        Give definitions from Wiktionary.

        Parameters
        ----------
        word : str
            word to be queried.

        Returns
        -------
        str
            String with the definitions.
        """
        return wiktionaryQuery(self.code2, word)

    def wiktionaryEnglish(self, word):
        """
        Give definitions from English Wiktionary.

        English Wiktionary has the most words.

        Parameters
        ----------
        word : str
            word to be queried.

        Returns
        -------
        str
            String with the definitions.
        """
        return wiktionaryQuery('en', word)

    def conceptnet(self, word, num=20):
        """
        Query Conceptnet multilingual knowledge graph

        Parameters
        ----------
        word : str
            word to be queried.

        num : integer
            number of edges in the knowledge graph to be returned.

        Returns
        -------
        str
            String with the concepts in the knowledge graph.
        """
        return conceptnetQuery(self.code2, word, num)

    def googleNews(self, num=None):
        """
        Return the news' title from Google news using RSS feeds.

        Parameters
        ----------
        num : integer
            Maximum number of news to be returned.

        Returns
        -------
        str
            String with the titles of the news.
        """
        return googleNews(self.code2, num)

    def fillMaskmBert(self, maskedSentence):
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
        if self.BertMultilingual == None:
            self.BertMultilingual = loadBertMultilingual()
        return fillMaskmBert(self.BertMultilingual, maskedSentence)

    def deleteBertMultilingual(self):
        """
        Delete the Bert Multilingual Language model
        """
        del self.BertMultilingual
        self.BertMultilingual = None

    def fillMaskXLMRoberta(self, maskedSentence):
        """
        Fill the mask tag on the masked Sentence

        Parameters
        ----------
        maskedSentence : str
            The masked sentence to be used by the language model.

        Returns
        -------
        str
            String with the words that fill the mask and their scores.
        """
        if self.XLMRoberta == None:
            self.XLMRoberta = loadXLMRoberta()
        return fillMaskXLMRoberta(self.XLMRoberta, maskedSentence)

    def deleteXLMRoberta(self):
        """
        Delete the XLM Roberta Language model
        """
        del self.XLMRoberta
        self.XLMRoberta = None

    def textSamples(self, expression, num=20):
        """
        Return the text samples of an expression

        Parameters
        ----------
        expression : str
            words

        num : integer
            number of examples to show.

        Returns
        -------
        str
            String with the examples of sentences with the given expression.
        """
        if self.tatoeba == None:
            self.tatoeba = loadLanguageTatoeba(self.code3)
        return textSamples(self.tatoeba, expression, num=20)

    def wikipedia(self, query):
        """
        Query Wikipedia

        Parameters
        ----------
        query : str
            words to be queried.

        Returns
        -------
        str
            String with the wikipedia page summary.
        """
        return wikipediaQuery(self.code2, query)

    def syllables(self, word):
        """
        Split the given word in syllables

        Parameters
        ----------
        word : str
            word to be split

        Returns
        -------
        str
            String with word's syllables
        """
        if self.hyphenatorModel == None:
            self.hyphenatorModel = loadHyphenator(self.code2)
        return syllables(self.hyphenatorModel, word)

    def image(self, query, websearch='google'):
        """
        Open browser and query Images from Internet

        Parameters
        ----------
        query : str

        websearch : str
            search engine to be used: google or duckduckgo
            deafault : google

        """
        if websearch == 'google':
            return googleImages(query)
        elif websearch == 'duckduckgo' or websearch == 'ddg':
            return duckduckGoImages(query)
        else:
            print('websearch not understood, using google')
            return googleImages(query)

    def audio(self, word):
        """
        Open browser and query Forvo audios

        Parameters
        ----------
        word : str
            word to be queried.

        """
        return forvo(self.code2, word)
