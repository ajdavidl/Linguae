# NER module

Named Entity Recognition module.

Functions:

```
linguae.nerSpacy : Get entities from text using spaCy model.
linguae.dbpediaEntityLink : Link entities from sentence to dbpedia knowledge base.
```

Examples:

- nerSpacy
```python
>>> import linguae
>>> nlp_en = linguae.loadSpacyModel('en')
>>> s = linguae.nerSpacy(nlp_en,'The English language is spoken in England.')
>>> print(s)
Token → Label
English → LANGUAGE
England → GPE
>>> nlp_pt = linguae.loadSpacyModel('pt')
>>> s = linguae.nerSpacy(nlp_en,'A língua portuguesa é falada no Brasil.')
>>> print(s)
Token → Label
Brasil → GPE
```

- dbpediaEntityLink
```python
>>> import linguae
>>> dbpediaEntityLink('en', 'The English language is spoken in England.')
```
