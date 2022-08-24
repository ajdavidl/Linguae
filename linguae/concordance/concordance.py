"""
Module to create concordance views for a given word.
Is uses NLTK under the hood.
"""
import nltk
import pandas as np
try:
    import importlib.resources as pkg_resources
except ImportError:
    import importlib_resources as pkg_resources

from .. import data

MAX_NR_SENTENCES = 100000

def loadTatoeba():
    """
        Load tatoeba sentences

        It reads the csv file from Tatoeba and returns a Pandas dataframe with the sentences.

        Parameters
        ----------
        No parameters

        Returns
        -------
        Pandas data frame with 3 columns: "index", "language", "sentence"
            
        """
    tatoebaFile = pkg_resources.open_text(data, "sentences.csv")
    return np.read_csv(tatoebaFile,sep="\t",header=None, names=["index", "language", "sentence"])

def loadLanguageTatoeba(language):
    """
        Load tatoeba sentences

        It reads the csv file from Tatoeba and returns a Pandas dataframe with the sentences.

        Parameters
        ----------
        language : str
            Language desired.
            example: 'eng', 'por', 'spa', 'fra', 'deu', 'ron', 'ita'

        Returns
        -------
        list
            List of sentences from the desired language
            
        """
    tatoebaFile = pkg_resources.open_text(data, "sentences.csv")
    tatoeba = np.read_csv(tatoebaFile,sep="\t",header=None, names=["index", "language", "sentence"])
    return tatoeba[tatoeba.language == language]['sentence'].values.tolist()

def concordance(listSentences, word):
    """
        Return the concordances of a word in a list of sentences

        It uses the NLTK package under the hood.

        Parameters
        ----------
        listSentences : list
            List of sentences

        word : str
            word

        Returns
        -------
        str
            String with the text of the word concordances.
        """
    if len(listSentences) > MAX_NR_SENTENCES:
        listSentences = listSentences[:MAX_NR_SENTENCES]
    tokens = nltk.word_tokenize("\n".join(listSentences))
    text1 = nltk.Text(tokens)
    results = text1.concordance_list(word, width = 100, lines = 20)
    textOutput = ""
    for i in range(len(results)):
        textOutput = textOutput + results[i][4] + " " + results[i][1] + " " + results[i][5]  + "\n"
    return(textOutput)
