"""
Module to explore sentence similarity using sentence transformer python package (SBERT).
"""

from sentence_transformers import SentenceTransformer, util


def loadSentenceTransformerModel():
    """
        Load a SentenceTransformer model

        It uses the sentence_transformers package to load a multilingual model.

        Returns
        -------
        SentenceTransformer model
            A 'sentence_transformers.SentenceTransformer.SentenceTransformer' model.
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
            the sentences to embed

        Returns
        _______
            a list of tensors is returned
        """
    return model.encode(sentences)


def similarSentences(model, querySentence, listSentences, querySentenceTensor=None, listSentencesTensors=None, nrSentencesReturned=10):
    """
        Gives the most similar sentences from a query sentence using the sentence transformer model.

        Parameters
        ----------
        model : 'sentence_transformers.SentenceTransformer.SentenceTransformer' model.
            Sentence transformer model

        querySentence : str
            sentence to be queried

        listSentences : List[str]
            sentences to be searched

        querySentenceTensor : torch.Tensor
            The query sentence embedding. If None, the tensor is calculated.

        listSentencesTensors : torch.Tensor
            The list sentences' tensors. If None, the tensor is calculated.

        nrSentencesReturned : int
            number of sentences to be returned

        Returns 
        _______
        str
            String with the most similar sentences.
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
