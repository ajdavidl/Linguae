from gensim.models import KeyedVectors
try:
    import importlib.resources as pkg_resources
except ImportError:
    import importlib_resources as pkg_resources

from .. import data

def loadVectors(language):
    """
        Load word vectors from the desired language

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
        """
    vectorFile = 'wiki.multi.%s.vec' % language
    template = pkg_resources.open_text(data, vectorFile)
    
    return KeyedVectors.load_word2vec_format(template, binary=False)

def similar(fromLanguageVectors, word, toLanguagesVectors = []):
    """
        It receives the loaded word vectors model from one language; 
        Then load a vector from a given word; 
        and then gives the most similar words in each model given.

        It uses the gensim KeyedVectors model.

        Parameters
        ----------
        fromLanguageVectors : gensim KeyedVectors model
            The model load with the function loadVectors.
            Alternatively, the model given by the funtion gensim.models.KeyedVectors.load_word2vec_format.

        word : str
            word to be queried.

        toLanguagesVectors : list of gensim KeyedVectors models
            MUSE models from other languages loaded by the function loadVectors.

        Returns
        -------
        str
            String with the similar words.
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
