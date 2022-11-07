"""
Module to search images on internet
"""

import webbrowser
import re


def googleImages(query):
    """
    Open browser and query Google Images.

    Parameters
    ----------
    query : str

    See Also
    --------
    linguae.duckduckGoImages : Open browser and query Duckduckgo images.
    linguae.forvo : Open browser and query audio samples from Forvo site.

    Examples
    --------
    >>> linguae.googleImages("ball")
    https://www.google.com/search?tbm=isch&q=ball
    >>> linguae.googleImages("bola")
    https://www.google.com/search?tbm=isch&q=bola
    """
    if ' ' in query:
        query = re.sub(' ', '+', query)
    url = 'https://www.google.com/search?tbm=isch&q=%s' % query
    print(url)
    webbrowser.open_new_tab(url)


def duckduckGoImages(query):
    """
    Open browser and query Duckduckgo images.

    Parameters
    ----------
    query : str

    See Also
    --------
    linguae.googleImages : Open browser and query Google images.
    linguae.forvo : Open browser and query audio samples from Forvo site.

    Examples
    --------
    >>> linguae.duckduckGoImages("ball")
    https://duckduckgo.com/?q=ball&t=ffab&iar=images&iax=images&ia=images
    >>> linguae.duckduckGoImages("bola")
    https://duckduckgo.com/?q=bola&t=ffab&iar=images&iax=images&ia=images
    """
    if ' ' in query:
        query = re.sub(' ', '+', query)
    url = 'https://duckduckgo.com/?q=%s&t=ffab&iar=images&iax=images&ia=images' % query
    print(url)
    webbrowser.open_new_tab(url)
