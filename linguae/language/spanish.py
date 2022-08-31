"""
Spanish Class language
"""

from .language import Language


class Spanish(Language):
    """
    Class Spanish Language to centralize functions
    """

    def __init__(self):
        Language.__init__(self, name='Spanish', code2='es', code3='spa')
