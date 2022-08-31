"""
English Class language
"""

from .language import Language


class English(Language):
    """
    Class English Language to centralize functions
    """

    def __init__(self):
        Language.__init__(self, name='English', code2='en', code3='emg')
