"""
Module to query Wikipedia
"""
import wikipedia
import wikipediaapi


def wikipediaQuery(language, query):
    """
    Query Wikipedia.

    Parameters
    ----------
    language : str
        Language of the wikipedia.
        example: 'en', 'pt', 'es', 'fr', 'de', 'ro', 'ca', 'it', 'nl'

    query : str
        words to be queried.

    Returns
    -------
    str
        String with the wikipedia page summary.

    See Also
    --------
    linguae.wiktionaryQuery : Receive a language and a word and gives definitions from Wiktionary.

    Examples
    --------
    >>> linguae.wikipediaQuery('en','English language')
    >>> linguae.wikipediaQuery('pt','Língua portuguesa')
    >>> linguae.wikipediaQuery('es','Idioma español')
    """
    wikipedia.set_lang(language)
    results = wikipedia.search(query)
    if len(results) == 0:
        return("Page not found!")
    wiki_wiki = wikipediaapi.Wikipedia(language)
    page = wiki_wiki.page(results[0])
    if 'may refer to' in page.summary:
        page = wiki_wiki.page(results[1])
    return(page.summary)
