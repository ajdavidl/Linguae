# Text to speech module

Module to convert text in speech

It uses the [gTTS](https://gtts.readthedocs.io/en/latest/index.html) package under the hood.

Function:

```
linguae.tts : Convert text to speech.
```

Examples:

```python
>>> import linguae
>>> linguae.tts('en','I like to study languages.')
>>> linguae.tts('pt','Gosto de estudar idiomas.')
```
