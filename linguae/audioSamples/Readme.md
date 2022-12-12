# AudioSamples module

Module to query audio samples from [Forvo](https://forvo.com) site.

The main function is `forvo` that opens a browser and makes a query to the Forvo site.

Example:

```python
>>> import linguae
>>> linguae.forvo('en','language')
https://forvo.com/search/language/en/
>>> linguae.forvo('pt','idioma')
https://forvo.com/search/idioma/pt/
```
