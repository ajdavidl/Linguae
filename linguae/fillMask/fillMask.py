"""
Module for the task of fill the mask on sentences
"""
import re
from transformers import pipeline


def loadBertMultilingual():
    """
        Load Bert multilingual Language model

        It uses the pipeline from transformers package.

        Parameters
        ----------
        No parameters

        Returns
        -------
        a Pipeline object from the transformers package with the model loaded

        """
    return pipeline('fill-mask', model='bert-base-multilingual-cased')


def loadXLMRoberta():
    """
        Load XLM-Roberta Language model

        It uses the pipeline from transformers package.

        Parameters
        ----------
        No parameters

        Returns
        -------
        a Pipeline object from the transformers package with the model loaded

        """
    return pipeline('fill-mask', model='xlm-roberta-base')


def fillMaskmBert(modelPipeline, maskedSentence):
    """
        It receives the pipeline with the language model loaded; 
        Fill the mask tag on the masked Sentence

        It uses the transformers pipeline model to fill the mask.

        Parameters
        ----------
        modelPipeline : pipeline from transformers package with the model loaded.

        maskedSentence : str
            The masked sentence to be used by the language model.

        Returns
        -------
        str
            String with the words that fill the mask and their scores.
        """
    if "[MASK]" not in maskedSentence:
        return("Token [MASK] not found.")
    solutions = modelPipeline(maskedSentence)
    outputText = [maskedSentence]
    outputText.append("\n")
    for dic in solutions:
        outputText.append(dic["sequence"] + " - " +
                          str((dic["score"]*100 % 100)/100))
        outputText.append("\n")
    return(' '.join(outputText))


def fillMaskXLMRoberta(modelPipeline, maskedSentence):
    """
        It receives the pipeline with the language model loaded; 
        Fill the mask tag on the masked Sentence

        It uses the transformers pipeline model to fill the mask.

        Parameters
        ----------
        modelPipeline : pipeline from transformers package with the model loaded.

        maskedSentence : str
            The masked sentence to be used by the language model.

        Returns
        -------
        str
            String with the words that fill the mask and their scores.
        """
    if "<mask>" not in maskedSentence:
        return("Token <mask> not found.")
    solutions = modelPipeline(maskedSentence)
    outputText = [maskedSentence]
    outputText.append("\n")
    for dic in solutions:
        outputText.append(dic["sequence"] + " - " +
                          str((dic["score"]*100 % 100)/100))
        outputText.append("\n")
    return(' '.join(outputText))
