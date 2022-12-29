# Image module

Module to search images on internet.

Functions:
```
linguae.googleImages : Open browser and query Google images.
linguae.duckduckGoImages : Open browser and query Duckduckgo images.
```

Examples:

- Google Images:
```python
>>> import linguae
>>> linguae.googleImages("ball")
https://www.google.com/search?tbm=isch&q=ball
>>> linguae.googleImages("bola")
https://www.google.com/search?tbm=isch&q=bola
```

- Duckduckgo images
```python
>>> import linguae
>>> linguae.duckduckGoImages("ball")
https://duckduckgo.com/?q=ball&t=ffab&iar=images&iax=images&ia=images
>>> linguae.duckduckGoImages("bola")
https://duckduckgo.com/?q=bola&t=ffab&iar=images&iax=images&ia=images
```
