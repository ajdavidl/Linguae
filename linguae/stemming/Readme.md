# Stemming module

Module to do stemming task. It uses the [NLTK](https://github.com/nltk/nltk) package.

Main function:

```
linguae.stem : Stem a given token.
```

Examples:

```python
>>> import linguae
>>> linguae.stem('en','languages')
'languag'
>>> linguae.stem('pt','idiomas')
'idiom'
