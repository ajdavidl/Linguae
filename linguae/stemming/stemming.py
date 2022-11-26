"""
Module to do stemming task
"""
from nltk.stem import RSLPStemmer, PorterStemmer


def stem(language, token):
    """
    Stem a given token.

    This function receives the language name and the token and performs the stemming task.
    It uses the nltk.stem module.

    Parameters
    ----------
    language : str
        Language of the stemming model. Only Portuguese and English is supported.
        example: 'en', 'pt'

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
    else:
        print('Language not supported.')
    if type(token) == str:
        return stem.stem(token)
    else:
        raise('Type error. The token parameter must be a string.')
