"""
Module to explore word similarity using pre-trained word embeddings.
"""
from gensim.models import KeyedVectors
try:
    import importlib.resources as pkg_resources
except ImportError:
    import importlib_resources as pkg_resources

from .. import data


def loadWordVectors(language):
    """
    Load word vectors from the desired language.

    It uses the MUSE pre-trained word embeddings and gensim KeyedVectors model.

    Parameters
    ----------
    language : str
        Language of the word.
        example: 'en', 'pt', 'es', 'fr', 'de', 'ro', 'it'

    Returns
    -------
    gensim KeyedVectors model
        A gensim model with the word vectors loaded.

    See Also
    --------
    linguae.similarWords : Get similar words with word embeddings.
    linguae.loadSentenceTransformerModel : Load a SentenceTransformer model.
    linguae.encodeSentence : Computes sentence embeddings using sentence_transformers package.
    linguae.similarSentences : Gives the most similar sentences from a query sentence using the sentence transformer model.

    Examples
    --------
    >>> engVectors = linguae.loadWordVectors('en')
    >>> porVectors = linguae.loadWordVectors('pt')

    """
    vectorFile = 'wiki.multi.%s.vec' % language
    template = pkg_resources.open_text(data, vectorFile)

    return KeyedVectors.load_word2vec_format(template, binary=False)


def similarWords(fromLanguageVectors, word, toLanguagesVectors=[]):
    """
    Get similar words with word embeddings.

    It receives the loaded word vectors model from one language; 
    Then load a vector from a given word; 
    and then gives the most similar words in each model given.

    It uses the gensim KeyedVectors model.

    Parameters
    ----------
    fromLanguageVectors : gensim KeyedVectors model
        The model load with the function loadWordVectors.
        Alternatively, the model given by the funtion gensim.models.KeyedVectors.load_word2vec_format.

    word : str
        word to be queried.

    toLanguagesVectors : list of gensim KeyedVectors models
        MUSE models from other languages loaded by the function loadWordVectors.

    Returns
    -------
    str
        String with the similar words.

    See Also
    --------
    linguae.loadWordVectors : Load word vectors from the desired language.
    linguae.loadSentenceTransformerModel : Load a SentenceTransformer model.
    linguae.encodeSentence : Computes sentence embeddings using sentence_transformers package.
    linguae.similarSentences : Gives the most similar sentences from a query sentence using the sentence transformer model.

    Examples
    --------
    >>> engVectors = linguae.loadWordVectors('en')
    >>> porVectors = linguae.loadWordVectors('pt')
    >>> spaVectors = linguae.loadWordVectors('es')
    >>> print(linguae.similarWords(engVectors, 'language', [porVectors, spaVectors]))
    >>> print(linguae.similarWords(porVectors, 'idioma', [engVectors, spaVectors]))
    """
    vector = fromLanguageVectors.get_vector(word)
    tuples = fromLanguageVectors.similar_by_vector(vector)
    textOutput = "%s:\n" % word
    for t in tuples:
        textOutput = textOutput + t[0] + " - " + str(t[1]) + "\n"
    for vecs in toLanguagesVectors:
        textOutput = textOutput + "\n"
        tuples = vecs.similar_by_vector(vector)
        for t in tuples:
            textOutput = textOutput + t[0] + " - " + str(t[1]) + "\n"
    return textOutput
