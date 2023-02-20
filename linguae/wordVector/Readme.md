# Word Vector Module

Module to explore word similarity using pre-trained word embeddings. It uses the [gensim](https://radimrehurek.com/gensim/) package under the hood.

Funtions:

```
linguae.loadWordVectors : Load word vectors from the desired language.
linguae.similarWords : Get similar words with word embeddings.
```

Examples:

```python
>>> import linguae
>>> engVectors = linguae.loadWordVectors('en')
>>> porVectors = linguae.loadWordVectors('pt')
>>> spaVectors = linguae.loadWordVectors('es')
>>> print(linguae.similarWords(engVectors, 'language', [porVectors, spaVectors]))
>>> print(linguae.similarWords(porVectors, 'idioma', [engVectors, spaVectors]))
>>> print(linguae.similarWords(spaVectors, 'idioma', [engVectors, porVectors]))
```