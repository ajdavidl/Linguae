# Translation module

Module to translate sentences between languages.

Functions:

```
linguae.translate : Translate text from one language to another.
linguae.googleTranslate : Open browser and query Google translate site.
```

Examples:

```python
>>> import linguae
>>> linguae.translate('pt','en','Aprender idiomas é divertido.')
'Learning languages is fun.'
>>> linguae.googleTranslate('pt','en','Aprender idiomas é divertido.')
https://translate.google.com.br/?sl=pt&tl=en&text=Aprender%20idiomas%20é%20divertido.&op=translate
```