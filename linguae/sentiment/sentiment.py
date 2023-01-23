"""
Module to get the sentiment/polarity of a word.
"""

import pandas as pd
from textblob import TextBlob
try:
    import importlib.resources as pkg_resources
except ImportError:
    import importlib_resources as pkg_resources

from .. import data


def loadSentiment(language):
    """
    Load sentiments lexicon of different languages.

    It reads the xml file with the sentiments of a word.

    Parameters
    ----------
    language : str
        Language to be loaded.
        examples: 'en', 'fr', 'pt', 'it', 'es', 'de'

    Returns
    -------
    Python Dictionary
    Dictionary with the word on keys and polarities on values

    None if language not supported.
	
    See also
    --------
    linguae.polarity : Get the sentiment associated to a word.
    linguae.sentenceSentiment : Get the sentiment associated to a sentence.

    Examples
    --------
    >>> engLex = linguae.loadSentiment('en')
    >>> porLex = linguae.loadSentiment('pt')
    """
    if language in ['pt', 'en', 'it', 'fr', 'es', 'de']:
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

    It receives a dictionary with sentiments and it prints the polarity of a word.

    Parameters
    ----------
    dictionary : dict
        Dictionary with the sentiments. The dictionary is loaded in function "loadSentiment".

    word : string
        String with the word to be queried.

    Returns
    -------
    Prints the polarity of a word.

    See also
    --------
    linguae.loadSentiment : Load sentiments lexicon of different languages.
    linguae.sentenceSentiment : Get the sentiment associated to a sentence.

    Examples
    --------
    >>> engLex = linguae.loadSentiment('en')
    >>> linguae.polarity(engLex, 'good')
    0.7
    >>> linguae.polarity(engLex, 'bad')
    -0.7
    >>> porLex = linguae.loadSentiment('pt')
    >>> linguae.polarity(porLex, 'bom')
    1
    >>> linguae.polarity(porLex, 'ruim')
    -1
    """
    if word in dictionary.keys():
        print(dictionary[word])
    else:
        print('word not in dictionary')
    return


def sentenceSentiment(sentence):
    """
    Get the sentiment associated to a sentence.

    Only English language.

    It loads TextBlob sentiment analysis model and prints the polarity and subjectivity of a sentence.

    Parameters
    ----------
    sentence : str
        String with a sentence to be analysed.

    Returns
    -------
    Prints the polarity and subjectivity of a word.

    See also
    --------
    linguae.loadSentiment : Load sentiments lexicon of different languages.
    linguae.polarity : Get the sentiment associated to a word.

    Examples
    --------
    >>> linguae.sentenceSentiment('Learning languages is good.')
    Sentiment(polarity=0.7, subjectivity=0.6000000000000001)
    """
    text = TextBlob(sentence)
    print(text.sentiment)
    return
