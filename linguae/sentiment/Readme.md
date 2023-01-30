# Sentiment module

Module to get the sentiment/polarity of words and sentences.

Functions:

```
linguae.loadSentiment : Load sentiments lexicon of different languages.
linguae.polarity : Get the sentiment associated to a word.
linguae.sentenceSentiment : Get the sentiment associated to a sentence.
```

Examples:

```python
>>> import linguae
>>> engLex = linguae.loadSentiment('en')
>>> linguae.polarity(engLex, 'good')
0.7
>>> linguae.polarity(engLex, 'bad')
-0.7
>>> porLex = linguae.loadSentiment('pt')
>>> linguae.polarity(porLex, 'bom')
1
>>> linguae.polarity(porLex, 'ruim')
-1
>>> linguae.sentenceSentiment('Learning languages is good.')
Sentiment(polarity=0.7, subjectivity=0.6000000000000001)
```