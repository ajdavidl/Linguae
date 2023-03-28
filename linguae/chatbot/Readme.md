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
