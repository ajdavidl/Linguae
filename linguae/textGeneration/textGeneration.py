from transformers import pipeline

def loadBloom():
    """
        Load Bloom Language model

        It uses the pipeline from transformers package.

        Parameters
        ----------
        No parameters

        Returns
        -------
        a Pipeline object from the transformers package with the Bloom model loaded
            
        """
    return pipeline("text-generation", model="bigscience/bloom-1b1")

def loadmGPT():
    """
        Load mGPT Language model

        It uses the pipeline from transformers package.

        Parameters
        ----------
        No parameters

        Returns
        -------
        a Pipeline object from the transformers package with the mGPT model loaded
            
        """
    return pipeline("text-generation", model="sberbank-ai/mGPT")

def generateText(modelPipeline, textSeed, textSize=80, numberSentences=1):
    """
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
        """
    result = modelPipeline(textSeed, max_length=textSize,
                                    num_return_sequences=numberSentences)
    textOutput = []
    for i in range(len(result)):
        textOutput.append(str(i+1)+":\n")
        textOutput.append(result[0]['generated_text'])
        textOutput.append("\n")
    return ' '.join(textOutput)