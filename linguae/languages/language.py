"""
Class Language
"""
from random import sample
from ..translation.translate import *
from ..parsing.parse import loadSpacyModel, parseSpacy
from ..wordFrequency.wordFrequency import wordFreq
from ..wordVector.wordVector import *
from ..textGeneration.textGeneration import loadBloom, loadmGPT, generateText
from ..concordance.concordance import concordance
from ..verbConjugation.verbConjugation import *
from ..dictionary.wiktionary import wiktionaryQuery
from ..dictionary.dictionaries import linguee, glosbe, pons
from ..conceptnet.conceptnet import conceptnetQuery
from ..news.news import googleNews, emmNewsBrief
from ..fillMask.fillMask import loadBertMultilingual, loadXLMRoberta, fillMaskBert, fillMaskXLMRoberta
from ..textSamples.textSamples import textSamples
from ..tatoeba.tatoeba import loadLanguageTatoeba, tatoebaSite
from ..wikipediaQuery.wikipediaQuery import wikipediaQuery
from ..syllables.syllables import *
from ..image.image import *
from ..audioSamples.audioSamples import forvo
from ..sentenceVector.sentenceVector import *
from ..ner.ner import *
from ..chatbot.chatbot import chatbot


class Language:
    """
    Class Language to centralize functions.

    Attributes
    ----------
        name : str
            Name of the language.
        code2 : str
            2 letters abbreviation of the language.
        code3 : str
            3 letters abbreviation of the language.
        spacyModel : class spacy.lang
            SpaCy model for the language selected.
        wordVectorModel : gensim KeyedVectors model
            A gensim model with the word vectors loaded.
        Bloom : a Pipeline object from the transformers package with the Bloom model loaded.
        mGPT : a Pipeline object from the transformers package with the Bloom model loaded.
        tatoeba : list
            list of sentences from tatoeba site.
        BertMultilingual : a Pipeline object from the transformers package with the Bloom model loaded.
        XLMRoberta : a Pipeline object from the transformers package with the Bloom model loaded.
        hyphenatorModel : class hyphen.hyphenator.Hyphenator
            Hyphenator model.
        sentenceVectorModel : 'sentence_transformers.SentenceTransformer.SentenceTransformer' model.
            Sentence transformer model
        tatoebaTensorsEmbeddings : tensor encoded by sentence_transformers.SentenceTransformer.SentenceTransformer model.
    """

    def __init__(self, name, code2, code3):
        """
        Constructor of the class.

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
        self.sentenceVectorModel = None
        self.tatoebaTensorsEmbeddings = None

    def __repr__(self):
        return "{self.__class__.__name__}({self.name}, {self.code2}, {self.code3})".format(self=self)

    def __str__(self):
        return "Object of class {self.__class__.__name__} with parameters: {self.name}, {self.code2}, {self.code3}".format(self=self)

    def translateTo(self, to_language, text):
        """
        Translate text to the informed language.

        Parameters
        ----------
        to_language : str
            Language that the text will be translated
            example: 'en', 'pt', 'es', 'fr', 'de', 'ro', 'ca', 'it', 'nl'

        text : str
            Text to be translated

        Returns
        -------
        str
            String with the text translated in the language asked.
        """
        return translate(self.code2, to_language, text)

    def translateFrom(self, from_language, text):
        """
        Translate text from the informed language.

        Parameters
        ----------
        from_language : str
            Language that the text will be translated
            example: 'en', 'pt', 'es', 'fr', 'de', 'ro', 'ca', 'it', 'nl'

        text : str
            Text to be translated

        Returns
        -------
        str
            String with the text translated in the language of the class.
        """
        return translate(from_language, self.code2, text)

    def googleTranslateTo(self, to_language, text):
        """
        Open browser and query Google translate site.

        Parameters
        ----------
        to_language : str
            Language that the text will be translated
            example: 'en', 'pt', 'es', 'fr', 'de', 'ro', 'ca', 'it', 'nl'

        text : str
            Text to be translated
        """
        return googleTranslate(self.code2, to_language, text)

    def googleTranslateFrom(self, from_language, text):
        """
        Open browser and query Google translate site.

        Parameters
        ----------
        from_language : str
            Language that the text will be translated
            example: 'en', 'pt', 'es', 'fr', 'de', 'ro', 'ca', 'it', 'nl'

        text : str
            Text to be translated
        """
        return googleTranslate(from_language, self.code2, text)

    def parse(self, text):
        """
        Parse text using spaCy model.

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
        Get the frequency of `word`.

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
            MUSE models from other languages loaded by the function loadWordVectors.

        Returns
        -------
        str
            String with the similar words and their scores.
        """
        if self.wordVectorModel == None:
            self.wordVectorModel = loadWordVectors(self.code2)
        return similarWords(self.wordVectorModel, word, otherLanguages)

    def loadWordVectorsModel(self):
        """
        Load the MUSE word vectors model.
        """
        self.wordVectorModel = loadWordVectors(self.code2)

    def deleteWordVectorsModel(self):
        """
        Delete the word vectors model.
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
        Delete the Bloom Language model.
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
        Delete the mGPT Language model.
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

    def loadTatoebaList(self):
        """
        Load the tatoeba word list.
        """
        self.tatoeba = loadLanguageTatoeba(self.code3)

    def trimTatoebaList(self, NrSentences):
        """
            Trim the tatoeba list sentences

            Parameters
            ----------
            NrSentences : int
                the new list's number of sentences
        """
        if (self.tatoeba != None) & (len(self.tatoeba) > NrSentences):
            index = [i for i in range(len(self.tatoeba))]
            index = sample(index, NrSentences)
            self.tatoeba = [self.tatoeba[i] for i in index]
            if not (self.tatoebaTensorsEmbeddings is None):
                del self.tatoebaTensorsEmbeddings
                self.tatoebaTensorsEmbeddings = None

    def deleteTatoebaList(self):
        """
        Delete the tatoeba word list.
        """
        del self.tatoeba
        self.tatoeba = None

    def conjugation(self, verb):
        """
        Conjugate a verb.

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

    def verbix(self, verb):
        """
        Open browser and query the Verbix site.

        Parameters
        ----------
        verb : str
            verb to be conjugated

        """
        return verbix(self.name.lower(), verb)

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
        Query Conceptnet multilingual knowledge graph.

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

    def emmNewsBrief(self, num=None):
        """
        Return the news' title from emm.newsbrief.eu using RSS feeds.

        Parameters
        ----------
        num : integer
            Maximum number of news to be returned.

        Returns
        -------
        str
            String with the titles of the news.
        """
        return emmNewsBrief(self.code2, num)

    def fillMaskmBert(self, maskedSentence):
        """
        Fill the mask tag on the masked Sentence.

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
        return fillMaskBert(self.BertMultilingual, maskedSentence)

    def deleteBertMultilingual(self):
        """
        Delete the Bert Multilingual Language model.
        """
        del self.BertMultilingual
        self.BertMultilingual = None

    def fillMaskXLMRoberta(self, maskedSentence):
        """
        Fill the mask tag on the masked Sentence.

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
        Delete the XLM Roberta Language model.
        """
        del self.XLMRoberta
        self.XLMRoberta = None

    def textSamples(self, expression, num=20):
        """
        Return the text samples of an expression.

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
        return textSamples(self.tatoeba, expression, num=num)

    def wikipedia(self, query):
        """
        Query Wikipedia.

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
        Split the given word in syllables.

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
        Open browser and query Images from Internet.

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
        Open browser and query Forvo audios.

        Parameters
        ----------
        word : str
            word to be queried.

        """
        return forvo(self.code2, word)

    def glosbeTo(self, to_language, word):
        """
        Open browser and query word to the informed language using Glosbe dictionary.

        Parameters
        ----------
        to_language : str
            Language that the text will be translated
            example: 'en', 'pt', 'es', 'fr', 'de', 'ro', 'ca', 'it', 'nl'

        word : str
            word to be queried.

        """
        return glosbe(self.code2, to_language, word)

    def glosbeFrom(self, from_language, word):
        """
        Open browser and query word from the informed language using Glosbe dictionary.

        Parameters
        ----------
        from_language : str
            Language from the word that will be translated
            example: 'en', 'pt', 'es', 'fr', 'de', 'ro', 'ca', 'it', 'nl'

        word : str
            word to be queried.

        """
        return glosbe(from_language, self.code2, word)

    def lingueeTo(self, to_language, word):
        """
        Open browser and query word to the informed language using Linguee dictionary.

        Parameters
        ----------
        to_language : str
            Language that the text will be translated
            examples: 'english', 'portuguese', 'spanish', 'french'

        word : str
            word to be queried.

        """
        return linguee(self.name.lower(), to_language, word)

    def lingueeFrom(self, from_language, word):
        """
        Open browser and query word from the informed language using Linguee dictionary.

        Parameters
        ----------
        from_language : str
            Language from the word that will be translated
            examples: 'english', 'portuguese', 'spanish', 'french'

        word : str
            word to be queried.

        """
        return linguee(from_language, self.name.lower(), word)

    def ponsTo(self, to_language, word):
        """
        Open browser and query word to the informed language using Pons dictionary.

        Parameters
        ----------
        to_language : str
            Language that the text will be translated
            examples: 'english', 'portuguese', 'spanish', 'french'

        word : str
            word to be queried.

        """
        return pons(self.name.lower(), to_language, word)

    def ponsFrom(self, from_language, word):
        """
        Open browser and query word from the informed language using Pons dictionary.

        Parameters
        ----------
        from_language : str
            Language from the word that will be translated
            examples: 'english', 'portuguese', 'spanish', 'french'

        word : str
            word to be queried.

        """
        return pons(from_language, self.name.lower(), word)

    def tatoebaSite(self, text, languageTo=None):
        """
        Open browser and query tatoeba site.

        Parameters
        ----------
        text : str
            Text to be queried

        languageTo : str (optional)
            Language that the text will be translated
            example: 'eng', 'por', 'spa', 'fre', 'deu' 

        """
        return tatoebaSite(text, self.code3, to_language=languageTo)

    def similarSentences(self, querySentence, nrSentencesReturned=10):
        """
        Gives the most similar sentences from a query sentence using the sentence transformer model.

        Parameters
        ----------
        querySentence : str
            sentence to be queried

        nrSentencesReturned : int
            number of sentences to be returned

        Returns 
        -------
        str
            String with the most similar sentences.
    """
        if self.sentenceVectorModel == None:
            self.sentenceVectorModel = loadSentenceTransformerModel()
        if self.tatoeba == None:
            self.tatoeba = loadLanguageTatoeba(self.code3)
        if self.tatoebaTensorsEmbeddings is None:
            self.tatoebaTensorsEmbeddings = encodeSentence(
                self.sentenceVectorModel, self.tatoeba)
        return similarSentences(self.sentenceVectorModel, querySentence, self.tatoeba, None, self.tatoebaTensorsEmbeddings, nrSentencesReturned)

    def deleteSentenceVectorModel(self):
        """
        Delete the Sentence Vector Model.
        """
        del self.sentenceVectorModel
        self.sentenceVectorModel = None

    def encodeSentences(self):
        """
        Computes sentence embeddings using of the tatoeba list of sentences.
        """
        if self.sentenceVectorModel == None:
            self.sentenceVectorModel = loadSentenceTransformerModel()
        if self.tatoeba == None:
            self.tatoeba = loadLanguageTatoeba(self.code3)
        self.tatoebaTensorsEmbeddings = encodeSentence(
            self.sentenceVectorModel, self.tatoeba)

    def nerSpacy(self, sentence):
        """
        Get entities from text using spaCy model.

        Parameters
        ----------
        model : spacy.lang
            SpaCy Language model. Load from linguae.parsing.parse.loadSpacyModel function

        sentence : str
            Text to be parsed

        Returns
        -------
        str
            String with the entities.
        """
        if self.spaCyModel == None:
            self.spaCyModel = loadSpacyModel(self.code2)
        return nerSpacy(self.spaCyModel, sentence)

    def dbpediaEntityLink(self, sentence):
        """
        Link entities from sentence to dbpedia knowledge base.

        Parameters
        ----------

        sentence : str
            Sentence to be queried.

        Returns
        -------
        str
            string with the entities extracted from the sentence.

        """
        return dbpediaEntityLink(self.code2, sentence)

    def chatbot(self, train=True, feedback=False, readOnly=False):
        """
        Open a command line chatbot.

        It uses the chatterbot package under the hood.

        Press ctrl+c or ctrl+d to exit the function.

        Parameters
        ----------
        train : bool (default=True)
            If True, the chatbot trains with the available data.
            If False, the chatbot doesn't train.
        feedback : bool (defaul=False)
            If True, the chatbot ask you if the answer is coherent.
            If False, it doesn't get the feedback.
        readOnly : bool (default=False)
            If True, it doesn't save the user's answers.
            If False, it saves the user's answer in a database for future use.
        """
        return(chatbot(self.code2, train=True, feedback=False, readOnly=False))
