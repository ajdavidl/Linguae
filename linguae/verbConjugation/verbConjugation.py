"""
Module for verb conjugation of any Verb using Machine Learning for French, Spanish, Portuguese, Italian and Romanian.
It uses verbecc package under the hood.
https://github.com/bretttolbert/verbecc
"""
import json
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
        """
    if language not in ['pt', 'es', 'fr', 'it', 'ro']:
        print("Language not supported!")
        return None
    cg = Conjugator(lang=language)
    conj = cg.conjugate(verb)
    return  json.dumps(conj, indent=4, ensure_ascii = False)
    

    