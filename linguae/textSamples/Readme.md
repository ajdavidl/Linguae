# Text samples module

Module to present text samples from a list of text.

You can get a list of text from `linguae` using the [tatoeba](https://github.com/ajdavidl/Linguae/tree/main/linguae/tatoeba) module.

Main function:

```
linguae.textSamples : Return the text samples of an expression in a list of sentences.
```

Examples:

```python
>>> import linguae
>>> engList = linguae.loadLanguageTatoeba('eng')
>>> print(linguae.textSamples(engList, 'language'))
>>> porList = linguae.loadLanguageTatoeba('por')
>>> print(linguae.textSamples(porList, 'idioma'))
```
