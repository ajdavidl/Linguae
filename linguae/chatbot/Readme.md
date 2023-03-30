# Module Chatbot

Module to practice language with a chatbot.

It uses the [ChatterBot](https://github.com/gunthercox/ChatterBot) package under the hood.

The main function is `chatbot` that opens a command line interface chat with the Linguae package.

Examples: 

```python
>>> import linguae
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
```

There is also the function `dialoGPT` that uses a pre-trained model called [**dialoGPT**](https://huggingface.co/microsoft/DialoGPT-medium) to create a chatbot. This function has only two languages available: English and Spanish.

Example:

```python
>>> linguae.dialoGPT("en")
>> User: Hi
DialoGPT: Hi!
>> User:

>>> linguae.dialoGPT("es")
>> User: Hola
DialoGPT: hola
>> User: 

```
