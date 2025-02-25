"""
Module to create lists fo ngrams
"""

from sklearn.feature_extraction.text import CountVectorizer


def nGram(listText, stopwords=None, ngramRange=(1, 1), vocabulary=None):
    """
    Return a list of ngrams
    """
    count_vect = CountVectorizer(
        analyzer='word',
        stop_words=stopwords,
        ngram_range=ngramRange,
        vocabulary=vocabulary
    )
    count_vect.fit_transform(listText)
    return [token  for token, idx in count_vect.vocabulary_.items()]
