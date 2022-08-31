"""
Portuguese Class language
"""

from .language import Language


class Portuguese(Language):
    """
    Class Portuguese Language to centralize functions
    """

    def __init__(self):
        Language.__init__(self, name='Portuguese', code2='pt', code3='por')
