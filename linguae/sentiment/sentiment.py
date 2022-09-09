"""
Module to get the sentiment/polarity of a word.
"""

import pandas as pd
try:
    import importlib.resources as pkg_resources
except ImportError:
    import importlib_resources as pkg_resources

from .. import data


def loadSentiment(language):
    """
        Load portuguese sentiments

        It reads the xml file with the portuguese sentiments of a word.

        Parameters
        ----------
        language : str
            Language to be loaded.
            examples: 'en', 'fr', 'pt', 'it'

        Returns
        -------
        Python Dictionary
        Dictionary with the word on keys and polarities on values

        None if language not supported
        """
    if language == 'pt':
        nameFile = '%s-sentiment.xml' % language
    else:
        print("Language not supported!")
        return None
    file = pkg_resources.open_text(data, nameFile)

    df = pd.read_xml(file, xpath='.//word')
    df.columns = ['word', 'polarity']
    df = df.set_index('word')
    dictSent = df.polarity.to_dict()
    return dictSent


def polarity(dictionary, word):
    """
        Get the sentiment associated to a word.

        It receives a dictionary with sentiments and it prints the polarity of a word

        Parameters
        ----------
        dictionary : dict
            Dictionary with the sentiments. The dictionary is loaded in function "loadSentiment".

        word : string
            String with the word to be queried.

        Returns
        -------
        Prints the polarity of a word.
        """
    if word in dictionary.keys():
        print(dictionary[word])
    else:
        print('word not in dictionary')
    return
