"""
Module to generate a command line report
"""

from ..languages.language import Language
from ..languages.portuguese import Portuguese
from ..languages.english import English
from ..languages.spanish import Spanish
from ..languages.italian import Italian
from ..languages.french import French
from ..languages.german import German


def wordReport(language, word):

    if language == "en":
        obj = English()
    elif language == "pt":
        obj = Portuguese()
    elif language == "es":
        obj = Spanish()
    elif language == "it":
        obj = Italian()
    elif language == "fr":
        obj = French()
    elif language == "de":
        obj = German()
    else:
        print("Language not supported!")
        return

    print(f"Definition of the word {word} in wiktionary:")
    print(obj.wiktionary(word))
    print()
    print(f"Definition of the word {word} in English Wiktionary:")
    print(obj.wiktionaryEnglish(word))
    print()
    print("Syllables of the word {word}:")
    print(obj.syllables(word))
    print()
    print(f"Word Frequency in {obj.name} language:")
    print(obj.wordFreq(word))
    print()
    print(f"Similar Words in {obj.name} language:")
    print(obj.similarWords(word))
    print()
    obj.loadTatoebaList()
    obj.trimTatoebaList(100000)
    print(f"Concordance of the word {word}:")
    print(obj.concordance(word))
    print()
    print(f"Concepnet graph of the word {word}:")
    print(obj.conceptnet(word, 25))
    print()
    print(f"Text samples of the word {word} in {language} language:")
    print(obj.textSamples(word, 25))
    print()
    print(f"Now listen to the sound of word {word} in {language} Portuguese!")
    obj.tts(word)
