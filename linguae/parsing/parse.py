"""
Module to parse sentences and give the part-of-speech tags.
"""
from spacy import load

SPACY_MODEL_PT = "pt_core_news_sm"
SPACY_MODEL_EN = "en_core_web_sm"
SPACY_MODEL_ES = "es_core_news_sm"
SPACY_MODEL_IT = "it_core_news_sm"
SPACY_MODEL_FR = "fr_core_news_sm"
SPACY_MODEL_DE = "de_core_news_sm"
SPACY_MODEL_RO = "ro_core_news_sm"


def loadSpacyModel(language):
    """
    Load the Spacy Model for one language.

    Parameters
    ----------
    language : str
    	Language of the text.
	example: 'en', 'pt', 'es', 'fr', 'de', 'ro', 'it'

    Returns
    -------
    class spacy.lang
	SpaCy model for the language selected.

    See Also
    --------
    linguae.parseSpacy : Parse text using spaCy model.
    linguae.parse : Parse text from given language.

    Examples
    --------
    >>> import linguae
    >>> eng = linguae.loadSpacyModel('en')
    >>> por = linguae.loadSpacyModel('pt')
    """
    if language == 'pt':
        nlp = load(SPACY_MODEL_PT)
    elif language == 'en':
        nlp = load(SPACY_MODEL_EN)
    elif language == 'es':
        nlp = load(SPACY_MODEL_ES)
    elif language == 'it':
        nlp = load(SPACY_MODEL_IT)
    elif language == 'fr':
        nlp = load(SPACY_MODEL_FR)
    elif language == 'de':
        nlp = load(SPACY_MODEL_FR)
    elif language == 'ro':
        nlp = load(SPACY_MODEL_RO)
    else:
        print("Language not supported!")
        return None
    return nlp


def parseSpacy(model, sentence):
    """
    Parse text using spaCy model.

    Parameters
    ----------
    model : spacy.lang
	SpaCy Language model.

    sentence : str
	Text to be parsed.

    Returns
    -------
    str
	String with the token, pos, tags and dependencies in a table format.
    
    See Also
    --------
    linguae.loadSpacyModel : Load the Spacy Model for one language.
    linguae.parse : Parse text from given language.

    Examples
    --------
    >>> import linguae
    >>> eng = linguae.loadSpacyModel('en')
    >>> print(linguae.parseSpacy(eng,'I love languages.'))
    >>> por = linguae.loadSpacyModel('pt')
    >>> print(linguae.parseSpacy(por,'Eu amo idiomas.'))
    """
    doc = model(sentence)
    text = "Token → POS → Tag → Dep\n"
    for token in doc:
        text += token.text + ' → ' + token.pos_ + \
            ' → ' + token.tag_ + ' → ' + token.dep_ + '\n'
    return text


def parse(language, sentence):
    """
    Parse text from given language.

    It uses the SpaCy package under the hood.

    Parameters
    ----------
    language : str
	Language of the text.
	example: 'en', 'pt', 'es', 'fr', 'de', 'ro', 'it'

    sentence : str
	Text to be parsed

    Returns
    -------
    str
	String with the token, pos, tags and dependencies in a table format.
	
    See Also
    --------
    linguae.loadSpacyModel : Load the Spacy Model for one language.
    linguae.parseSpacy : Parse text using spaCy model.

    Examples
    --------
    >>> import linguae
    >>> print(linguae.parse('en','I love languages.'))
    >>> print(linguae.parse('pt','Eu amo idiomas.'))
    """
    if language == 'pt':
        nlp = load(SPACY_MODEL_PT)
    elif language == 'en':
        nlp = load(SPACY_MODEL_EN)
    elif language == 'es':
        nlp = load(SPACY_MODEL_ES)
    elif language == 'it':
        nlp = load(SPACY_MODEL_IT)
    elif language == 'fr':
        nlp = load(SPACY_MODEL_FR)
    elif language == 'de':
        nlp = load(SPACY_MODEL_FR)
    elif language == 'ro':
        nlp = load(SPACY_MODEL_RO)
    else:
        print("Language not supported!")
        return ""
    doc = nlp(sentence)
    text = "Token → POS → Tag → Dep\n"
    for token in doc:
        text += token.text + ' → ' + token.pos_ + \
            ' → ' + token.tag_ + ' → ' + token.dep_ + '\n'
    return text
