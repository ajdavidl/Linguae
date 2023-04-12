"""
Module to generate text using language models.
"""
from transformers import pipeline
from warnings import warn


def loadBloom():
    """
    Load Bloom Language model.

    It uses the pipeline from transformers package.

    Parameters
    ----------
    No parameters.

    Returns
    -------
    a Pipeline object from the transformers package with the Bloom model loaded.

    See Also
    --------
    loadmGPT : Load mGPT Language model.
    loadGPTPortuguese : Load Portuguese GPT2 Language model.
    loadGPTEnglish : Load English GPT2 Language model.
    loadGPTSpanish : Load Spanish GPT2 Language model. 
    generateText : Generate text using a language model.

    Examples
    --------
    >>> pipelineBloom = linguae.loadBloom()
    """
    return pipeline("text-generation", model="bigscience/bloom-1b1")


def loadmGPT():
    """
    Load multilingual GPT Language model.

    It uses the pipeline from transformers package.

    Parameters
    ----------
    No parameters.

    Returns
    -------
    a Pipeline object from the transformers package with the mGPT model loaded.

    See Also
    --------
    loadBloom : Load Bloom Language model.
    loadGPTPortuguese : Load Portuguese GPT2 Language model.
    loadGPTEnglish : Load English GPT2 Language model.
    loadGPTSpanish : Load Spanish GPT2 Language model. 
    generateText : Generate text using a language model.

    Examples
    --------
    >>> pipelinemGPT = linguae.loadmGPT()
    """
    return pipeline("text-generation", model="sberbank-ai/mGPT")


def loadGPTPortuguese():
    """
    Load Portuguese GPT2 Language model.

    It uses the pipeline from transformers package.

    Parameters
    ----------
    No parameters.

    Returns
    -------
    a Pipeline object from the transformers package with the Portuguese GPT model loaded.

    See Also
    --------
    loadBloom : Load Bloom Language model.
    loadmGPT : Load mGPT Language model.
    loadGPTEnglish : Load English GPT2 Language model.
    loadGPTSpanish : Load Spanish GPT2 Language model. 
    generateText : Generate text using a language model.

    Examples
    --------
    >>> pipelineGPTPor = linguae.loadGPTPortuguese()
    """
    warn("This function is deprecated, use linguae.loadGPT('pt') instead.",
         DeprecationWarning, stacklevel=2)
    return pipeline("text-generation", model="pierreguillou/gpt2-small-portuguese")


def loadGPTEnglish():
    """
    Load English GPT2 Language model.

    It uses the pipeline from transformers package.

    Parameters
    ----------
    No parameters.

    Returns
    -------
    a Pipeline object from the transformers package with the Portuguese GPT model loaded.

    See Also
    --------
    loadBloom : Load Bloom Language model.
    loadmGPT : Load mGPT Language model.
    loadGPTPortuguese : Load Portuguese GPT2 Language model.
    loadGPTSpanish : Load Spanish GPT2 Language model. 
    generateText : Generate text using a language model.

    Examples
    --------
    >>> pipelineGPTEng = linguae.loadGPTEnglish()
    """
    warn("This function is deprecated, use linguae.loadGPT('en') instead.",
         DeprecationWarning, stacklevel=2)
    return pipeline("text-generation", model="gpt2-medium")


def loadGPTSpanish():
    """
    Load Spanish GPT2 Language model.

    It uses the pipeline from transformers package.

    Parameters
    ----------
    No parameters.

    Returns
    -------
    a Pipeline object from the transformers package with the Portuguese GPT model loaded.

    See Also
    --------
    loadBloom : Load Bloom Language model.
    loadmGPT : Load mGPT Language model.
    loadGPTPortuguese : Load Portuguese GPT2 Language model.
    loadGPTEnglish : Load English GPT2 Language model.
    generateText : Generate text using a language model.

    Examples
    --------
    >>> pipelineGPTSpa = linguae.loadGPTSpanish()
    """
    warn("This function is deprecated, use linguae.loadGPT('es') instead.",
         DeprecationWarning, stacklevel=2)
    return pipeline("text-generation", model="datificate/gpt2-small-spanish")


def loadGPT(language):
    """
    Load GPT2 Language model.

    It uses the pipeline from transformers package.

    Parameters
    ----------
    language : str
        Language to be loaded.
        examples: 'en', 'pt', 'es', 'de'

    See Also
    --------
    loadBloom : Load Bloom Language model.
    loadmGPT : Load mGPT Language model.
    generateText : Generate text using a language model.

    Examples
    --------
    >>> pipeline = linguae.loadGPT('en')

    >>> pipeline = linguae.loadGPT('pt')
    """
    if language == 'en':
        return pipeline("text-generation", model="gpt2-medium")
    elif language == 'pt':
        return pipeline("text-generation", model="pierreguillou/gpt2-small-portuguese")
    elif language == 'es':
        return pipeline("text-generation", model="datificate/gpt2-small-spanish")
    elif language == 'de':
        return pipeline("text-generation", model="dbmdz/german-gpt2")
    else:
        raise Exception("Language "+language +
                        " not available in linguae.loadGPT function.")
        return None


def generateText(modelPipeline, textSeed, textSize=80, numberSentences=1):
    """
    Generate text using a language model.

    It receives the pipeline with the language model loaded; 
    It gives the text received as seed; 
    and generate the next words.

    It uses the transformers pipeline model to generate text.

    Parameters
    ----------
    modelPipeline : pipeline from transformers package with the model loaded.

    textSeed : str
        The text to be used by the language model as a seed.

    textSize : integer
        The number of words to be generated.

    numberSentences : integer
        number of sentences to be generated.

    Returns
    -------
    str
        String with the seed text and all text generated.

    See Also
    --------
    loadBloom : Load Bloom Language model.
    loadmGPT : Load mGPT Language model.
    loadGPTPortuguese : Load Portuguese GPT2 Language model.
    loadGPTEnglish : Load English GPT2 Language model.
    loadGPTSpanish : Load Spanish GPT2 Language model. 

    Examples
    --------
    >>> pipelineGPTEng = linguae.loadGPT('en')
    >>> linguae.generateText(pipelineGPTEng, "Learning languages is very important to ")

    >>> pipelineBloom = linguae.loadBloom()
    >>> linguae.generateText(pipelineBloom, "Learning languages is very important to ")
    """
    result = modelPipeline(textSeed, max_length=textSize, temperature=0.8, top_p=0.92,
                           repetition_penalty=2.0, num_return_sequences=numberSentences)
    textOutput = []
    for i in range(len(result)):
        textOutput.append(str(i+1)+":\n")
        textOutput.append(result[i]['generated_text'])
        textOutput.append("\n")
    return ' '.join(textOutput)
