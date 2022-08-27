"""
Class Language
"""

from ..translation.translate import translate
from ..parsing.parse import loadSpacyModel, parseSpacy
# from ..wordFrequency.wordFrequency import wordFreq
# from ..wordVector.wordVector import *
# from ..textGeneration.textGeneration import *
# from ..concordance.concordance import concordance
# from ..verbConjugation.verbConjugation import conjugation
# from ..wiktionary.wiktionary import wiktionaryQuery
# from ..conceptnet.conceptnet import conceptnetQuery
# from ..news.news import googleNews
# from ..fillMask.fillMask import *
# from ..textSamples.textSamples import textSamples
# from ..tatoeba.tatoeba import *
# from ..wikipediaQuery.wikipediaQuery import wikipediaQuery


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
        self.spaCyModel = loadSpacyModel(self.code2)

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
        return parseSpacy(self.spaCyModel, text)
