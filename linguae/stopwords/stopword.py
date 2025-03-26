"""
Module that returns stopwords lists.
"""

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def stopWords(language):
    """
    Return the NLTK stopwords list

    Parameters:
    -----------
    language : str
        The language of the stop words list. 
        Example: 'english', 'portuguese', 'spanish', 'german'
    """
    return set(stopwords.words(language.lower()))

def filterStopWords(listTexts, listStopwords):
    """
    Remove the stop words of a list of strings

    Parameters:
    -----------
    listTexts : list of str
        A list with the texts to be filtered.
    
    listStopwords : list of str
        The stop words list.
    """
    if type(listTexts) == str:
        listTexts = [listTexts]
    listTextsOut = []
    for txt in listTexts:
        words = word_tokenize(txt)
        wordsFiltered = [w for w in words if w not in listStopwords]
        listTextsOut.append(' '.join(wordsFiltered))
    return listTextsOut