""""
Module to query Conceptnet, an open, multilingual knowledge graph.
https://conceptnet.io/
"""

import requests

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