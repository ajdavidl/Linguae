"""
Module to create lists fo ngrams
"""

from sklearn.feature_extraction.text import CountVectorizer


def nGram(listText, stopwords=None, ngramRange=(1, 1), vocabulary=None):
    """
    Return a list of ngrams

    Parameters
    ----------
    listText : list of str
        List with the texts.
    
    stopwords : list of str
        List of the stop words.
    
    ngramRange : tuple (min_n, max_n), default=(1, 1)
        The number of tokens in the ngram. For example an ngramRange of (1, 1) means only unigrams, (1, 2) means unigrams and bigrams, and (2, 2) means only bigrams.
    
    vocabulary : list of str
        List of the words/ngrams to be added to the frequency list.
    
    Returns
    -------
        list of str
    """
    count_vect = CountVectorizer(
        analyzer='word',
        stop_words=stopwords,
        ngram_range=ngramRange,
        vocabulary=vocabulary
    )
    count_vect.fit_transform(listText)
    return [token  for token, idx in count_vect.vocabulary_.items()]
