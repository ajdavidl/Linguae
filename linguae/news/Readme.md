# News module

Module to bring news from RSS Feeds.

Functions:

```
linguae.googleNews : Return the news' title from Google news using RSS feeds.
linguae.emmNewsBrief : Return the news' title from emm.newsbrief.eu using RSS feeds.
```

Examples:

```python
>>> import linguae
>>> linguae.googleNews('en')
>>> linguae.googleNews('pt', 20)
>>> linguae.emmNewsBrief('es')
>>> linguae.emmNewsBrief('it', 20)
```
