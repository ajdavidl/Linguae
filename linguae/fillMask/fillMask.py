"""
Module for the task of fill the mask on sentences
"""
import re
from transformers import pipeline
from warnings import warn


def loadBertMultilingual():
    """
    Load multilingual Bert Language model.

    It uses the pipeline from transformers package.

    Parameters
    ----------
    No parameters.

    Returns
    -------
    A Pipeline object from the transformers package with the model loaded.
    <class 'transformers.pipelines.fill_mask.FillMaskPipeline'>

    See Also
    --------
    linguae.loadXLMRoberta : Load XLM-Roberta Language model.
    linguae.loadBertPortuguese : Load Portuguese Bert Language model.
    linguae.loadBertEnglish : Load English Bert Language model.
    linguae.loadBertSpanish : Load Spanish Bert Language model.
    linguae.fillMaskBert : Fill the mask tag on the masked Sentence.

    Examples
    --------
    >>> pipeline = linguae.loadBertMultilingual()
    """
    return pipeline('fill-mask', model='bert-base-multilingual-cased')


def loadXLMRoberta():
    """
    Load XLM-Roberta Language model.

    It uses the pipeline from transformers package.

    Parameters
    ----------
    No parameters.

    Returns
    -------
    A Pipeline object from the transformers package with the model loaded.
    <class 'transformers.pipelines.fill_mask.FillMaskPipeline'>

    See Also
    --------
    linguae.loadBertMultilingual : Load multilingual Bert Language model.
    linguae.loadBertPortuguese : Load Portuguese Bert Language model.
    linguae.loadBertEnglish : Load English Bert Language model.
    linguae.loadBertSpanish : Load Spanish Bert Language model.
    linguae.fillMaskXLMRoberta : Fill the mask tag on the masked Sentence.

    Examples
    --------
    >>> pipeline = linguae.loadXLMRoberta()
    """
    return pipeline('fill-mask', model='xlm-roberta-base')


def fillMaskBert(modelPipeline, maskedSentence):
    """
    Fill the mask tag on the masked Sentence.

    It receives the pipeline with the language model loaded. 

    It uses the transformers pipeline model to fill the mask.

    Parameters
    ----------
    modelPipeline : pipeline from transformers package with the model loaded.

    maskedSentence : str
        The masked sentence to be used by the language model. The masked token is [MASK].

    Returns
    -------
    str
        String with the words that fill the mask and their scores.

    See Also
    --------
    linguae.loadBertMultilingual : Load multilingual Bert Language model.
    linguae.loadBertPortuguese : Load Portuguese Bert Language model.
    linguae.loadBertEnglish : Load English Bert Language model.
    linguae.loadBertSpanish : Load Spanish Bert Language model.

    Examples
    --------
    >>> pipeline = linguae.loadBertMultilingual()
    >>> s1 = linguae.fillMaskBert(pipeline, "Languages are very [MASK] to learn.")
    >>> print(s1)
    Languages are very [MASK] to learn. 
    Languages are very important to learn. - 0.31147173047065735 
    Languages are very difficult to learn. - 0.11882742494344711 
    Languages are very easy to learn. - 0.05582128465175629 
    Languages are very useful to learn. - 0.02000458538532257 
    Languages are very different to learn. - 0.01871359348297119
    >>> s2 = linguae.fillMaskBert(pipeline, "Idiomas são muito [MASK] de aprender.")
    >>> print(s2)
    Idiomas são muito [MASK] de aprender. 
    Idiomas são muito fácil de aprender. - 0.23076950013637543 
    Idiomas são muito difícil de aprender. - 0.14634060859680176 
    Idiomas são muito simples de aprender. - 0.10525200515985489 
    Idiomas são muito muito de aprender. - 0.03582744300365448 
    Idiomas são muito pouco de aprender. - 0.022088903933763504 
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
    Fill the mask tag on the masked Sentence.

    It receives the pipeline with the language model loaded. 

    It uses the transformers pipeline model to fill the mask.

    Parameters
    ----------
    modelPipeline : pipeline from transformers package with the model loaded.

    maskedSentence : str
        The masked sentence to be used by the language model. The masked token is <mask>. 

    Returns
    -------
    str
        String with the words that fill the mask and their scores.

    See Also
    --------
    linguae.loadXLMRoberta : Load XLM-Roberta Language model.

    Examples
    --------
    >>> pipeline = linguae.loadXLMRoberta()
    >>> s1 = linguae.fillMaskXLMRoberta(pipeline, "Languages are very <mask> to learn.")
    >>> print(s1)
    Languages are very <mask> to learn. 
    Languages are very easy to learn. - 0.4749657213687897 
    Languages are very difficult to learn. - 0.28722426295280457 
    Languages are very hard to learn. - 0.0973852351307869 
    Languages are very simple to learn. - 0.0434383861720562 
    Languages are very important to learn. - 0.023733003064990044
    >>> s2 = linguae.fillMaskXLMRoberta(pipeline, "Idiomas são muito <mask> de aprender.")
    >>> print(s2)
    Idiomas são muito <mask> de aprender. 
    Idiomas são muito importantes de aprender. - 0.32905060052871704 
    Idiomas são muito simples de aprender. - 0.30486467480659485 
    Idiomas são muito difíceis de aprender. - 0.25990456342697144 
    Idiomas são muito fácil de aprender. - 0.028021013364195824 
    Idiomas são muito difícil de aprender. - 0.01971607282757759
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


def loadBertPortuguese():
    """
    Load Portuguese Bert Language model.

    It uses the pipeline from transformers package.

    Parameters
    ----------
    No parameters.

    Returns
    -------
    A Pipeline object from the transformers package with the model loaded.
    <class 'transformers.pipelines.fill_mask.FillMaskPipeline'>

    See Also
    --------
    linguae.loadBertMultilingual : Load multilingual Bert Language model.
    linguae.loadBertEnglish : Load English Bert Language model.
    linguae.loadBertSpanish : Load Spanish Bert Language model.
    linguae.fillMaskBert : Fill the mask tag on the masked Sentence.

    Examples
    --------
    >>> pipeline = linguae.loadBertPortuguese()
    """
    warn("This function is deprecated, use linguae.loadBert('pt') instead.",
         DeprecationWarning, stacklevel=2)
    return pipeline('fill-mask', model='neuralmind/bert-base-portuguese-cased')


def loadBertEnglish():
    """
    Load English Bert Language model.

    It uses the pipeline from transformers package.

    Parameters
    ----------
    No parameters.

    Returns
    -------
    A Pipeline object from the transformers package with the model loaded.
    <class 'transformers.pipelines.fill_mask.FillMaskPipeline'>

    See Also
    --------
    linguae.loadBertMultilingual : Load multilingual Bert Language model.
    linguae.loadBertPortuguese : Load Portuguese Bert Language model.
    linguae.loadBertSpanish : Load Spanish Bert Language model.
    linguae.fillMaskBert : Fill the mask tag on the masked Sentence.

    Examples
    --------
    >>> pipeline = linguae.loadBertEnglish()
    """
    warn("This function is deprecated, use linguae.loadBert('en') instead.",
         DeprecationWarning, stacklevel=2)
    return pipeline('fill-mask', model='bert-base-cased')


def loadBertSpanish():
    """
    Load Spanish Bert Language model.

    It uses the pipeline from transformers package.

    Parameters
    ----------
    No parameters.

    Returns
    -------
    A Pipeline object from the transformers package with the model loaded.
    <class 'transformers.pipelines.fill_mask.FillMaskPipeline'>

    See Also
    --------
    linguae.loadBertMultilingual : Load multilingual Bert Language model.
    linguae.loadBertPortuguese : Load Portuguese Bert Language model.
    linguae.loadBertEnglish : Load English Bert Language model.
    linguae.fillMaskBert : Fill the mask tag on the masked Sentence.

    Examples
    --------
    >>> pipeline = linguae.loadBertSpanish()
    """
    warn("This function is deprecated, use linguae.loadBert('es') instead.",
         DeprecationWarning, stacklevel=2)
    return pipeline('fill-mask', model='dccuchile/bert-base-spanish-wwm-cased')


def loadBert(language):
    """
    Load Bert Language model.

    It uses the pipeline from transformers package.

    Parameters
    ----------
    language : str
        Language to be loaded.
        examples: 'en', 'pt', 'es', 'de'


    Returns
    -------
    A Pipeline object from the transformers package with the model loaded.
    <class 'transformers.pipelines.fill_mask.FillMaskPipeline'>

    See Also
    --------
    linguae.loadBertMultilingual : Load multilingual Bert Language model.
    linguae.fillMaskBert : Fill the mask tag on the masked Sentence.

    Examples
    --------
    >>> pipeline = linguae.loadBert('en')

    >>> pipeline = linguae.loadBert('pt')
    """
    if language == 'en':
        return pipeline('fill-mask', model='bert-base-cased')
    elif language == 'pt':
        return pipeline('fill-mask', model='neuralmind/bert-base-portuguese-cased')
    elif language == 'es':
        return pipeline('fill-mask', model='dccuchile/bert-base-spanish-wwm-cased')
    elif language == 'de':
        return pipeline('fill-mask', model='bert-base-german-cased')
    else:
        raise Exception("Language "+language +
                        " not available in linguae.loadBert function.")
        return None
