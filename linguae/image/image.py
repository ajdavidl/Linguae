"""
Module to search images on internet
"""

import webbrowser
import re


def googleImages(query):
    """
        Open browser and query Google Images

        Parameters
        ----------
        query : str

        """
    if ' ' in query:
        query = re.sub(' ', '+', query)
    url = 'https://www.google.com/search?tbm=isch&q=%s' % query
    print(url)
    webbrowser.open_new_tab(url)


def duckduckGoImages(query):
    """
        Open browser and query Duckduckgo images

        Parameters
        ----------
        query : str

        """
    if ' ' in query:
        query = re.sub(' ', '+', query)
    url = 'https://duckduckgo.com/?q=%s&t=ffab&iar=images&iax=images&ia=images' % query
    print(url)
    webbrowser.open_new_tab(url)
