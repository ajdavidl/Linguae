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

from .. import data
import re


def __get_feedback():

    text = input()

    if 'yes' in text.lower():
        return True
    elif 'no' in text.lower():
        return False
    else:
        print('Please type either "Yes" or "No"')
        return get_feedback()


def chatbot(language='en', train=True, feedback=False, readOnly=False):

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
