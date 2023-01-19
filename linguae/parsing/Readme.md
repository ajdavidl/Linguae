# Parsing module

Module to parse sentences and give the part-of-speech tags.

Functions:

```
linguae.loadSpacyModel : Load the Spacy Model for one language.
linguae.parseSpacy : Parse text using spaCy model.
linguae.parse : Parse text from given language.
```

Examples:

- `loadSpacyModel` and `parseSpacy`

```python
>>> import linguae
>>> eng = linguae.loadSpacyModel('en')
>>> print(linguae.parseSpacy(eng,'I love languages.'))
>>> por = linguae.loadSpacyModel('pt')
>>> print(linguae.parseSpacy(por,'Eu amo idiomas.'))
```

- `parse`

```python
>>> import linguae
>>> print(linguae.parse('en','I love languages.'))
>>> print(linguae.parse('pt','Eu amo idiomas.'))
```
