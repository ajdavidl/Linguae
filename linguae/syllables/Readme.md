# Syllables module


Module to split words in syllables.

It uses the [Hyphenator](https://github.com/wbsoft/hyphenator) package under the hood.

Functions:

```
linguae.loadHyphenator : Load the Hyphenator Model for one language.
linguae.syllables : Split the given word in syllables.
```

Example:

```python
>>> import linguae
>>> eng = linguae.loadHyphenator('en')
>>> linguae.syllables(eng, 'language')
'lan-guage'
>>> por = linguae.loadHyphenator('pt')
>>> linguae.syllables(por, 'idioma')
'idi-o-ma'
```
