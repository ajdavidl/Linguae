# Verb conjugation module

Module for verb conjugation.

Functions:

```
linguae.conjugation : Conjugate a verb from given language.
linguae.verbix : Open browser and query the Verbix site.
```

Examples:

* conjugation: 
It uses the [verbecc](https://github.com/bretttolbert/verbecc) package under the hood.

```python
>>> import linguae
>>> linguae.conjugation('pt','aprender')
>>> linguae.conjugation('es','aprender')
>>> linguae.conjugation('it','imparare')
```

* verbix

```python
>>> import linguae
>>> linguae.verbix('english','learn')
https://www.verbix.com/webverbix/english/learn
>>> linguae.verbix('portuguese','aprender')
https://www.verbix.com/webverbix/portuguese/aprender
>>> linguae.verbix('spanish','aprender')
https://www.verbix.com/webverbix/spanish/aprender
```