# Word frequency module

Module to give the frequency of a word.

It uses the [wordfreq](https://github.com/rspeer/wordfreq) package under the hood.

Main function:

```
linguae.wordFreq : Get the frequency of word in a given language.
```

Examples:

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
