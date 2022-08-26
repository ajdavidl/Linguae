"""
Module to present text samples given words
"""

import pandas as pd


def textSamples(listSentences, expression, num=20):
    """
        Return the text samples of a expression in a list of sentences

        Parameters
        ----------
        listSentences : list
            List of sentences

        expression : str
            words 

        num : integer
            number of examples to show.

        Returns
        -------
        str
            String with the examples of sentences with the given expression.
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
