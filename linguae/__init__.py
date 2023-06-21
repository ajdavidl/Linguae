"""
Python package to explore natural languages. 
"""
from .translation.translate import *
from .parsing.parse import parse, loadSpacyModel, parseSpacy
from .wordFrequency.wordFrequency import wordFreq
from .wordVector.wordVector import *
from .textGeneration.textGeneration import *
from .concordance.concordance import concordance
from .verbConjugation.verbConjugation import *
from .dictionary.wiktionary import wiktionaryQuery
from .dictionary.dictionaries import *
from .conceptnet.conceptnet import *
from .news.news import googleNews, emmNewsBrief
from .fillMask.fillMask import *
from .textSamples.textSamples import textSamples
from .tatoeba.tatoeba import *
from .wikipediaQuery.wikipediaQuery import wikipediaQuery
from .languages.language import Language
from .languages.portuguese import Portuguese
from .languages.english import English
from .languages.spanish import Spanish
from .languages.italian import Italian
from .languages.french import French
from .languages.german import German
from .syllables.syllables import *
from .image.image import *
from .audioSamples.audioSamples import forvo
from .sentiment.sentiment import *
from .sentenceVector.sentenceVector import *
from .ner.ner import *
from .stemming.stemming import stem
from .chatbot.chatbot import chatbot, dialoGPT
from .numspell.numspell import num2words
from .text2speech.text2speech import tts
from .spellChecker.spellChecker import spellchecker
from .report.report import *

__version__ = '0.5.0-alpha'
