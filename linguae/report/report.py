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

    print()
    print(f"Report of the word: {word}")
    print()
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
    if language == "en":
        print("Translation to Portuguese")
        print(obj.translateTo("pt", word))
        print()
        print("Translation to Spanish")
        print(obj.translateTo("es", word))
    elif language == "pt":
        print("Translation to English")
        print(obj.translateTo("en", word))
        print()
        print("Translation to Spanish")
        print(obj.translateTo("es", word))
    else:
        print("Translation to English")
        print(obj.translateTo("en", word))
        print()
        print("Translation to Portuguese")
        print(obj.translateTo("pt", word))
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
    print(f"Now listen to the sound of word {word} in {language} language!")
    obj.tts(word)


def sentenceReport(language, sentence):

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

    print()
    print(f"Report of the sentence: {sentence}")
    print()
    if language == "en":
        print("Translation to Spanish")
        print(obj.translateTo("es", sentence))
        print()
        print("Translation to Portuguese")
        print(obj.translateTo("pt", sentence))
        print()
        print("Translation to French")
        print(obj.translateTo("fr", sentence))
        print()
        print("Translation to German")
        print(obj.translateTo("de", sentence))
    elif language == "pt":
        print("Translation to English")
        print(obj.translateTo("en", sentence))
        print()
        print("Translation to Spanish")
        print(obj.translateTo("es", sentence))
        print()
        print("Translation to French")
        print(obj.translateTo("fr", sentence))
        print()
        print("Translation to Italian")
        print(obj.translateTo("it", sentence))
        print()
        print("Translation to German")
        print(obj.translateTo("de", sentence))
    elif language == "es":
        print("Translation to English")
        print(obj.translateTo("en", sentence))
        print()
        print("Translation to Portuguese")
        print(obj.translateTo("pt", sentence))
    else:
        print("Translation to English")
        print(obj.translateTo("en", sentence))
        print()
        print("Translation to Portuguese")
        print(obj.translateTo("pt", sentence))
        print()
        print("Translation to Spanish")
        print(obj.translateTo("es", sentence))
    print()
    print("Parsing the sentence:")
    print(obj.parse(sentence))
    print()
    obj.loadTatoebaList()
    obj.trimTatoebaList(50000)
    print("Similar Sentences on Tatoeba")
    print(obj.similarSentences(sentence, 20))
    print()
    print("Entities in the sentence:")
    print(obj.nerSpacy(sentence))
    print()
    print("Entity link")
    print(obj.dbpediaEntityLink(sentence))
    print()
    print(f"Now listen to the sound of sentence in {language} language!")
    obj.tts(sentence)
