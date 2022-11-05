"""
Module to load tatoeba data and query tatoeba site
"""

import pandas as pd
import webbrowser
import re
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

        It reads the csv file from Tatoeba and returns a list with the sentences.

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


def tatoebaSite(text, from_language, to_language=None):
    """
        Open browser and query tatoeba site
        Parameters
        ----------
        text : str
            Text to be queried

        from_language : str
            Language of the text.
            example: 'eng', 'por', 'spa', 'fre', 'deu' 

        to_language : str (optional)
            Language that the text will be translated
            example: 'eng', 'por', 'spa', 'fre', 'deu' 

        """
    if ' ' in text:
        text = re.sub(' ', '%20', text)
    url = 'https://tatoeba.org/en/sentences/search?from=%s&query=%s' % (
        from_language, text)
    if to_language != None:
        url = '%s&to=%s' % (url, to_language)
    print(url)
    webbrowser.open_new_tab(url)
