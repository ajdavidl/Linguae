"""
Module to check the spelling of words.
"""

import re
from spellchecker import SpellChecker


def spellchecker(language, text, distance=1):
    """
    Check the spelling of words

    It uses the pyspellchecker package under the hood.

    Parameters
    ----------
    lang : str
        Language of the model.
        example: 'en', 'es', 'fr', 'pt', 'de', 'ru', 'ar', 'eu', 'lv'.

    text : str
        Text to be checked.

    Examples
    --------
    >>> linguae.spellchecker('en','I am studing languajes!')
    studing :
    corrections: studying
    candidates: {'studding', 'studying'}
    languajes :
    corrections: languages
    candidates: {'languages'}
    >>> linguae.spellchecker('pt','Aprendu linguaz!')
    linguaz :
    corrections: lingua
    candidates: {'lingua', 'linguas'}
    aprendu :
    corrections: aprendi
    candidates: {'aprenda', 'aprendeu', 'aprende', 'aprendi', 'aprendo'}
    """
    if language not in ['en', 'es', 'fr', 'pt', 'de', 'ru', 'ar', 'eu', 'lv']:
        print('Language not supported.')
        return
    spell = SpellChecker(language=language, distance=distance)
    text = re.sub(r'[^\w\s]', '', text)
    wordList = text.split()
    # find those words that may be misspelled
    misspelled = spell.unknown(wordList)
    if len(misspelled) > 0:
        for word in misspelled:
            print(word, ':')
            # Get the one `most likely` answer
            print('corrections:', spell.correction(word))
            # Get a list of `likely` options
            print('candidates:', spell.candidates(word))
    else:
        print('No errors found.')
    return
