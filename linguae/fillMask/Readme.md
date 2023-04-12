# Fill Mask module

Module for the task of fill the mask on sentences.

It uses the transformers package under the hood.

Functions:

```
linguae.loadBertMultilingual : Load multilingual Bert Language model.
linguae.loadXLMRoberta : Load XLM-Roberta Language model.
linguae.loadBert : Load Bert Language model.
linguae.loadBertPortuguese : Load Portuguese Bert Language model.
linguae.loadBertEnglish : Load English Bert Language model.
linguae.loadBertSpanish : Load Spanish Bert Language model.
linguae.fillMaskBert : Fill the mask tag on the masked Sentence.
linguae.fillMaskXLMRoberta : Fill the mask tag on the masked Sentence.
```

Examples:

- Multilingual Bert

```python
>>> import linguae
>>> pipeline = linguae.loadBertMultilingual()
>>> s1 = linguae.fillMaskBert(pipeline, "Languages are very [MASK] to learn.")
>>> print(s1)
Languages are very [MASK] to learn. 
Languages are very important to learn. - 0.31147173047065735 
Languages are very difficult to learn. - 0.11882742494344711 
Languages are very easy to learn. - 0.05582128465175629 
Languages are very useful to learn. - 0.02000458538532257 
Languages are very different to learn. - 0.01871359348297119
>>> s2 = linguae.fillMaskBert(pipeline, "Idiomas são muito [MASK] de aprender.")
>>> print(s2)
Idiomas são muito [MASK] de aprender. 
Idiomas são muito fácil de aprender. - 0.23076950013637543 
Idiomas são muito difícil de aprender. - 0.14634060859680176 
Idiomas são muito simples de aprender. - 0.10525200515985489 
Idiomas são muito muito de aprender. - 0.03582744300365448 
Idiomas são muito pouco de aprender. - 0.022088903933763504 
```
- XLM Roberta

```python
>>> import linguae
>>> pipeline = linguae.loadXLMRoberta()
>>> s1 = linguae.fillMaskXLMRoberta(pipeline, "Languages are very <mask> to learn.")
>>> print(s1)
Languages are very <mask> to learn. 
Languages are very easy to learn. - 0.4749657213687897 
Languages are very difficult to learn. - 0.28722426295280457 
Languages are very hard to learn. - 0.0973852351307869 
Languages are very simple to learn. - 0.0434383861720562 
Languages are very important to learn. - 0.023733003064990044
>>> s2 = linguae.fillMaskXLMRoberta(pipeline, "Idiomas são muito <mask> de aprender.")
>>> print(s2)
Idiomas são muito <mask> de aprender. 
Idiomas são muito importantes de aprender. - 0.32905060052871704 
Idiomas são muito simples de aprender. - 0.30486467480659485 
Idiomas são muito difíceis de aprender. - 0.25990456342697144 
Idiomas são muito fácil de aprender. - 0.028021013364195824 
Idiomas são muito difícil de aprender. - 0.01971607282757759
```

- English Bert
```python
>>> import linguae
>>> pipeline = linguae.loadBertEnglish()
```


- Portuguese Bert
```python
>>> import linguae
>>> pipeline = linguae.loadBertPortuguese()
```

- Spanish Bert
```python
>>> import linguae
>>> pipeline = linguae.loadBertSpanish()
```

- Bert
```python
>>> import linguae
>>> pipelineEng = linguae.loadBert('en')
>>> pipelinePor = linguae.loadBert('pt')
```
