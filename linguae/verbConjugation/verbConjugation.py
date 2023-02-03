"""
Module for verb conjugation of any Verb using Machine Learning for French, Spanish, Portuguese, Italian and Romanian.
It uses verbecc package under the hood.
https://github.com/bretttolbert/verbecc
"""
import json
import webbrowser
from verbecc import Conjugator


def conjugation(language, verb):
    """
    Conjugate a verb from given language.

    It uses the verbecc package under the hood.

    Parameters
    ----------
    language : str
        Language of the text.
        example: 'pt', 'es', 'fr', 'ro', 'it'

    verb : str
        verb to be conjugated.

    Returns
    -------
    str
        String with the verb conjugation in json format.

    See Also
    --------
    linguae.verbix : Open browser and query the Verbix site.

    Examples
    --------
    >>> linguae.conjugation('pt','aprender')
    >>> linguae.conjugation('es','aprender')
    >>> linguae.conjugation('it','imparare')
    """
    if language not in ['pt', 'es', 'fr', 'it', 'ro']:
        print("Language not supported!")
        return None
    cg = Conjugator(lang=language)
    conj = cg.conjugate(verb)
    return json.dumps(conj, indent=4, ensure_ascii=False)


def verbix(language, verb):
    """
    Open browser and query the Verbix site

    Parameters
    ----------
    language : str
        Language of the text.
        examples: 'portuguese', 'spanish', 'french', 'english', 'italian', 'german'

    verb : str
        verb to be conjugated

    See Also
    --------
    linguae.conjugation : Conjugate a verb from given language.

    Examples
    --------
    >>> linguae.verbix('english','learn')
    https://www.verbix.com/webverbix/english/learn
    >>> linguae.verbix('portuguese','aprender')
    https://www.verbix.com/webverbix/portuguese/aprender
    >>> linguae.verbix('spanish','aprender')
    https://www.verbix.com/webverbix/spanish/aprender
    """
    url = 'https://www.verbix.com/webverbix/%s/%s' % (language, verb)
    print(url)
    webbrowser.open_new_tab(url)
