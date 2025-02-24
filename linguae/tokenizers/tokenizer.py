"""
Module to tokenize sentences.
"""

from transformers import AutoTokenizer

tokenizer_ = AutoTokenizer.from_pretrained("google-bert/bert-base-multilingual-cased")

def tokenize(text, tokenizer=tokenizer_):
    """
    Tokenize the text using the given tokenizer
    """
    return tokenizer.tokenize(text)

def tokenizerEncode(text, tokenizer=tokenizer_):
    """
    Encode the text using the tokenizer and return the token's id
    """
    return tokenizer.encode(text)

def tokenizerDecode(tokenId, tokenizer=tokenizer_):
    """
    Decode the token's id using the tokenizer and return the text
    """
    return tokenizer.decode(tokenId)