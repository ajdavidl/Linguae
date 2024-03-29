"""
Module with functions for open source large language models
"""
from langchain.memory import ConversationBufferMemory
from langchain.llms import GPT4All
from langchain.chains import ConversationChain
from langchain.prompts.prompt import PromptTemplate
from langchain import LLMChain


def loadLLM(model_path):
    """
    Load a large language model.

    It uses the langchain and the gpt4all packages.

    Parameters
    ----------
    model_path : str
        The path of the large language model. 

    Returns
    -------
    <class 'langchain.llms.gpt4all.GPT4All'>

    See Also
    --------
    linguae.llmChat : Create a chat with the large language model.
    linguae.llmDefinitions : Print the definition of the word according the language model in the language asked.
    linguae.llmStory : Print a short story written by the language model about the specified topic and in the language asked.
    linguae.llmTeacher : Create a chat with the large language model playing a role like a language teacher.

    Examples
    --------
    >>> llmWizardlm = linguae.loadLLM("wizardlm-13b-v1.1-superhot-8k.ggmlv3.q4_0.bin")
    >>> llmStableVicuna = linguae.loadLLM("ggml-stable-vicuna-13B.q4_2.bin")
    >>> llmMPT = linguae.loadLLM("ggml-mpt-7b-instruct.bin")
    """
    return GPT4All(model=model_path,
                   n_threads=8, echo=False,
                   temp=0.5, top_p=0.95, top_k=40,
                   repeat_penalty=1.3, n_predict=2048)


def llmChat(language, model):
    """
    Create a chat with the large language model.

    It uses the langchain and the gpt4all packages.

    It uses the models available in the gpt4all site.

    The function opens a chat with the language model in the python terminal. Type "QUIT" to end the conversation.

    Parameters
    ----------
    language : str
        Language to be loaded.
        examples: 'en', 'pt', 'es', 'fr', 'it, 'de'

    model : str or <class 'langchain.llms.gpt4all.GPT4All'>
        You can pass the string with the path of the large language model.
        Or you can pass the model loaded by the function linguae.loadLLM.

    See Also
    --------
    linguae.loadLLM : Load a large language model.
    linguae.llmDefinitions : Print the definition of the word according the language model in the language asked.
    linguae.llmStory : Print a short story written by the language model about the specified topic and in the language asked.
    linguae.llmTeacher : Create a chat with the large language model playing a role like a language teacher.

    Examples
    --------
    >>> linguae.llmChat('en',"ggml-gpt4all-l13b-snoozy.bin")
    >>> linguae.llmChat('pt',"wizardlm-13b-v1.1-superhot-8k.ggmlv3.q4_0.bin")
    or
    >>> llm = linguae.loadLLM('wizardLM-13B-Uncensored.ggmlv3.q4_0.bin')
    >>> linguae.llmChat('es',llm)

    """
    if language == 'en':
        template_ = """
# Instruction:
            The prompt below is a question to answer, a task to complete, or a conversation
            to respond to; decide which and write an appropriate response.

# Prompt:
Current conversation:
{history}

Human: {input}
# Response:
AI:
"""
    elif language == 'pt':
        template_ = """
# Instruction:
            O prompt abaixo é uma pergunta a ser respondida, uma tarefa a ser concluída ou uma conversa
            para responder; decida qual e escreva uma resposta apropriada.
            Responda em português.

# Prompt:
Conversa atual:
{history}

Human: {input}
# Response:
AI:
"""
    elif language == 'es':
        template_ = """
# Instruction:
            El siguiente mensaje es una pregunta que debe responderse, una tarea que debe completarse o una conversación
            para responder; decide cuál y escribe una respuesta apropiada.
            Responde en español.

# Prompt:
Conversación actual:
{history}

Human: {input}
# Response:
AI:
"""
    elif language == 'it':
        template_ = """
# Instruction:
            Il prompt di seguito è una domanda a cui rispondere, un'attività da completare o una conversazione a cui rispondere;
            decidere quale e scrivere una risposta appropriata. Rispondi in italiano.

# Prompt:
Conversazione in corso:
{history}

Human: {input}
# Response:
AI:
"""
    elif language == 'fr':
        template_ = """
# Instruction:
            L'invite ci-dessous est une question à laquelle répondre, une tâche à accomplir ou une conversation à laquelle répondre;
            décidez lequel et écrivez une réponse appropriée. Réponse en français.

# Prompt:
Conversation en cours:
{history}

Human: {input}
# Response:
AI:
"""
    elif language == 'de':
        template_ = """
# Instruction:
            Bei der folgenden Eingabeaufforderung handelt es sich um eine zu beantwortende Frage, eine zu erledigende Aufgabe oder ein Gespräch
            Antworten auf; Entscheiden Sie sich für welche und schreiben Sie eine entsprechende Antwort. Antwort auf Deutsch.

# Prompt:
Aktuelles Gespräch:
{history}

Human: {input}
# Response:
AI:
"""
    else:
        print("Language not supported!")
        return

    PROMPT = PromptTemplate(
        input_variables=["history", "input"], template=template_)

    if type(model) == str:
        llm = GPT4All(model=model,
                      n_threads=8, echo=False,
                      temp=0.5, top_p=0.95, top_k=40,
                      repeat_penalty=1.3, n_predict=2048)
    else:
        llm = model

    conversation = ConversationChain(
        prompt=PROMPT,
        llm=llm, verbose=False, memory=ConversationBufferMemory())

    print()
    txt_input = input("Human: ")
    while txt_input != "QUIT":
        print("\nAi:", end=" ")
        txt_out = conversation.predict(input=txt_input)
        print(txt_out)
        print()
        txt_input = input("Human: ")


def llmDefinitions(language, word, model):
    """
    Print the definition of the word according the language model in the language asked.

    It uses the langchain and gpt4all package.

    Parameters
    ----------
    language : str
        Language to be used in the answer. Not always the LLM will respect this. Sometimes it answers in English. 
        examples: 'English', 'Portuguese', 'Spanish', 'French', 'Italian, 'German'

    word : str
        The word that will be defined by the language model. It can be an expression.

    model : str or <class 'langchain.llms.gpt4all.GPT4All'>
        You can pass the string with the path of the large language model.
        Or you can pass the model loaded by the function linguae.loadLLM.

    See Also
    --------
    linguae.loadLLM : Load a large language model.
    linguae.llmChat : Create a chat with the large language model.
    linguae.llmStory : Print a short story written by the language model about the specified topic and in the language asked.
    linguae.llmTeacher : Create a chat with the large language model playing a role like a language teacher.

    Examples
    --------
    >>> linguae.llmDefinitions('English','language','wizardlm-13b-v1.1-superhot-8k.ggmlv3.q4_0.bin')
    >>> linguae.llmDefinitions('Portuguese','aprender','wizardlm-13b-v1.1-superhot-8k.ggmlv3.q4_0.bin')
    or
    >>> llm = linguae.loadLLM('wizardLM-13B-Uncensored.ggmlv3.q4_0.bin')
    >>> linguae.llmDefinitions('French', 'parole', llm)
    """
    templateDefinition = """
### Instruction: 
Give the definition of the word {word} in {language} language. Answer in the {language} language.

### Response:
"""
    promptDefinition = PromptTemplate(template=templateDefinition, input_variables=[
        "word", "language"])

    if type(model) == str:
        llm = GPT4All(model=model,
                      n_threads=8,
                      temp=0.5, top_p=0.95, top_k=40,
                      repeat_penalty=1.3, n_predict=2048)
    else:
        llm = model

    llm_definition = LLMChain(prompt=promptDefinition, llm=llm)
    print("\n", word, " - ", language, ":")
    txt = llm_definition.run({"word": word, "language": language})
    print(txt, "\n")
    return


def llmStory(language, topic, model):
    """
    Print a short story written by the language model about the specified topic and in the language asked.

    It uses the langchain and gpt4all package.

    Parameters
    ----------
    language : str
        Language to be used in the answer. Not always the LLM will respect this. Sometimes it answers in English. 
        examples: 'English', 'Portuguese', 'Spanish', 'French', 'Italian, 'German'

    topic : str
        The topic of the story that will be written by the language model. 

    model : str or <class 'langchain.llms.gpt4all.GPT4All'>
        You can pass the string with the path of the large language model.
        Or you can pass the model loaded by the function linguae.loadLLM.

    See Also
    --------
    linguae.loadLLM : Load a large language model.
    linguae.llmChat : Create a chat with the large language model.
    linguae.llmDefinitions : Print the definition of the word according the language model in the language asked.
    linguae.llmTeacher : Create a chat with the large language model playing a role like a language teacher.

    Examples
    --------
    >>> linguae.llmStory('English','the colonization of Mars by Human kind.','wizardlm-13b-v1.1-superhot-8k.ggmlv3.q4_0.bin')
    >>> linguae.llmStory('Portuguese',"the exploration of the Saturn's moons.",'wizardlm-13b-v1.1-superhot-8k.ggmlv3.q4_0.bin')
    or
    >>> llm = linguae.loadLLM('wizardLM-13B-Uncensored.ggmlv3.q4_0.bin')
    >>> linguae.llmStory('French', 'the discover of an ancient language in a cave of the Moon', llm)
    """
    if type(model) == str:
        llm = GPT4All(model=model,
                      n_threads=8,
                      temp=0.5, top_p=0.95, top_k=40,
                      repeat_penalty=1.3, n_predict=2048)
    else:
        llm = model

    if "vicuna" in llm.model:
        templateStory = """\
### Human: Craft a short story or poem prompt in {language} language about {topic}.
### Assistant:\
"""
    else:
        templateStory = """
### Instruction: 
The prompt below is a task to complete; decide which and write an appropriate response.

### Prompt:
Craft a short story about the following topic: {topic}.
Write the story in {language} language.

### Response:
"""
    promptStory = PromptTemplate(
        template=templateStory, input_variables=["language", "topic"])
    llm_story = LLMChain(prompt=promptStory, llm=llm)
    txt = llm_story.run({"topic": topic, "language": language})
    print(txt, "\n")
    return


def llmTeacher(language, model):
    """
    Create a chat with the large language model playing a role like a language teacher.

    It uses the langchain and the gpt4all packages.

    It uses the models available in the gpt4all site.

    The function opens a chat with the language model in the python terminal. Type "QUIT" to end the conversation.

    Parameters
    ----------
    language : str
        Language to be loaded.
        examples: 'English', 'Portuguese', 'Spanish', 'French', 'Italian, 'German'

    model : str or <class 'langchain.llms.gpt4all.GPT4All'>
        You can pass the string with the path of the large language model.
        Or you can pass the model loaded by the function linguae.loadLLM.

    See Also
    --------
    linguae.loadLLM : Load a large language model.
    linguae.llmDefinitions : Print the definition of the word according the language model in the language asked.
    linguae.llmStory : Print a short story written by the language model about the specified topic and in the language asked.
    linguae.llmChat : Create a chat with the large language model.

    Examples
    --------
    >>> linguae.llmTeacher('English',"ggml-gpt4all-l13b-snoozy.bin")
    >>> linguae.llmTeacher('Portuguese',"wizardlm-13b-v1.1-superhot-8k.ggmlv3.q4_0.bin")
    or
    >>> llm = linguae.loadLLM('wizardLM-13B-Uncensored.ggmlv3.q4_0.bin')
    >>> linguae.llmTeacher('Spanish',llm)

    """
    templateTeacher = """
### Instruction: 
I want you to act as a spoken {language} teacher and improver. 
I will speak to you in {language} and you will reply to me in {language} to practice my spoken {language}. 
I want you to keep your reply neat, limiting the reply to 100 words. 
I want you to strictly correct my grammar mistakes, typos, and factual errors. 
I want you to ask me a question in your reply. Now let's start practicing, you could ask me a question first. 
Remember, I want you to strictly correct my grammar mistakes, typos, and factual errors.

# Prompt:
Current conversation:
{history}

Human: {input}
### Response:
"""
    PROMPT = PromptTemplate(partial_variables={"language": language},
                            input_variables=["history", "input"], template=templateTeacher)

    if type(model) == str:
        llm = GPT4All(model=model,
                      n_threads=8, echo=False,
                      temp=0.5, top_p=0.95, top_k=40,
                      repeat_penalty=1.3, n_predict=2048)
    else:
        llm = model

    conversation = ConversationChain(
        prompt=PROMPT,
        llm=llm, verbose=False, memory=ConversationBufferMemory())

    print()
    txt_out = conversation.predict(input=" ")
    print("Ai:", txt_out)
    txt_input = input("Human: ")
    while txt_input != "QUIT":
        print("\nAi:", end=" ")
        txt_out = conversation.predict(input=txt_input)
        print(txt_out)
        print()
        txt_input = input("Human: ")
