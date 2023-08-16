# LLM module

Module with functions for open source large language models.

It uses the [langchain](https://github.com/langchain-ai/langchain) and the [gpt4all](https://github.com/nomic-ai/gpt4all) packages.

The models are available in the gpt4all's [site](https://gpt4all.io/index.html).

In order to use this module you are going to need to download the models available in the gpt4all site. Some links are listed below:
- [wizardlm-13b-v1.1-superhot-8k](https://gpt4all.io/models/wizardlm-13b-v1.1-superhot-8k.ggmlv3.q4_0.bin)
- [ggml-model-gpt4all-falcon](https://huggingface.co/nomic-ai/gpt4all-falcon-ggml/resolve/main/ggml-model-gpt4all-falcon-q4_0.bin)
- [ggml-stable-vicuna-13B](https://gpt4all.io/models/ggml-stable-vicuna-13B.q4_2.bin)
- [ggml-mpt-7b-instruct](https://gpt4all.io/models/ggml-mpt-7b-instruct.bin)

Functions:

```
linguae.loadLLM : Load a large language model.
linguae.llmChat : Create a chat with the large language model.
linguae.llmDefinitions : Print the definition of the word according the language model in the language asked.
linguae.llmStory : Print a short story written by the language model about the specified topic and in the language asked.
linguae.llmTeacher : Create a chat with the large language model playing a role like a language teacher.
```

- loadLLM:
```python
>>> import linguae
>>> llmWizardlm = linguae.loadLLM("wizardlm-13b-v1.1-superhot-8k.ggmlv3.q4_0.bin")
>>> llmStableVicuna = linguae.loadLLM("ggml-stable-vicuna-13B.q4_2.bin")
>>> llmMPT = linguae.loadLLM("ggml-mpt-7b-instruct.bin")
```


- llmChat:

```python
>>> import linguae
>>> linguae.llmChat('en',"wizardlm-13b-v1.1-superhot-8k.ggmlv3.q4_0.bin")
>>> linguae.llmChat('en',"ggml-gpt4all-l13b-snoozy.bin")
```

or

```python
>>> import linguae
>>> llm = linguae.loadLLM('wizardLM-13B-Uncensored.ggmlv3.q4_0.bin')
>>> linguae.llmChat('es',llm)
```

- llmDefinitions:

```python
>>> import linguae
>>> linguae.llmDefinitions('English','language','wizardlm-13b-v1.1-superhot-8k.ggmlv3.q4_0.bin')
>>> linguae.llmDefinitions('Portuguese','aprender','wizardlm-13b-v1.1-superhot-8k.ggmlv3.q4_0.bin')
```

or

```python
>>> import linguae
>>> llm = linguae.loadLLM('wizardLM-13B-Uncensored.ggmlv3.q4_0.bin')
>>> linguae.llmDefinitions('French', 'parole', llm)
```

- llmStory:

```python
>>> import linguae
>>> linguae.llmStory('English','the colonization of Mars by Human kind.','wizardlm-13b-v1.1-superhot-8k.ggmlv3.q4_0.bin')
>>> linguae.llmStory('Portuguese',"the exploration of the Saturn's moons.",'wizardlm-13b-v1.1-superhot-8k.ggmlv3.q4_0.bin')
```

or

```python
>>> import linguae
>>> llm = linguae.loadLLM('wizardLM-13B-Uncensored.ggmlv3.q4_0.bin')
>>> linguae.llmStory('French', 'the discover of an ancient language in a cave of the Moon', llm)
```

- llmTeacher:

```python
>>> import linguae
>>> linguae.llmTeacher('English',"wizardlm-13b-v1.1-superhot-8k.ggmlv3.q4_0.bin")
>>> linguae.llmTeacher('Portuguese',"ggml-gpt4all-l13b-snoozy.bin")
```

or

```python
>>> import linguae
>>> llm = linguae.loadLLM('wizardLM-13B-Uncensored.ggmlv3.q4_0.bin')
>>> linguae.llmTeacher('Spanish',llm)
```
