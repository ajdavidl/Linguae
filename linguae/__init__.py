"""
Personal package to explore languages and learn about them.
"""
from .translation.translate import translate
from .parsing.parse import parse, loadSpacyModel, parseSpacy
from .wordFrequency.wordFrequency import wordFreq
from .wordVector.wordVector import *
from .textGeneration.textGeneration import *
from .concordance.concordance import concordance
from .verbConjugation.verbConjugation import conjugation
from .dictionary.wiktionary import wiktionaryQuery
from .dictionary.dictionaries import *
from .conceptnet.conceptnet import conceptnetQuery
from .news.news import googleNews
from .fillMask.fillMask import *
from .textSamples.textSamples import textSamples
from .tatoeba.tatoeba import *
from .wikipediaQuery.wikipediaQuery import wikipediaQuery
from .languages.language import Language
from .languages.portuguese import Portuguese
from .languages.english import English
from .languages.spanish import Spanish
from .syllables.syllables import *
from .image.image import *
from .audioSamples.audioSamples import forvo
