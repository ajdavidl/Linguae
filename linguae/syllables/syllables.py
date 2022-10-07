"""
Module to split words in syllables
"""
from hyphen import Hyphenator


def loadHyphenator(language):
    """
        Load the Hyphenator Model for one language

        Parameters
        ----------
        language : str
            Language of the text.
            example: 'en', 'pt', 'es', 'fr', 'de', 'ro', 'it'

        Returns
        -------
        class hyphen.hyphenator.Hyphenator
            Hyphenator model for the language selected.
        """
    if language == 'pt':
        return Hyphenator('pt_BR')
    elif language == 'en':
        return Hyphenator('en_US')
    elif language == 'es':
        return Hyphenator('es_ES')
    elif language == 'it':
        return Hyphenator('it_IT')
    elif language == 'fr':
        return Hyphenator('fr_FR')
    elif language == 'de':
        return Hyphenator('de_DE')
    elif language == 'ro':
        return Hyphenator('ro')
    else:
        print("Language not supported!")
        return None


def syllables(model, word):
    """
        Split the given word in syllables

        Parameters
        ----------
        model : class hyphen.hyphenator.Hyphenator
            Hyphenator model.

        word : str
            word to be split

        Returns
        -------
        str
            String with word's syllables
        """
    listSyllables = model.syllables(word)
    if len(listSyllables) == 0:
        return word
    else:
        return '-'.join(listSyllables)
