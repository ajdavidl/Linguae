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