""""
Module to query Conceptnet, an open, multilingual knowledge graph.
https://conceptnet.io/
"""

import requests
import webbrowser


def conceptnetQuery(language, word, num=20):
    """
    Query Conceptnet multilingual knowledge graph

    Receive a language and a word and query the Conceptnet API.

    Parameters
    ----------
    language : str
        Language of the word.
        example: 'en', 'pt', 'es', 'fr', 'de', 'ro', 'ca', 'it', 'nl'
    word : str
        word to be queried.
    num : integer
        number of edges in the knowledge graph to be returned.

    Returns
    -------
    str
        String with the concepts in the knowledge graph.


    Examples
    --------
    >>> s = linguae.conceptnetQuery('en','language',5)
    >>> print(s)
    Concepts related to language:
    1) French (en) IsA a language (en)
    2) Spanish (en) IsA language (en)
    3) english (en) RelatedTo language (en)
    4) German (en) IsA a language (en)
    5) Language (en) UsedFor communication (en)
    >>> s = linguae.conceptnetQuery('pt','idioma',5)
    >>> print(s)
    Concepts related to idioma:
    1) idioma (pt) Synonym language (en)
    2) idioma (pt) Synonym dialect (en)
    3) língua (pt) Synonym idioma (pt)
    4) idioma (pt) Synonym natural language (en)
    5) idioma (pt) Synonym língua (pt)
    """
    url = 'http://api.conceptnet.io/c/' + language + \
        '/'+word+'?offset=0&limit='+str(num)

    obj = requests.get(url).json()
    length = len(obj['edges'])

    text = 'Concepts related to ' + word + ':\n'
    for i in range(length):
        try:
            edge = str(i+1) + ") " + obj['edges'][i]['start']['label'] + \
                " (" + obj['edges'][i]['start']['language'] + ") " + \
                obj['edges'][i]['rel']['label'] + " " + \
                obj['edges'][i]['end']['label'] + \
                " (" + obj['edges'][i]['end']['language'] + ')\n '
            text += edge
        except Exception as e:
            print("Oops!", e.__class__, "occurred.")
            continue
    return text


def conceptnetSite(language, word):
    """
    Open browser and query the Conceptnet site.

    Parameters
    ----------
    language : str
        Language of the word.
        examples: 'en', 'es', 'fr', 'it', 'de', 'pt, 'nl'

    word : str
        word

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
    linguae.wiktionaryQuery : Receive a language and a word and gives definitions from Wiktionary.
    linguae.wikipediaQuery : Query Wikipedia. 

    Examples
    --------
    >>> linguae.wikwik('en','language')
    https://en.wikwik.org/language
    >>> linguae.wikwik('es','idioma')
    https://es.wikwik.org/idioma
    """
    url = 'https://conceptnet.io/c/%s/%s' % (language, word)
    print(url)
    webbrowser.open_new_tab(url)
