"""
Module to do stemming task
"""
from nltk.stem import RSLPStemmer, PorterStemmer, SnowballStemmer


def stem(language, token):
    """
    Stem a given token.

    This function receives the language name and the token and performs the stemming task.
    It uses the nltk.stem module.

    Parameters
    ----------
    language : str
        Language of the stemming model. 
        example: 'en', 'pt', 'es', 'it', 'fr', 'de', 'ro', 'nl'

    token : str
        The word to be used in the task.

    Returns
    -------
    str
        String with the root of the token.

    Examples
    --------
    >>> linguae.stem('en','languages')
    'languag'
    >>> linguae.stem('pt','idiomas')
    'idiom'
    """
    if language == 'en':
        stem = PorterStemmer()
    elif language == 'pt':
        stem = RSLPStemmer()
    elif language == 'es':
        stem = SnowballStemmer('spanish')
    elif language == 'it':
        stem = SnowballStemmer('italian')
    elif language == 'fr':
        stem = SnowballStemmer('french')
    elif language == 'de':
        stem = SnowballStemmer('german')
    elif language == 'ro':
        stem = SnowballStemmer('romanian')
    elif language == 'nl':
        stem = SnowballStemmer('dutch')
    else:
        print('Language not supported.')
    if type(token) == str:
        return stem.stem(token)
    else:
        raise('Type error. The token parameter must be a string.')
