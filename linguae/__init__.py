"""
Personal package to explore languages and learn about them.
"""
from .translation.translate import translate
from .parsing.parse import parse
from .wordFrequency.wordFrequency import wordFreq
from .wordVector.wordVector import *
from .textGeneration.textGeneration import *
from .concordance.concordance import *
from .verbConjugation.verbConjugation import conjugation
from .wiktionary.wiktionary import wiktionaryQuery
from .conceptnet.conceptnet import conceptnetQuery
from .news.news import googleNews
from .fillMask.fillMask import *
