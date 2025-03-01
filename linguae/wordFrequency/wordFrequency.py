"""
Module to give the frequency of a word.
"""
from wordfreq import word_frequency
from sklearn.feature_extraction.text import CountVectorizer

def wordFreq(language, word):
    """
    Get the frequency of word in a given language.

    It uses the wordfreq package under the hood.

    Parameters
    ----------
    language : str
        Language of the word.
        example: 'en', 'pt', 'es', 'fr', 'de', 'ro', 'it'

    word : str
        Word to be queried.

    Returns
    -------
    str
        String with with the number of frequency.

    Examples
    --------
    >>> linguae.wordFreq('en', 'the')
    '0.0537'
    >>> linguae.wordFreq('en', 'language')
    '0.000126'
    >>> linguae.wordFreq('pt', 'de')
    '0.0479'
    >>> linguae.wordFreq('pt', 'idioma')
    '1.95e-05'
    """
    freq = word_frequency(word=word, lang=language)
    return str(freq)



def frequency(listText, stopwords=None, ngramRange=(1, 1), vocabulary=None):
    """
    Calculate the frequency os tokens (unigrams, bigrams ...) of a list of strings.

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
    List of tuples

    Examples
    --------
    >>> listEng = linguae.loadLanguageTatoeba('eng')
    >>> listEngFreq = linguae.frequency(listEng)
    >>> listEngFreq[:10]
    """
    count_vect = CountVectorizer(
        analyzer='word',
        stop_words=stopwords,
        ngram_range=ngramRange,
        vocabulary=vocabulary
    )
    count_vect.fit(listText)
    bag_of_words = count_vect.transform(listText)
    sum_words = bag_of_words.sum(axis=0)
    word_freq = [(word, sum_words[0, idx])
                 for word, idx in count_vect.vocabulary_.items()]
    word_freq = sorted(word_freq, key=lambda x: x[1], reverse=True)
    return word_freq