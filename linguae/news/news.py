"""
Module to bring news from RSS Feeds
"""

import feedparser
import re


def strip_html_tags(text):
    """
        Strip html tags in a given text

        Parameters
        ----------
        text : str
            Text to be cleaned.

        Returns
        -------
        str
            String with the text cleaned.
        """
    p = re.compile(r'<.*?>')
    return p.sub('', text)


def googleNews(language, num=None):
    """
        Return the news' title from Google news using RSS feeds.

        Parameters
        ----------
        language : str
            Language of the news.
            example: 'en', 'pt', 'es', 'fr', 'de', 'ro', 'ca', 'it', 'nl'

        num : integer
            Maximum number of news to be returned.

        Returns
        -------
        str
            String with the titles of the news.
        """
    if language == 'pt':
        url = "https://news.google.com/rss/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx1YlY4U0JYQjBMVUpTR2dKQ1VpZ0FQAQ?hl=pt-BR&gl=BR&ceid=BR%3Apt-419"
    elif language == 'en':
        url = "https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US:en"
    elif language == 'es':
        url = "https://news.google.com/rss/topics/CAAqLAgKIiZDQkFTRmdvSUwyMHZNRGx1YlY4U0JtVnpMVFF4T1JvQ1ZWTW9BQVAB?hl=es-419&gl=US&ceid=US%3Aes-419"
    elif language == 'it':
        url = "https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtbDBHZ0pKVkNnQVAB?hl=it&gl=IT&ceid=IT%3Ait"
    elif language == 'fr':
        url = "https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtWnlHZ0pHVWlnQVAB?hl=fr&gl=FR&ceid=FR%3Afr"
    elif language == 'de':
        url = "https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtUmxHZ0pFUlNnQVAB?hl=de&gl=DE&ceid=DE%3Ade"
    elif language == 'ro':
        url = "https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FuSnZHZ0pTVHlnQVAB?hl=ro&gl=RO&ceid=RO%3Aro"
    else:
        return "Language not supported."
    listNews = []
    try:
        NewsFeed = feedparser.parse(url)
        for d in NewsFeed.entries:
            title = d['title']
            title = strip_html_tags(title)
            listNews.append(title)
    except:
        print("Erro em ", url)

    if num != None:
        listNews = listNews[:num]
    outputText = ["News:\n"]
    for n in listNews:
        outputText.append(n)
        outputText.append("\n")
    return(' '.join(outputText))


def emmNewsBrief(language, num=None):
    """
        Return the news' title from emm.newsbrief.eu using RSS feeds.

        Parameters
        ----------
        language : str
            Language of the news.
            example: 'en', 'pt', 'es', 'fr', 'de', 'ro', 'ca', 'it', 'nl'

        num : integer
            Maximum number of news to be returned.

        Returns
        -------
        str
            String with the titles of the news.
        """
    if language in ['pt', 'en', 'es', 'it', 'fr', 'de', 'ro', 'ca', 'nl', 'cs', 'da', 'ru', 'sv']:
        url = "https://emm.newsbrief.eu/rss/rss?type=rtn&language=%s&duplicates=false" % language
    else:
        return "Language not supported."
    listNews = []
    try:
        NewsFeed = feedparser.parse(url)
        for d in NewsFeed.entries:
            title = d['title']
            title = strip_html_tags(title)
            listNews.append(title)
    except:
        print("Erro em ", url)

    if num != None:
        listNews = listNews[:num]
    outputText = ["News:\n"]
    for n in listNews:
        outputText.append(n)
        outputText.append("\n")
    return(' '.join(outputText))
