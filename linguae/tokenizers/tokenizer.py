"""
Module to tokenize sentences.
"""

from transformers import AutoTokenizer
import importlib.resources
import pathlib

data_path = importlib.resources.files('linguae') / 'tokenizers' / 'linguae_tokenizer'

def returnTokenizer(name = "custom"):
    """ 
    Return tokenizer.

    Parameters:
    -----------
    name : str
        name of the tokenizer.
        Examples: 'bert', 'gpt2', 'custom'

    Returns
    -------
    Autotokenizer : PreTrainedTokenizerFast from transformers packages.

    Examples
    --------
    >>> tokenizer_ = linguae.returnTokenizer()
    >>> tokenizer_bert = linguae.returnTokenizer("bert")
    >>> tokenizer_gpt2 = linguae.returnTokenizer("gpt2")
    """ 
    if name.lower() == 'bert':
        return AutoTokenizer.from_pretrained("google-bert/bert-base-multilingual-cased")
    elif name.lower() == 'gpt2':
        return AutoTokenizer.from_pretrained("gpt2")
    elif name.lower() == "custom":
        return AutoTokenizer.from_pretrained(data_path)

def tokenize(text, tokenizer):
    """
    Tokenize the text using the given tokenizer.

    Parameters:
    -----------
    text : str
        The text to be tokenized.

    tokenizer : PreTrainedTokenizerFast from transformers packages
        Tokenizer loaded from return_tokenizer function or from AutoTokenizer.from_pretained function.

    Examples
    --------
    >>> tokenizer_ = linguae.returnTokenizer()
    >>> linguae.tokenize("Linguae is a python package", tokenizer_)
    """
    return tokenizer.tokenize(text)

def tokenizerEncode(text, tokenizer):
    """
    Encode the text using the tokenizer and return the token's id.

    Parameters:
    -----------
    text : str
        The text to be tokenized.

    tokenizer : PreTrainedTokenizerFast from transformers packages
        Tokenizer loaded from return_tokenizer function or from AutoTokenizer.from_pretained function.

    Examples
    --------
    >>> tokenizer_ = linguae.returnTokenizer()
    >>> linguae.tokenizerEncode("Linguae is a python package", tokenizer_)
    """
    return tokenizer.encode(text)

def tokenizerDecode(tokenId, tokenizer):
    """
    Decode the token's id using the tokenizer and return the text.

    Parameters:
    -----------
    text : str
        The text to be tokenized.

    tokenizer : PreTrainedTokenizerFast from transformers packages
        Tokenizer loaded from return_tokenizer function or from AutoTokenizer.from_pretained function.

    Examples
    --------
    >>> tokenizer_ = linguae.returnTokenizer()
    >>> linguae.tokenizerDecode([28513, 11496, 307, 259, 32474, 1846, 266, 16815, 14], tokenizer_)
    """
    return tokenizer.decode(tokenId)