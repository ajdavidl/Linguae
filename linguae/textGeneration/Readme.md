# Text Generation module

Module to generate text using language models.

It uses the [pipeline class](https://huggingface.co/docs/transformers/main_classes/pipelines) from [transformers](https://github.com/huggingface/transformers) package under the hood.

Funtions:

```
loadBloom : Load Bloom Language model.
loadmGPT : Load mGPT Language model.
loadGPTPortuguese : Load Portuguese GPT2 Language model.
loadGPTEnglish : Load English GPT2 Language model.
loadGPTSpanish : Load Spanish GPT2 Language model. 
generateText : Generate text using a language model.
```

Examples:

* Bloom:

```python
>>> import linguae
>>> pipelineBloom = linguae.loadBloom()
>>> linguae.generateText(pipelineBloom, "Learning languages is very important to ")
>>> linguae.generateText(pipelineBloom, "Aprender idiomas é muito importante para ")
>>> linguae.generateText(pipelineBloom, "Aprender idiomas es muy importante para")
```

* mGPT:

```python
>>> import linguae
>>> pipelinemGPT = linguae.loadmGPT()
>>> linguae.generateText(pipelinemGPT, "Learning languages is very important to ")
>>> linguae.generateText(pipelinemGPT, "Aprender idiomas é muito importante para ")
>>> linguae.generateText(pipelinemGPT, "Aprender idiomas es muy importante para")
```

* English GPT:

```python
>>> import linguae
>>> pipelineGPTEng = linguae.loadGPTEnglish()
>>> linguae.generateText(pipelineGPTEng, "Learning languages is very important to ")
```

* Portuguese GPT:

```python
>>> import linguae
>>> pipelineGPTPor = linguae.loadGPTPortuguese()
>>> linguae.generateText(pipelineGPTPor, "Aprender idiomas é muito importante para ")
```

* Spanish GPT:

```python
>>> import linguae
>>> pipelineGPTSpa = linguae.loadGPTSpanish()
>>> linguae.generateText(pipelineGPTSpa, "Aprender idiomas es muy importante para")
```

* GPT:

Available languages: English, Spanish, Portuguese and German.

```python
>>> import linguae
>>> pipeline = linguae.loadGPT('en')
>>> linguae.generateText(pipeline, "Learning languages is very important to ")
```


