# Class Language

Class Language to centralize functions from the other modules.

Attributes:
```
name : Name of the language.
code2 : 2 letters abbreviation of the language.
code3 : 3 letters abbreviation of the language.
spacyModel : SpaCy model for the language selected.
wordVectorModel : A gensim model with the word vectors loaded.
Bloom : a Pipeline object from the transformers package with the Bloom model loaded.
mGPT : a Pipeline object from the transformers package with the Bloom model loaded.
tatoeba : list of sentences from tatoeba site.
BertMultilingual : a Pipeline object from the transformers package with the Bloom model loaded.
XLMRoberta : a Pipeline object from the transformers package with the Bloom model loaded.
hyphenatorModel : Hyphenator model.
sentenceVectorModel : Sentence transformer model.
tatoebaTensorsEmbeddings : tensor encoded by Sentence Transformer model.
```

# Class English

Class English Language to centralize functions.

I has the same attributes of the Class Language plus:
```
BertEnglish : a Pipeline object from the transformers package with the Bloom model loaded.
GPTEnglish : a Pipeline object from the transformers package with the GPT model loaded.
Sentiment_ : a python dictionary with the English Lexicon.
```
