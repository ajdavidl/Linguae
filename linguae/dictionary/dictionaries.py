"""
Module with functions that query dictionaries
"""

import webbrowser
import re


def priberam(word):
    """
    Open browser and query the Portuguese Priberam dictionary.

    Parameters
    ----------
    word : str
        word

    See Also
    --------
    linguae.sinomimos : Open browser and query the Portuguese Sinonimos dictionary.
    linguae.linguee : Open browser and query the multilingual Linguee dictionary.
    linguae.glosbe : Open browser and query the multilingual Glosbe dictionary.
    linguae.dictionary_com : Open browser and query the English dictionary.com.
    linguae.thesaurus : Open browser and query the English thesaurus dictionary.
    linguae.pons : Open browser and query the multilingual Pons dictionary.
    linguae.dlerae : Open browser and query the Diccionario de la lengua española.
    linguae.wordReference : Open browser and query the WordReference dictionary.
    linguae.wiktionaryQuery : Receive a language and a word and gives definitions from Wiktionary.

    Examples
    --------
    >>> linguae.priberam('idioma')
    https://dicionario.priberam.org/idioma
    """
    if ' ' in word:
        word = re.sub(' ', '-', word)
    url = 'https://dicionario.priberam.org/%s' % word
    print(url)
    webbrowser.open_new_tab(url)


def sinomimos(word):
    """
    Open browser and query the Portuguese Sinonimos dictionary.

    Parameters
    ----------
    word : str
        word

    See Also
    --------
    linguae.priberam : Open browser and query the Portuguese Priberam dictionary.
    linguae.linguee : Open browser and query the multilingual Linguee dictionary.
    linguae.glosbe : Open browser and query the multilingual Glosbe dictionary.
    linguae.dictionary_com : Open browser and query the English dictionary.com.
    linguae.thesaurus : Open browser and query the English thesaurus dictionary.
    linguae.pons : Open browser and query the multilingual Pons dictionary.
    linguae.dlerae : Open browser and query the Diccionario de la lengua española.
    linguae.wordReference : Open browser and query the WordReference dictionary.
    linguae.wiktionaryQuery : Receive a language and a word and gives definitions from Wiktionary.

    Examples
    --------
    >>> linguae.sinomimos('idioma')
    https://www.sinonimos.com.br/idioma/
    """
    word = re.sub(' ', '-', word)
    word = re.sub('ç', 'c', word)
    word = re.sub('á', 'a', word)
    word = re.sub('ã', 'a', word)
    word = re.sub('â', 'a', word)
    word = re.sub('é', 'e', word)
    word = re.sub('ê', 'e', word)
    word = re.sub('í', 'i', word)
    word = re.sub('ó', 'o', word)
    word = re.sub('õ', 'o', word)
    word = re.sub('ô', 'o', word)
    word = re.sub('ú', 'u', word)
    url = 'https://www.sinonimos.com.br/%s/' % word
    print(url)
    webbrowser.open_new_tab(url)


def linguee(from_language, to_language, word):
    """
    Open browser and query the multilingual Linguee dictionary.

    Parameters
    ----------
    from_language : str
        Language of the text.
        examples: 'english', 'portuguese', 'spanish', 'french'

    to_language : str
        Language that the text will be translated
        examples: 'english', 'portuguese', 'spanish', 'french'

    word : str
        word

    See Also
    --------
    linguae.priberam : Open browser and query the Portuguese Priberam dictionary.
    linguae.sinomimos : Open browser and query the Portuguese Sinonimos dictionary.
    linguae.glosbe : Open browser and query the multilingual Glosbe dictionary.
    linguae.dictionary_com : Open browser and query the English dictionary.com.
    linguae.thesaurus : Open browser and query the English thesaurus dictionary.
    linguae.pons : Open browser and query the multilingual Pons dictionary.
    linguae.dlerae : Open browser and query the Diccionario de la lengua española.
    linguae.wordReference : Open browser and query the WordReference dictionary.
    linguae.wiktionaryQuery : Receive a language and a word and gives definitions from Wiktionary.

    Examples
    --------
    >>> linguae.linguee('portuguese','english','idioma')
    https://www.linguee.com/portuguese-english/search?source=portuguese&query=idioma
    >>> linguae.linguee('english','spanish','language')
    https://www.linguee.com/english-spanish/search?source=english&query=language
    """
    url = 'https://www.linguee.com/%s-%s/search?source=%s&query=%s' % (
        from_language, to_language, from_language, word)
    print(url)
    webbrowser.open_new_tab(url)


def glosbe(from_language, to_language, word):
    """
    Open browser and query the multilingual Glosbe dictionary.

    Parameters
    ----------
    from_language : str
        Language of the text.
        examples: 'en', 'pt', 'es', 'fr'

    to_language : str
        Language that the text will be translated
        examples: 'en', 'pt', 'es', 'fr'

    word : str
        word

    See Also
    --------
    linguae.priberam : Open browser and query the Portuguese Priberam dictionary.
    linguae.sinomimos : Open browser and query the Portuguese Sinonimos dictionary.
    linguae.linguee : Open browser and query the multilingual Linguee dictionary.
    linguae.dictionary_com : Open browser and query the English dictionary.com.
    linguae.thesaurus : Open browser and query the English thesaurus dictionary.
    linguae.pons : Open browser and query the multilingual Pons dictionary.
    linguae.dlerae : Open browser and query the Diccionario de la lengua española.
    linguae.wordReference : Open browser and query the WordReference dictionary.
    linguae.wiktionaryQuery : Receive a language and a word and gives definitions from Wiktionary.

    Examples
    --------
    >>> linguae.glosbe('pt','en','idioma')
    https://glosbe.com/pt/en/idioma
    >>> linguae.glosbe('en','es','language')
    https://glosbe.com/en/es/language
    """
    url = 'https://glosbe.com/%s/%s/%s' % (from_language, to_language, word)
    print(url)
    webbrowser.open_new_tab(url)


def dictionary_com(word):
    """
    Open browser and query the English dictionary.com.

    Parameters
    ----------
    word : str
        word

    See Also
    --------
    linguae.priberam : Open browser and query the Portuguese Priberam dictionary.
    linguae.sinomimos : Open browser and query the Portuguese Sinonimos dictionary.
    linguae.linguee : Open browser and query the multilingual Linguee dictionary.
    linguae.glosbe : Open browser and query the multilingual Glosbe dictionary.
    linguae.thesaurus : Open browser and query the English thesaurus dictionary.
    linguae.pons : Open browser and query the multilingual Pons dictionary.
    linguae.dlerae : Open browser and query the Diccionario de la lengua española.
    linguae.wordReference : Open browser and query the WordReference dictionary.
    linguae.wiktionaryQuery : Receive a language and a word and gives definitions from Wiktionary.

    Examples
    --------
    >>> linguae.dictionary_com('language')
    https://www.dictionary.com/browse/language
    """
    url = 'https://www.dictionary.com/browse/%s' % word
    print(url)
    webbrowser.open_new_tab(url)


def thesaurus(word):
    """
    Open browser and query the English thesaurus dictionary.

    Parameters
    ----------
    word : str
        word

    See Also
    --------
    linguae.priberam : Open browser and query the Portuguese Priberam dictionary.
    linguae.sinomimos : Open browser and query the Portuguese Sinonimos dictionary.
    linguae.linguee : Open browser and query the multilingual Linguee dictionary.
    linguae.glosbe : Open browser and query the multilingual Glosbe dictionary.
    linguae.dictionary_com : Open browser and query the English dictionary.com.
    linguae.pons : Open browser and query the multilingual Pons dictionary.
    linguae.dlerae : Open browser and query the Diccionario de la lengua española.
    linguae.wordReference : Open browser and query the WordReference dictionary.
    linguae.wiktionaryQuery : Receive a language and a word and gives definitions from Wiktionary.

    Examples
    --------
    >>> linguae.thesaurus('language')
    https://www.thesaurus.com/browse/language
    """
    url = 'https://www.thesaurus.com/browse/%s' % word
    print(url)
    webbrowser.open_new_tab(url)


def pons(from_language, to_language, word):
    """
    Open browser and query the multilingual Pons dictionary.

    Parameters
    ----------
    from_language : str
        Language of the text.
        examples: 'english', 'portuguese', 'spanish', 'french', 'german'  

    to_language : str
        Language that the text will be translated
        examples: 'english', 'portuguese', 'spanish', 'french', 'german' 

    word : str
        word

    See Also
    --------
    linguae.priberam : Open browser and query the Portuguese Priberam dictionary.
    linguae.sinomimos : Open browser and query the Portuguese Sinonimos dictionary.
    linguae.linguee : Open browser and query the multilingual Linguee dictionary.
    linguae.glosbe : Open browser and query the multilingual Glosbe dictionary.
    linguae.dictionary_com : Open browser and query the English dictionary.com.
    linguae.thesaurus : Open browser and query the English thesaurus dictionary.
    linguae.dlerae : Open browser and query the Diccionario de la lengua española.
    linguae.wordReference : Open browser and query the WordReference dictionary.
    linguae.wiktionaryQuery : Receive a language and a word and gives definitions from Wiktionary.

    Examples
    --------
    >>> linguae.pons('portuguese','english','idioma')
    https://en.pons.com/translate/portuguese-english/idioma
    >>> linguae.pons('english','spanish','language')
    https://en.pons.com/translate/english-spanish/language
    """
    url = 'https://en.pons.com/translate/%s-%s/%s' % (
        from_language, to_language, word)
    print(url)
    webbrowser.open_new_tab(url)


def dlerae(word):
    """
    Open browser and query the Diccionario de la lengua española.

    Parameters
    ----------
    word : str
        word

    See Also
    --------
    linguae.priberam : Open browser and query the Portuguese Priberam dictionary.
    linguae.sinomimos : Open browser and query the Portuguese Sinonimos dictionary.
    linguae.linguee : Open browser and query the multilingual Linguee dictionary.
    linguae.glosbe : Open browser and query the multilingual Glosbe dictionary.
    linguae.dictionary_com : Open browser and query the English dictionary.com.
    linguae.thesaurus : Open browser and query the English thesaurus dictionary.
    linguae.pons : Open browser and query the multilingual Pons dictionary.
    linguae.wordReference : Open browser and query the WordReference dictionary.
    linguae.wiktionaryQuery : Receive a language and a word and gives definitions from Wiktionary.

    Examples
    --------
    >>> linguae.dlerae('idioma')
    https://dle.rae.es/idioma?m=form
    """
    if ' ' in word:
        word = re.sub(' ', '-', word)
    url = 'https://dle.rae.es/%s?m=form' % word
    print(url)
    webbrowser.open_new_tab(url)


def wordReference(language, word):
    """
    Open browser and query the WordReference dictionary.

    Parameters
    ----------
    language : str
        Language of the word.
        examples: 'en', 'es', 'ca', 'it'

    word : str
        word

    See Also
    --------
    linguae.priberam : Open browser and query the Portuguese Priberam dictionary.
    linguae.sinomimos : Open browser and query the Portuguese Sinonimos dictionary.
    linguae.linguee : Open browser and query the multilingual Linguee dictionary.
    linguae.glosbe : Open browser and query the multilingual Glosbe dictionary.
    linguae.dictionary_com : Open browser and query the English dictionary.com.
    linguae.thesaurus : Open browser and query the English thesaurus dictionary.
    linguae.pons : Open browser and query the multilingual Pons dictionary.
    linguae.dlerae : Open browser and query the Diccionario de la lengua española.
    linguae.wiktionaryQuery : Receive a language and a word and gives definitions from Wiktionary.

    Examples
    --------
    >>> linguae.wordReference('en','language')
    https://www.wordreference.com/definition/language
    >>> linguae.wordReference('es','idioma')
    https://www.wordreference.com/definicion/idioma
    """
    if language == 'es':
        url = 'https://www.wordreference.com/definicion/%s' % word
    elif language == 'en':
        url = 'https://www.wordreference.com/definition/%s' % word
    elif language == 'it':
        url = 'https://www.wordreference.com/definizione/%s' % word
    elif language == 'ca':
        url = 'https://www.wordreference.com/definicio/%s' % word
    else:
        print('%s language is not supported' % language)
        return
    print(url)
    webbrowser.open_new_tab(url)
