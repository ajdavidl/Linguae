# Dictionary module

Module with functions that query dictionaries.

Functions:

```
- linguae.priberam : Open browser and query the Portuguese Priberam dictionary.
- linguae.sinomimos : Open browser and query the Portuguese Sinonimos dictionary.
- linguae.linguee : Open browser and query the multilingual Linguee dictionary.
- linguae.glosbe : Open browser and query the multilingual Glosbe dictionary.
- linguae.dictionary_com : Open browser and query the English dictionary.com.
- linguae.thesaurus : Open browser and query the English thesaurus dictionary.
- linguae.pons : Open browser and query the multilingual Pons dictionary.
- linguae.dlerae : Open browser and query the Diccionario de la lengua española.
- linguae.wordReference : Open browser and query the WordReference dictionary.
- linguae.wiktionaryQuery : Receive a language and a word and gives definitions from Wiktionary.
```

Examples:

- Priberam
```python
>>> import linguae
>>> linguae.priberam('idioma')
    https://dicionario.priberam.org/idioma
```

- Sinonimos
```python
>>> import linguae
>>> linguae.sinomimos('idioma')
https://www.sinonimos.com.br/idioma/
```

- Linguee
```python
>>> import linguae
>>> linguae.linguee('portuguese','english','idioma')
https://www.linguee.com/portuguese-english/search?source=portuguese&query=idioma
>>> linguae.linguee('english','spanish','language')
https://www.linguee.com/english-spanish/search?source=english&query=language
```

- Glosbe
```python
>>> import linguae
>>> linguae.glosbe('pt','en','idioma')
https://glosbe.com/pt/en/idioma
>>> linguae.glosbe('en','es','language')
https://glosbe.com/en/es/language
```

- Dictionary.com
```python
>>> import linguae
>>> linguae.dictionary_com('language')
https://www.dictionary.com/browse/language
```

- Thesaurus
```python
>>> import linguae
>>> linguae.thesaurus('language')
https://www.thesaurus.com/browse/language
```

- Pons
```python
>>> import linguae
>>> linguae.pons('portuguese','english','idioma')
https://en.pons.com/translate/portuguese-english/idioma
>>> linguae.pons('english','spanish','language')
https://en.pons.com/translate/english-spanish/language
```

- DLR.RAE
```python
>>> import linguae
>>> linguae.dlerae('idioma')
https://dle.rae.es/idioma?m=form
```

- Word Reference
```python
>>> import linguae
>>> linguae.wordReference('en','language')
https://www.wordreference.com/definition/language
>>> linguae.wordReference('es','idioma')
https://www.wordreference.com/definicion/idioma
```

- Wiktionary
```python
>>> import linguae
>>> s = linguae.wiktionaryQuery('en', 'language')
>>> print(s)
Definitions: language (countable and uncountable, plural languages)
(countable) A body of words, and set of methods of combining them (called a grammar), understood by a community and used as a form of communication.
(uncountable) The ability to communicate using words.
(uncountable) A sublanguage: the slang of a particular community or jargon of a particular specialist field.
(countable, uncountable, figuratively) The expression of thought (the communication of meaning) in a specified way; that which communicates something, as language does.
(countable, uncountable) A body of sounds, signs and/or signals by which animals communicate, and by which plants are sometimes also thought to communicate.
(computing, countable) A computer language; a machine language.
(uncountable) Manner of expression.
(uncountable) The particular words used in a speech or a passage of text.
(uncountable) Profanity.
>>> s = linguae.wiktionaryQuery('pt', 'idioma')
>>> print(s)
Definitions: idioma m (plural idiomas)
language (form of communication using words and structured with grammar)
```
