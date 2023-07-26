# LLM module

Module with functions for open source large language models.

It uses the [langchain](https://github.com/langchain-ai/langchain) and the [gpt4all](https://github.com/nomic-ai/gpt4all) packages.

The models are available in the gpt4all's [site](https://gpt4all.io/index.html).

Functions:

```
linguae.llmChat : Create a chat with the large language model.
linguae.llmDefinitions : Print the definition of the word according the language model in the language asked.
```

- llmChat:

```python
>>> import linguae
>>> linguae.llmChat('en',"wizardlm-13b-v1.1-superhot-8k.ggmlv3.q4_0.bin")
>>> linguae.llmChat('en',"ggml-gpt4all-l13b-snoozy.bin")
```

- llmDefinitions:

```python
>>> import linguae
>>> linguae.definitions('English','language','wizardlm-13b-v1.1-superhot-8k.ggmlv3.q4_0.bin')
>>> linguae.definitions('Portuguese','aprender','wizardlm-13b-v1.1-superhot-8k.ggmlv3.q4_0.bin')
```
