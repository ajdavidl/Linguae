"""
Module to translate sentences between languages.
"""
from textblob import TextBlob

def translate(from_language, to_language, text):
    """
        Translate text from one language to another

        It uses the textblob package under the hood.

        Parameters
        ----------
        from_language : str
            Language of the text.
            example: 'en', 'pt', 'es', 'fr', 'de', 'ro', 'ca', 'it', 'nl'

        to_language : str
            Language that the text will be translated
            example: 'en', 'pt', 'es', 'fr', 'de', 'ro', 'ca', 'it', 'nl'

        Returns
        -------
        str
            String with the text translated in the language asked.
        """
    blob = TextBlob(text).translate(to=to_language, from_lang=from_language)
    return str(blob)