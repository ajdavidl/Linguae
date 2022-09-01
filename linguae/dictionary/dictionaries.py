"""
Module with functions that queries dictionaries
"""

import webbrowser
import re


def priberam(query):
    """
        Open browser and query the Portuguese Priberam dictionary

        Parameters
        ----------
        query : str
            word

        """
    if ' ' in query:
        query = re.sub(' ', '-', query)
    url = 'https://dicionario.priberam.org/%s' % query
    print(url)
    webbrowser.open_new_tab(url)


def sinomimos(query):
    """
        Open browser and query the Portuguese Sinonimos dictionary

        Parameters
        ----------
        query : str
            word

        """
    query = re.sub(' ', '-', query)
    query = re.sub('ç', 'c', query)
    query = re.sub('á', 'a', query)
    query = re.sub('ã', 'a', query)
    query = re.sub('â', 'a', query)
    query = re.sub('é', 'e', query)
    query = re.sub('ê', 'e', query)
    query = re.sub('í', 'i', query)
    query = re.sub('ó', 'o', query)
    query = re.sub('õ', 'o', query)
    query = re.sub('ô', 'o', query)
    query = re.sub('ú', 'u', query)
    url = 'https://www.sinonimos.com.br/%s/' % query
    print(url)
    webbrowser.open_new_tab(url)
