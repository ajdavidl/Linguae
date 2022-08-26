"""
Module to create concordance views for a given word.
Is uses NLTK under the hood.
"""
import nltk

MAX_NR_SENTENCES = 100000


def concordance(listSentences, word):
    """
        Return the concordances of a word in a list of sentences

        It uses the NLTK package under the hood.

        Parameters
        ----------
        listSentences : list
            List of sentences

        word : str
            word

        Returns
        -------
        str
            String with the text of the word concordances.
        """
    if len(listSentences) > MAX_NR_SENTENCES:
        listSentences = listSentences[:MAX_NR_SENTENCES]
    tokens = nltk.word_tokenize("\n".join(listSentences))
    text1 = nltk.Text(tokens)
    results = text1.concordance_list(word, width=100, lines=20)
    textOutput = ""
    for i in range(len(results)):
        textOutput = textOutput + \
            results[i][4] + " " + results[i][1] + " " + results[i][5] + "\n"
    return(textOutput)
