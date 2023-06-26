# Report Module

Module to generate a command line report using functions from the Linguae package.

Function:

```
linguae.wordReport : Makes a report about words.
linguae.sentenceReport : Makes a report about sentences.
```

Examples

- wordReport:

```python
>>> import linguae
>>> linguae.wordReport('en','language')
>>> linguae.wordReport('pt','idioma')
```

- sentenceReport:

```python
>>> import linguae
>>> linguae.sentenceReport('en', 'Learn languages is good')
>>> linguae.sentenceReport('pt', 'Aprender idiomas é divertido.')
```
