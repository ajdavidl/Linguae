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
GPT : a Pipeline object from the transformers package with the GPT monolingual model loaded.
mGPT : a Pipeline object from the transformers package with the GPT multilingual model loaded.
tatoeba : list of sentences from tatoeba site.
Bert : a Pipeline object from the transformers package with the monolingual Bert model loaded.
BertMultilingual : a Pipeline object from the transformers package with the multilingual Bert model loaded.
XLMRoberta : a Pipeline object from the transformers package with the XLMRoberta model loaded.
hyphenatorModel : Hyphenator model.
sentenceVectorModel : Sentence transformer model.
tatoebaTensorsEmbeddings : tensor encoded by Sentence Transformer model.
LLM : 'langchain.llms.gpt4all.GPT4All' large language model.
ConceptnetNumberbatch : gensim KeyedVectors model with the Conceptnet numberbatch vectors loaded.
```

# Class English

Attributes:
```
BertEnglish : a Pipeline object from the transformers package with the Bloom model loaded.
GPTEnglish : a Pipeline object from the transformers package with the GPT model loaded.
Sentiment_ : a python dictionary with the English Lexicon.
```

# Class Portuguese

Attributes:
```
BertPortuguese : a Pipeline object from the transformers package with the Bloom model loaded.
GPTPortuguese : a Pipeline object from the transformers package with the Bloom model loaded.
Sentiment_ : a python dictionary with the Portuguese Lexicon.
```

# Class Spanish

Attributes:
```
BertSpanish : a Pipeline object from the transformers package with the Bloom model loaded.
GPTSpanish : a Pipeline object from the transformers package with the Bloom model loaded.
Sentiment_ : a python dictionary with the Spanish Lexicon.
```

# Class Italian

Attributes:
```
Sentiment_ : a python dictionary with the Italian Lexicon.
```

# Class French

Attributes:
```
Sentiment_ : a python dictionary with the Italian Lexicon.
```

# Class German

Attributes:
```
Sentiment_ : a python dictionary with the Italian Lexicon.
```


