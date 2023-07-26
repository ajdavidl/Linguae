"""
Module with functions for open source large language models
"""
from langchain.memory import ConversationBufferMemory
from langchain.llms import GPT4All
from langchain.chains import ConversationChain
from langchain.prompts.prompt import PromptTemplate

templateENG = """
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

templatePOR = """
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

templateSPA = """
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

templateITA = """
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

templateFRE = """
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

templateDEU = """
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


def llmChat(language, model_path):
    """
    Create a chat with the language model.

    It uses the langchain and the gpt4all packages.

    It uses the models available in the gpt4all site.

    The function opens a chat with the language model in the python terminal. Type "QUIT" to end the conversation.

    Parameters
    ----------
    language : str
        Language to be loaded.
        examples: 'en', 'pt', 'es', 'fr', 'it, 'de'

    model_path : str
        The path of the large language model. 


    Examples
    --------
    >>> linguae.llmChat('en',"ggml-gpt4all-l13b-snoozy.bin")
    >>> linguae.llmChat('pt',"wizardlm-13b-v1.1-superhot-8k.ggmlv3.q4_0.bin")
    """
    if language == 'en':
        template_ = templateENG
    elif language == 'pt':
        template_ = templatePOR
    elif language == 'es':
        template_ = templateSPA
    elif language == 'it':
        template_ = templateITA
    elif language == 'fr':
        template_ = templateFRE
    elif language == 'de':
        template_ = templateDEU
    else:
        print("Language not supported!")
        return

    PROMPT = PromptTemplate(
        input_variables=["history", "input"], template=template_)

    memory = ConversationBufferMemory(memory_key="chat_history")

    llm = GPT4All(model=model_path,
                  n_threads=8, echo=False,
                  temp=0.5, top_p=0.95, top_k=40,
                  repeat_penalty=1.3, n_predict=2048)

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
