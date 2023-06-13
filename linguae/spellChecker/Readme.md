# Spell Checker module

Module to check the spelling of words.

Function:

```
linguae.spellchecker : Check the spelling of words
```

Examples:

```python
>>> import linguae
>>> linguae.spellchecker('en','I am studing languajes!')
studing :
corrections: studying
candidates: {'studding', 'studying'}
languajes :
corrections: languages
candidates: {'languages'}
>>> linguae.spellchecker('pt','Aprendu linguaz!')
linguaz :
corrections: lingua
candidates: {'lingua', 'linguas'}
aprendu :
corrections: aprendi
candidates: {'aprenda', 'aprendeu', 'aprende', 'aprendi', 'aprendo'}
```
