# Sentence Vector Module

Module to explore sentence similarity using sentence transformer python package ([SBERT](https://www.sbert.net/)).

Functions:

```
linguae.loadSentenceTransformerModel : Load a SentenceTransformer model.
linguae.encodeSentence : Computes sentence embeddings using sentence_transformers package.
linguae.similarSentences : Gives the most similar sentences from a query sentence using the sentence transformer model.
```

Examples:

```python
>>> import linguae
>>> sentTransfModel = linguae.loadSentenceTransformerModel()
>>> listEnglishSentences = linguae.loadLanguageTatoeba('eng')
>>> listEnglishSentencesSample = listEnglishSentences[:10000]
>>> print(linguae.similarSentences(sentTransfModel, 'Learn languages is good', listEnglishSentencesSample))
```

You can pass the tensors of the query sentence and the tensors of the sentences in the list.

```python
>>> sentTransfModel = linguae.loadSentenceTransformerModel()
>>> listEnglishSentences = linguae.loadLanguageTatoeba('eng')
>>> myListOfSentences = listEnglishSentences[:10000]
>>> myListOfSentencesTensors = linguae.encodeSentence(sentTransfModel, myListOfSentences)
>>> mySentenceQuery = 'Learning languages is good.'
>>> mySentenceQueryTensor = linguae.encodeSentence(sentTransfModel, mySentenceQuery)
>>> print(linguae.similarSentences(sentTransfModel, mySentenceQuery, myListOfSentences, mySentenceQueryTensor, myListOfSentencesTensors))
```