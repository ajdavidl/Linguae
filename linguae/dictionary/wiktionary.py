"""
Module to query Wiktionary
"""

from wiktionaryparser import WiktionaryParser


def wiktionaryQuery(language, word):
    """
    Receive a language and a word and gives definitions from Wiktionary.

    Use WiktionaryParser package under the hood.

    Parameters
    ----------
    language : str
        Language of the text.
        example: 'en', 'pt', 'es', 'fr', 'de', 'it'

    word : str
        word to be queried.

    Returns
    -------
    str
        String with the definitions.

    See Also
    --------
    linguae.priberam : Open browser and query the Portuguese Priberam dictionary.
    linguae.sinomimos : Open browser and query the Portuguese Sinonimos dictionary.
    linguae.linguee : Open browser and query the multilingual Linguee dictionary.
    linguae.glosbe : Open browser and query the multilingual Glosbe dictionary.
    linguae.dictionary_com : Open browser and query the English dictionary.com.
    linguae.thesaurus : Open browser and query the English thesaurus dictionary.
    linguae.pons : Open browser and query the multilingual Pons dictionary.
    linguae.dlerae : Open browser and query the Diccionario de la lengua española.
    linguae.wordReference : Open browser and query the WordReference dictionary.

    Examples
    --------
    >>> linguae.wiktionaryQuery('en', 'language')
    >>> linguae.wiktionaryQuery('pt', 'idioma')
    """
    if language == 'pt':
        language = 'portuguese'
    elif language == 'en':
        language = 'english'
    elif language == 'es':
        language = 'spanish'
    elif language == 'it':
        language = 'italian'
    elif language == 'fr':
        language = 'french'
    elif language == 'de':
        language = 'german'
    else:
        language = 'english'
    parser = WiktionaryParser()
    parser.set_default_language(language)
    try:
        data = parser.fetch(word)
    except Exception as e:
        return "Sorry! Error in wiktionary package!!"
    if len(data) > 0:
        if 'definitions' in data[0].keys():
            if len(data[0]['definitions']) > 0:
                definitions = data[0]['definitions'][0]['text']
                text = "Definitions: "
                for i in range(len(definitions)):
                    text += data[0]['definitions'][0]['text'][i]+'\n'
                return text
            else:
                return "No text inside definitions data from wiktionary."
        else:
            return "No definitions found in wiktionary data."
    else:
        return "Empty data from wiktionary."
