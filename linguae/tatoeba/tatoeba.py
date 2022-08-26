"""
Module to load tatoeba data
"""

import pandas as pd
try:
    import importlib.resources as pkg_resources
except ImportError:
    import importlib_resources as pkg_resources

from .. import data


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
    return pd.read_csv(tatoebaFile, sep="\t", header=None, names=["index", "language", "sentence"])


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
    tatoeba = pd.read_csv(tatoebaFile, sep="\t", header=None, names=[
                          "index", "language", "sentence"])
    return tatoeba[tatoeba.language == language]['sentence'].values.tolist()
