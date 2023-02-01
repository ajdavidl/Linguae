# Tatoeba module

Module to load tatoeba data and query [tatoeba site](https://tatoeba.org/).

Functions:

```
linguae.loadTatoeba : Read the csv file from Tatoeba and returns a Pandas dataframe with the sentences.
linguae.loadLanguageTatoeba : Read the csv file from Tatoeba and returns a list with the sentences.
linguae.tatoebaSite : Open browser and query tatoeba site.
```

Examples:

* loadTatoeba:

```python
>>> import linguae
>>> dfTatoeba = linguae.loadTatoeba()
>>> dfTatoeba.info()
```

* loadLanguageTatoeba:

```python
>>> import linguae
>>> engList = linguae.loadLanguageTatoeba('eng')
>>> print(engList[:5])
>>> porList = linguae.loadLanguageTatoeba('por')
>>> print(porList[:5])
```

* tatoebaSite:

```python
>>> import linguae
>>> linguae.tatoebaSite('language','eng')
https://tatoeba.org/en/sentences/search?from=eng&query=language
>>> linguae.tatoebaSite('idioma','por','eng')
https://tatoeba.org/en/sentences/search?from=por&query=idioma&to=eng
```
