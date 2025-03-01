# Word frequency module

Module to give the frequency of a word.

It uses the [wordfreq](https://github.com/rspeer/wordfreq) package in the function `wordFreq`. And it uses the sklearn `CountVectorizer` method in the function `frequency`.

Functions:

```
linguae.wordFreq : Get the frequency of word in a given language.
linguae.frequency : Calculate the frequency os tokens (unigrams, bigrams ...) of a list of strings.
```

Examples:

* wordFreq

```python
>>> import linguae
>>> linguae.wordFreq('en', 'the')
'0.0537'
>>> linguae.wordFreq('en', 'language')
'0.000126'
>>> linguae.wordFreq('pt', 'de')
'0.0479'
>>> linguae.wordFreq('pt', 'idioma')
'1.95e-05'
```

* frequency

```python
>>> listEng = linguae.loadLanguageTatoeba('eng')
>>> listEngFreq = linguae.frequency(listEng)
>>> listEngFreq[:10]
[('to', 496283), ('the', 472956), ('tom', 447763), ('that', 314474), ('you', 282733), ('is', 219346), ('he', 186283), ('in', 170506), ('and', 164284), ('of', 163454)]
```