"""
Spanish Class language
"""

from .language import Language
from ..textGeneration.textGeneration import loadGPTSpanish, generateText


class Spanish(Language):
    """
    Class Spanish Language to centralize functions
    """

    def __init__(self):
        Language.__init__(self, name='Spanish', code2='es', code3='spa')
        self.GPTSpanish = None

    def generateTextGPTSpanish(self, textSeed, textSize=80):
        """
        Generate texts using the Spanish GPT language model.

        Parameters
        ----------
        textSeed : str
            The text to be used by the language model as a seed.

        textSize : integer
            The number of words to be generated.

        Returns
        -------
        str
            String with the seed text and all text generated.
        """
        if self.GPTSpanish == None:
            self.GPTSpanish = loadGPTSpanish()
        return generateText(self.GPTSpanish, textSeed, textSize)

    def deleteGPTSpanishModel(self):
        """
        Delete the Spanish GPT Language model
        """
        del self.GPTSpanish
        self.GPTSpanish = None
