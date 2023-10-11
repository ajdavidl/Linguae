"""
Module with functions that query dictionaries
"""

import webbrowser
import re
import requests
from bs4 import BeautifulSoup


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
    linguae.wikipediaQuery : Query Wikipedia. 
    linguae.wikwik : Open browser and query the Wikwik dictionary.
    linguae.thefreedictionary : Open browser and query the Free Dictionary.
    linguae.wikdict : Open browser and query the Wikdict dictionary.
    linguae.reversoDictionary : Open browser and query the reverso dictionary.

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
    linguae.wikipediaQuery : Query Wikipedia. 
    linguae.wikwik : Open browser and query the Wikwik dictionary.
    linguae.thefreedictionary : Open browser and query the Free Dictionary.
    linguae.wikdict : Open browser and query the Wikdict dictionary.
    linguae.reversoDictionary : Open browser and query the reverso dictionary.

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
    linguae.wikipediaQuery : Query Wikipedia. 
    linguae.wikwik : Open browser and query the Wikwik dictionary.
    linguae.thefreedictionary : Open browser and query the Free Dictionary.
    linguae.wikdict : Open browser and query the Wikdict dictionary.
    linguae.reversoDictionary : Open browser and query the reverso dictionary.

    Examples
    --------
    >>> linguae.linguee('portuguese','english','idioma')
    https://www.linguee.com/portuguese-english/search?source=portuguese&query=idioma
    >>> linguae.linguee('english','spanish','language')
    https://www.linguee.com/english-spanish/search?source=english&query=language
    """
    url = 'https://www.linguee.com/%s-%s/search?source=%s&query=%s' % (
        from_language.lower(), to_language.lower(), from_language.lower(), word)
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
    linguae.wikipediaQuery : Query Wikipedia. 
    linguae.wikwik : Open browser and query the Wikwik dictionary.
    linguae.thefreedictionary : Open browser and query the Free Dictionary.
    linguae.wikdict : Open browser and query the Wikdict dictionary.
    linguae.glosbeScrap : Scrap the multilingual Glosbe dictionary and return translations and expressions.
    linguae.reversoDictionary : Open browser and query the reverso dictionary.

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
    linguae.wikipediaQuery : Query Wikipedia. 
    linguae.wikwik : Open browser and query the Wikwik dictionary.
    linguae.thefreedictionary : Open browser and query the Free Dictionary.
    linguae.wikdict : Open browser and query the Wikdict dictionary.
    linguae.reversoDictionary : Open browser and query the reverso dictionary.

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
    linguae.wikipediaQuery : Query Wikipedia. 
    linguae.wikwik : Open browser and query the Wikwik dictionary.
    linguae.thefreedictionary : Open browser and query the Free Dictionary.
    linguae.wikdict : Open browser and query the Wikdict dictionary.
    linguae.reversoDictionary : Open browser and query the reverso dictionary.

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
    linguae.wikipediaQuery : Query Wikipedia. 
    linguae.wikwik : Open browser and query the Wikwik dictionary.
    linguae.thefreedictionary : Open browser and query the Free Dictionary.
    linguae.wikdict : Open browser and query the Wikdict dictionary.
    linguae.reversoDictionary : Open browser and query the reverso dictionary.

    Examples
    --------
    >>> linguae.pons('portuguese','english','idioma')
    https://en.pons.com/translate/portuguese-english/idioma
    >>> linguae.pons('english','spanish','language')
    https://en.pons.com/translate/english-spanish/language
    """
    url = 'https://en.pons.com/translate/%s-%s/%s' % (
        from_language.lower(), to_language.lower(), word)
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
    linguae.wikipediaQuery : Query Wikipedia. 
    linguae.wikwik : Open browser and query the Wikwik dictionary.
    linguae.thefreedictionary : Open browser and query the Free Dictionary.
    linguae.wikdict : Open browser and query the Wikdict dictionary.
    linguae.reversoDictionary : Open browser and query the reverso dictionary.

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
    linguae.wikipediaQuery : Query Wikipedia. 
    linguae.wikwik : Open browser and query the Wikwik dictionary.
    linguae.thefreedictionary : Open browser and query the Free Dictionary.
    linguae.wikdict : Open browser and query the Wikdict dictionary.
    linguae.reversoDictionary : Open browser and query the reverso dictionary.

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


def wikwik(language, word):
    """
    Open browser and query the Wikwik dictionary.

    Parameters
    ----------
    language : str
        Language of the word.
        examples: 'en', 'es', 'fr', 'it', 'de', 'pt, 'nl'

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
    linguae.wordReference : Open browser and query the WordReference dictionary.
    linguae.wiktionaryQuery : Receive a language and a word and gives definitions from Wiktionary.
    linguae.wikipediaQuery : Query Wikipedia. 
    linguae.thefreedictionary : Open browser and query the Free Dictionary.
    linguae.wikdict : Open browser and query the Wikdict dictionary.
    linguae.reversoDictionary : Open browser and query the reverso dictionary.

    Examples
    --------
    >>> linguae.wikwik('en','language')
    https://en.wikwik.org/language
    >>> linguae.wikwik('es','idioma')
    https://es.wikwik.org/idioma
    """
    if language in ['en', 'es', 'pt', 'it', 'fr', 'de', 'nl']:
        url = 'https://%s.wikwik.org/%s' % (language, word)
    else:
        print('%s language is not supported' % language)
        return
    print(url)
    webbrowser.open_new_tab(url)


def thefreedictionary(language, word):
    """
    Open browser and query the the Free Dictionary.

    Parameters
    ----------
    language : str
        Language of the word.
        examples: 'en', 'es', 'fr', 'it', 'de', 'pt, 'nl'

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
    linguae.wordReference : Open browser and query the WordReference dictionary.
    linguae.wiktionaryQuery : Receive a language and a word and gives definitions from Wiktionary.
    linguae.wikipediaQuery : Query Wikipedia. 
    linguae.wikwik : Open browser and query the Wikwik dictionary.
    linguae.wikdict : Open browser and query the Wikdict dictionary.
    linguae.reversoDictionary : Open browser and query the reverso dictionary.

    Examples
    --------
    >>> linguae.thefreedictionary('en','language')
    https://www.thefreedictionary.com/language
    >>> linguae.thefreedictionary('es','idioma')
    https://es.thefreedictionary.com/idioma
    """
    if language == 'en':
        url = 'https://www.thefreedictionary.com/%s' % (word)
    elif language in ['es', 'pt', 'it', 'fr', 'de', 'nl']:
        url = 'https://%s.thefreedictionary.com/%s' % (language, word)
    else:
        print('%s language is not supported' % language)
        return
    print(url)
    webbrowser.open_new_tab(url)


def wikdict(from_language, to_language, word):
    """
    Open browser and query the Wikdict dictionary.

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
    linguae.glosbe : Open browser and query the multilingual Glosbe dictionary.
    linguae.dictionary_com : Open browser and query the English dictionary.com.
    linguae.thesaurus : Open browser and query the English thesaurus dictionary.
    linguae.pons : Open browser and query the multilingual Pons dictionary.
    linguae.dlerae : Open browser and query the Diccionario de la lengua española.
    linguae.wordReference : Open browser and query the WordReference dictionary.
    linguae.wiktionaryQuery : Receive a language and a word and gives definitions from Wiktionary.
    linguae.wikipediaQuery : Query Wikipedia. 
    linguae.wikwik : Open browser and query the Wikwik dictionary.
    linguae.thefreedictionary : Open browser and query the Free Dictionary.
    linguae.reversoDictionary : Open browser and query the reverso dictionary.

    Examples
    --------
    >>> linguae.wikdict('pt','en','idioma')
    https://www.wikdict.com/pt-en/idioma
    >>> linguae.wikdict('en','es','language')
    https://www.wikdict.com/en-es/language
    """
    url = 'https://www.wikdict.com/%s-%s/%s' % (
        from_language, to_language, word)
    print(url)
    webbrowser.open_new_tab(url)


def glosbeScrap(from_language, to_language, word):
    """
    Scrap the multilingual Glosbe dictionary and return translations and expressions.

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

    Returns
    -------
    dict
        A python dictionary whit the translation and expressions.

    See Also
    --------
    linguae.ponsScrap : Scrap the Pons dictionary and return translations.
    linguae.glosbe : Open browser and query the multilingual Glosbe dictionary.

    Examples
    --------
    >>> linguae.glosbeScrap('pt','en','idioma')
    >>> linguae.glosbeScrap('en','es','language')
    """
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"

    text = {}

    URL_GLOSBE = 'https://pt.glosbe.com/%s/%s/%s' % (
        from_language, to_language, word)

    print(URL_GLOSBE)
    response = requests.get(URL_GLOSBE, headers={
                            'User-agent': user_agent})
    soup = BeautifulSoup(response.content, 'html.parser')

    words = []
    for div in soup.findAll('h3'):
        words.append(div.text)

    text[word] = words

    expressions = {}
    for li in soup.findAll('li', {'class': 'px-2 py-1 flex even:bg-slate-100'}):
        a = li.find('a')
        div = li.findAll('div')
        s = re.sub('\n', ' ', a.text)
        try:
            t = re.sub('\n', ' ', div[1].text)
            expressions[s] = t
        except:
            pass
    text['expressions'] = expressions
    return text


def ponsScrap(from_language, to_language, word):
    """
    Scrap the Pons dictionary and return translations.

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

    Returns
    -------
    dict
        A python dictionary whit the translation and expressions.

    See Also
    --------
    linguae.glosbeScrap : Scrap the multilingual Glosbe dictionary and return translations and expressions.
    linguae.pons : Open browser and query the multilingual Pons dictionary.

    Examples
    --------
    >>> linguae.ponsScrap('portuguese','english','idioma')
    >>> linguae.ponsScrap('english','spanish','language')
    """
    from_language = from_language.lower()
    to_language = to_language.lower()
    text = {}

    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"

    URL_PONS = 'https://en.pons.com/translate/%s-%s/%s' % (
        from_language, to_language, word)
    print(URL_PONS)

    response = requests.get(URL_PONS, headers={
                            'User-agent': user_agent})
    soup = BeautifulSoup(response.content, 'html.parser')

    wordsSource = []
    wordsTarget = []

    for div in soup.findAll('div', {'class': 'source'}):
        wordsSource.append(div.text)

    for div in soup.findAll('div', {'class': 'target'}):
        wordsTarget.append(div.text)

    if len(wordsSource) == len(wordsTarget):
        for i in range(1, len(wordsTarget)):
            s = re.sub('\n', '', wordsSource[i])
            t = re.sub('\n', '', wordsTarget[i])
            text[s] = t
    return text


def lingueeScrap(from_language, to_language, word):
    from_language = from_language.lower()
    to_language = to_language.lower()
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    text = {}

    URL_LINGUEE = 'https://www.linguee.com/%s-%s/search?source=auto&query=%s' % (
        from_language, to_language, word)
    print(URL_LINGUEE)

    response = requests.get(URL_LINGUEE, headers={
                            'User-agent': user_agent})
    soup = BeautifulSoup(response.content, 'html.parser')

    wordsList = []
    for div in soup.findAll('div', {'class': 'translation sortablemg'}):
        t = re.sub('\n', '', div.text)
        wordsList.append(t)

    text[word] = wordsList
    return text


def reversoDictionary(from_language, to_language, word):
    """
    Open browser and query the reverso dictionary.

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
    linguae.linguee : Open browser and query the multilingual Linguee dictionary.
    linguae.glosbe : Open browser and query the multilingual Glosbe dictionary.
    linguae.dictionary_com : Open browser and query the English dictionary.com.
    linguae.thesaurus : Open browser and query the English thesaurus dictionary.
    linguae.pons : Open browser and query the multilingual Pons dictionary.
    linguae.dlerae : Open browser and query the Diccionario de la lengua española.
    linguae.wordReference : Open browser and query the WordReference dictionary.
    linguae.wiktionaryQuery : Receive a language and a word and gives definitions from Wiktionary.
    linguae.wikipediaQuery : Query Wikipedia. 
    linguae.wikwik : Open browser and query the Wikwik dictionary.
    linguae.thefreedictionary : Open browser and query the Free Dictionary.
    linguae.wikdict : Open browser and query the Wikdict dictionary.

    Examples
    --------
    >>> linguae.reversoDictionary('english','spanish','language')
    https://dictionary.reverso.net/english-spanish/language
    >>> linguae.reversoDictionary('portuguese','english','idioma')
    https://dictionary.reverso.net/portuguese-english/idioma
    """
    url = 'https://dictionary.reverso.net/%s-%s/%s' % (
        from_language.lower(), to_language.lower(), word)
    print(url)
    webbrowser.open_new_tab(url)
