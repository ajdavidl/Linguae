"""
Italian Class language
"""

from .language import Language
from ..dictionary.dictionaries import wordReference


class Italian(Language):
    """
    Class Italian Language to centralize functions
    """

    def __init__(self):
        Language.__init__(self, name='Italian', code2='it', code3='ita')

    def wordReference(self, word):
        """
        Open browser and query the WordReference dictionary

        Parameters
        ----------
        word : str
            word

        """
        return wordReference(self.code2, word)
