"""
Module to practice language with a chatbot.
"""

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.conversation import Statement
try:
    import importlib.resources as pkg_resources
except ImportError:
    import importlib_resources as pkg_resources

from ..data import chatterbotFiles
import re
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch


def __get_feedback():
    """
    Auxiliary funtion to get the user's feedback about the chatbot answers.
    """
    text = input()

    if 'yes' in text.lower():
        return True
    elif 'no' in text.lower():
        return False
    else:
        print('Please type either "Yes" or "No"')
        return __get_feedback()


def chatbot(language='en', train=True, feedback=False, readOnly=False):
    """
    Open a command line chatbot.

    It uses the chatterbot package under the hood.

    Press ctrl+c or ctrl+d to exit the function.

    Parameters
    ----------
    language : str
        Language of the chatbot.
        example: 'en', 'pt', 'es', 'fr', 'de'
    train : bool (default=True)
        If True, the chatbot trains with the available data.
        If False, the chatbot doesn't train.
    feedback : bool (defaul=False)
        If True, the chatbot ask you if the answer is coherent.
        If False, it doesn't get the feedback.
    readOnly : bool (default=False)
        If True, it doesn't save the user's answers.
        If False, it saves the user's answer in a database for future use.

    Examples
    --------
    >>> linguae.chatbot("en")
    List Trainer: [####################] 100%
    Type something to begin...
    You: Hi
    Linguae:  Hi
    You: 

    >>> linguae.chatbot("pt")
    List Trainer: [####################] 100%
    Type something to begin...
    You: Olá
    Linguae:  Oi
    You: 

    >>> linguae.chatbot("es")
    List Trainer: [####################] 100%
    Type something to begin...
    You: Hola
    Linguae:  Hola
    You: 
    """
    bot = ChatBot(
        'Linguae',
        read_only=readOnly,
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        preprocessors=['chatterbot.preprocessors.clean_whitespace'],
        logic_adapters=['chatterbot.logic.BestMatch'],
        database_uri='sqlite:///chatbot_%s.db' % language
    )

    if train:
        trainer = ListTrainer(bot)
        ymlFile = '%s-chatterbot.txt' % language
        template = pkg_resources.open_text(data, ymlFile)
        chat = template.readlines()
        chat = [re.sub("\n", "", line) for line in chat]
        trainer.train(chat)

    print('Type something to begin...')
    while True:
        if feedback:
            try:
                input_statement = Statement(text=input("You: "))
                response = bot.generate_response(input_statement)

                print('\n Is "{}" this a coherent response to "{}"? \n'.format(
                    response.text, input_statement.text))

                if __get_feedback() is False:
                    correct_response = Statement(
                        text=input("input the correct answer: "))
                    bot.learn_response(correct_response, input_statement)
                else:
                    bot.learn_response(response, input_statement)

            # Press ctrl-c or ctrl-d on the keyboard to exit
            except (KeyboardInterrupt, EOFError, SystemExit):
                break
        else:
            try:
                user_input = input("You: ")
                bot_response = bot.get_response(user_input)
                print("Linguae: ", bot_response)
            # Press ctrl-c or ctrl-d on the keyboard to exit
            except (KeyboardInterrupt, EOFError, SystemExit):
                break


def dialoGPT(language, numberOfLines=20):
    """
    Create a chatbot using the DialoGPT-medium model.

    The code of the function was adapted from "https://huggingface.co/microsoft/DialoGPT-medium".

    Parameters
    ----------
    language : str
        Language of the chatbot.
        example: 'en', 'es'
    numberOfLines : integer (default = 20)
        The number of questions/sentences to send to the chatbot.

    Examples
    --------
    >>> linguae.dialoGPT("en")
    >> User: Hi
    DialoGPT: Hi!
    >> User:

    >>> linguae.dialoGPT("es")
    >> User: Hola
    DialoGPT: hola
    >> User: 
    """
    if language == "en":
        model = "microsoft/DialoGPT-medium"
    elif language == "es":
        model = "EZSNoVa/DialogGPT-medium-NoVa"
    else:
        print("Language ", language, " is not available!")
        return
    tokenizer = AutoTokenizer.from_pretrained(model)
    model = AutoModelForCausalLM.from_pretrained(model)
    for step in range(numberOfLines):
        # encode the new user input, add the eos_token and return a tensor in Pytorch
        new_user_input_ids = tokenizer.encode(
            input(">> User: ") + tokenizer.eos_token, return_tensors='pt')
        # append the new user input tokens to the chat history
        bot_input_ids = torch.cat(
            [chat_history_ids, new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids
        # generated a response while limiting the total chat history to 1000 tokens,
        chat_history_ids = model.generate(
            bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
        # pretty print last ouput tokens from bot
        print("DialoGPT: {}".format(tokenizer.decode(
            chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)))
