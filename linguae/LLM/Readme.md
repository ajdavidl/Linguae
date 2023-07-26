# LLM module

Module with functions for open source large language models.

It uses the [langchain](https://github.com/langchain-ai/langchain) and the [gpt4all](https://github.com/nomic-ai/gpt4all) packages.

The models are available in the gpt4all's [site](https://gpt4all.io/index.html).

Functions:

```
linguae.llmChat : Create a chat with the large language model.
```

- llmChat:

```python
>>> import linguae
>>> linguae.llmChat('en',"wizardlm-13b-v1.1-superhot-8k.ggmlv3.q4_0.bin")
```