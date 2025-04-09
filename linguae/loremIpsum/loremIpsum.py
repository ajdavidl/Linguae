"""
Generates Lorem Ipsum text.
"""

import random

from ..wordLists.wordLists import wordList

def generateLoremIpsum(language = None, num_words = 10, num_sentences = None, start_with_sentence=False):
    """
    Generates Lorem Ipsum text.

    Parameters
    ----------
    language : str 
        the language of the text

    num_words : int (optional) 
        The number of words to generate. Defaults to 10.
        
    num_sentences : int (optional) 
        The number of sentences to generate.  If provided, `num_words` is ignored. Defaults to None.
    
    start_with_sentence : bool (optional)
        Whether to start the generated text with a sentence. Defaults to False.

    Returns
    -------
        str: The generated Lorem Ipsum text.
    
    Examples
    --------
    >>> print("10 words:")
    >>> print(generate_lorem_ipsum())
    >>> print("\n2 sentences:")
    >>> print(generate_lorem_ipsum(num_sentences=2))
    >>> print("\n15 words, starting with a sentence:")
    >>> print(generate_lorem_ipsum(num_words=15, start_with_sentence=True))
    >>> print("\n5 sentences:")
    >>> print(generate_lorem_ipsum(num_sentences=5))
    """
    if language is None:
        words = [
            "lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit",
            "sed", "do", "eiusmod", "tempor", "incididunt", "ut", "labore", "et", "dolore",
            "magna", "aliqua", "ut", "enim", "ad", "minim", "veniam", "quis", "nostrud",
            "exercitation", "ullamco", "laboris", "nisi", "ut", "aliquip", "ex", "ea",
            "commodo", "consequat", "duis", "aute", "irure", "dolor", "in", "reprehenderit",
            "in", "voluptate", "velit", "esse", "cillum", "dolore", "eu", "fugiat", "nulla",
            "pariatur", "excepteur", "sint", "occaecat", "cupidatat", "non", "proident",
            "sunt", "in", "culpa", "qui", "officia", "deserunt", "molit", "anim", "id",
            "est", "laborum"
        ]
    elif language in ['por', 'eng', 'ita', 'fre', 'spa', 'deu', 'nld']:
        words = wordList(language=language)
    else:
        print("Language not supported!")
        return

    if num_sentences is not None:
        text = ""
        for _ in range(num_sentences):
            sentence_length = random.randint(5, 15)  # Vary sentence length
            sentence = " ".join(random.choice(words) for _ in range(sentence_length)).capitalize() + "."
            text += sentence + " "
        return text.strip()  # Remove trailing space

    else:
        text = " ".join(random.choice(words) for _ in range(num_words))
        if start_with_sentence:
            sentence_length = random.randint(5, 15)
            sentence = " ".join(random.choice(words) for _ in range(sentence_length)).capitalize() + "."
            text = sentence + " " + text
        return text

