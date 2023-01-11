"""
Module to present text samples
"""

import pandas as pd


def textSamples(listSentences, expression, num=20):
    """
    Return the text samples of an expression in a list of sentences.

    Parameters
    ----------
    listSentences : list
        List of sentences.

    expression : str
        words 

    num : integer
        number of examples to show.

    Returns
    -------
    str
        String with the examples of sentences with the given expression.

    See Also
    --------
    linguae.loadTatoeba : Read the csv file from Tatoeba and returns a Pandas dataframe with the sentences.

    Examples
    --------
    >>> engList = linguae.loadLanguageTatoeba('eng')
    >>> print(linguae.textSamples(engList, 'language'))
    >>> porList = linguae.loadLanguageTatoeba('por')
    >>> print(linguae.textSamples(porList, 'idioma'))
    """
    sentencesOk = []
    for sent in listSentences:
        if expression in sent:
            sentencesOk.append(sent)
    if len(sentencesOk) < num:
        return '\n'.join(sentencesOk)
    else:
        sentencesOk = pd.Series(sentencesOk).sample(num).to_list()
        return '\n'.join(sentencesOk)
