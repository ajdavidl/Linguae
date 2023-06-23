"""
Module to explore sentence similarity using sentence transformer python package (SBERT).
"""

from sentence_transformers import SentenceTransformer, util


def loadSentenceTransformerModel():
    """
    Load a SentenceTransformer model.

    It uses the sentence_transformers package to load a multilingual model.

    Returns
    -------
    SentenceTransformer model
        A 'sentence_transformers.SentenceTransformer.SentenceTransformer' model.

    See Also
    --------
    linguae.encodeSentence : Computes sentence embeddings using sentence_transformers package.
    linguae.similarSentences : Gives the most similar sentences from a query sentence using the sentence transformer model.
    linguae.loadWordVectors : Load word vectors from the desired language.
    linguae.similarWords : Get similar words with word embeddings.

    Examples
    --------
    >>> sentTransfModel = linguae.loadSentenceTransformerModel()
    >>> linguae.encodeSentence(sentTransfModel, 'Learn languages is good.')

    """
    return SentenceTransformer('paraphrase-multilingual-mpnet-base-v2')


def encodeSentence(model, sentences):
    """
    Computes sentence embeddings using sentence_transformers package.

    Parameters
    ----------
    model : 'sentence_transformers.SentenceTransformer.SentenceTransformer' model.
        Sentence transformer model

    sentences : Union[str, List[str]]
        The sentences to embed.

    Returns
    -------
        A list of tensors is returned.

    See Also
    --------
    linguae.loadSentenceTransformerModel : Load a SentenceTransformer model.
    linguae.similarSentences : Gives the most similar sentences from a query sentence using the sentence transformer model.
    linguae.loadWordVectors : Load word vectors from the desired language.
    linguae.similarWords : Get similar words with word embeddings.

    Examples
    --------
    >>> sentTransfModel = linguae.loadSentenceTransformerModel()
    >>> linguae.encodeSentence(sentTransfModel, 'Learn languages is good.')

    It's also possible to encode a list of sentences.

    >>> sentTransfModel = linguae.loadSentenceTransformerModel()
    >>> linguae.encodeSentence(sentTransfModel, ['Learn languages is good.', 'I like to learn languages.'])
    """
    if len(sentences) == 0:
        print("Error while encoding sentences. The list of sentences is empty.")
        return
    return model.encode(sentences)


def similarSentences(model, querySentence, listSentences, querySentenceTensor=None, listSentencesTensors=None, nrSentencesReturned=10):
    """
    Gives the most similar sentences from a query sentence using the sentence transformer model.

    Parameters
    ----------
    model : 'sentence_transformers.SentenceTransformer.SentenceTransformer' model.
        Sentence transformer model.

    querySentence : str
        Sentence to be queried.

    listSentences : List[str]
        Sentences to be searched.

    querySentenceTensor : torch.Tensor
        The query sentence embedding. If None, the tensor is calculated.

    listSentencesTensors : torch.Tensor
        The list sentences' tensors. If None, the tensor is calculated.

    nrSentencesReturned : int (default=10)
        number of sentences to be returned.

    Returns 
    -------
    str
        String with the most similar sentences.

    See Also
    --------
    linguae.loadSentenceTransformerModel : Load a SentenceTransformer model.
    linguae.encodeSentence : Computes sentence embeddings using sentence_transformers package.
    linguae.loadWordVectors : Load word vectors from the desired language.
    linguae.similarWords : Get similar words with word embeddings.

    Examples
    --------
    >>> sentTransfModel = linguae.loadSentenceTransformerModel()
    >>> listEnglishSentences = linguae.loadLanguageTatoeba('eng')
    >>> listEnglishSentencesSample = listEnglishSentences[:10000]
    >>> print(linguae.similarSentences(sentTransfModel, 'Learn languages is good', listEnglishSentencesSample))

    You can pass the tensors of the query sentence and the tensors of the sentences in the list.

    >>> sentTransfModel = linguae.loadSentenceTransformerModel()
    >>> listEnglishSentences = linguae.loadLanguageTatoeba('eng')
    >>> myListOfSentences = listEnglishSentences[:10000]
    >>> myListOfSentencesTensors = linguae.encodeSentence(sentTransfModel, myListOfSentences)
    >>> mySentenceQuery = 'Learning languages is good.'
    >>> mySentenceQueryTensor = linguae.encodeSentence(sentTransfModel, mySentenceQuery)
    >>> print(linguae.similarSentences(sentTransfModel, mySentenceQuery, myListOfSentences, mySentenceQueryTensor, myListOfSentencesTensors))
    """
    if querySentenceTensor is None:
        querySentenceTensor = model.encode(querySentence)
    if listSentencesTensors is None:
        listSentencesTensors = model.encode(listSentences)
    similarities = util.cos_sim(querySentenceTensor, listSentencesTensors)
    similarities = similarities.argsort(descending=True).tolist()
    if nrSentencesReturned < len(listSentences):
        similarities = similarities[0][:nrSentencesReturned]
    listSentences = [listSentences[i] for i in similarities]
    return '\n'.join(listSentences)
