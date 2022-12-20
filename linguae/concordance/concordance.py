"""
Module to create concordance views for a given word.
It uses NLTK under the hood.
"""
import nltk

MAX_NR_SENTENCES = 100000


def concordance(listSentences, word):
    """
    Return the concordances of a word in a list of sentences.

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

    See Also
    --------
    linguae.loadLanguageTatoeba : Load tatoeba sentences from the given lamguage.

    Examples
    --------
    >>> EngSentences = linguae.loadLanguageTatoeba('eng')
    >>> conc = linguae.concordance(EngSentences,'language')
    >>> print(conc)
    ou tell them they translate it into their own language and turn it into something totally different 
     released , regardless of price . The profane language used on network television makes many parents
     gracefully . Bill Clinton spoke in ambiguous language when asked to describe his relationship with 
     . It is important for you to learn a foreign language . I 'll open the curtain for you to look out 
    ifficult to understand a lecture in a foreign language . The students have taken no notice of these 
     'll find it your advantage to know a foreign language . It is almost impossible to learn a foreign 

    >>> PorSentences = linguae.loadLanguageTatoeba('por')
    >>> conc = linguae.concordance(PorSentences,'idioma')
    >>> print(conc)
     estou muito feliz de te ver ! Aprender bem um idioma estrangeiro requer uma grande quantidade de tr
    l é ? O livro mais importante para aprender um idioma é , naturalmente , um dicionário . Odeio meu v
    eu cavalo . Que língua é falada no Egito ? Que idioma falam no Egito ? Que língua é utilizada no Egi
    rante três dias a partir da meia-noite . O meu idioma não está na lista ! Parte da ilha ficou devast
    sabe como ganhar dinheiro . O inglês não é meu idioma nativo . Inglês não é minha língua nativa . Bi
    , eu fico . Ela está costurando um vestido . O idioma Na'vi é usado em Avatar . Vamos continuar com 
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
