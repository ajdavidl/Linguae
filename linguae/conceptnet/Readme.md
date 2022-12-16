# Conceptnet module

Module to query [Conceptnet](https://conceptnet.io/), an open, multilingual knowledge graph.

The main function is `conceptnetQuery` that query the Conceptnet API and returns a string with the relations.

Example:

```python
>>> import linguae
>>> s1 = linguae.conceptnetQuery('en','language',5)
>>> print(s1)
Concepts related to language:
1) French (en) IsA a language (en)
2) Spanish (en) IsA language (en)
3) english (en) RelatedTo language (en)
4) German (en) IsA a language (en)
5) Language (en) UsedFor communication (en)
>>> s2 = linguae.conceptnetQuery('pt','idioma',5)
>>> print(s2)
Concepts related to idioma:
1) idioma (pt) Synonym language (en)
2) idioma (pt) Synonym dialect (en)
3) língua (pt) Synonym idioma (pt)
4) idioma (pt) Synonym natural language (en)
5) idioma (pt) Synonym língua (pt)
``` 
