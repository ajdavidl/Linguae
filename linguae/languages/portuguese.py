"""
Portuguese Class language
"""

from .language import Language
from ..dictionary.dictionaries import sinomimos, priberam


class Portuguese(Language):
    """
    Class Portuguese Language to centralize functions
    """

    def __init__(self):
        Language.__init__(self, name='Portuguese', code2='pt', code3='por')

    def priberam(self, word):
        """
        Open browser and query the Portuguese Priberam dictionary

        Parameters
        ----------
        query : str
            word

        """
        return priberam(word)

    def sinonimos(self, word):
        """
        Open browser and query the Portuguese Sinonimos dictionary

        Parameters
        ----------
        query : str
            word

        """
        return sinomimos(word)
