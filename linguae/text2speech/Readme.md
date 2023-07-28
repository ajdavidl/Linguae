# Text to speech module

Module to convert text into speech.

It uses the [gTTS](https://gtts.readthedocs.io/en/latest/index.html) package under the hood in the `tts` function.

It also uses the [bark](https://github.com/suno-ai/bark) model for generate audio in the `playBark` function.

Functions:

```
linguae.tts : Convert text to speech.
linguae.loadBark : Load all suno-bark models.
linguae.playBark : Generate and play the audio from the text.
```

Examples:

- tts:

```python
>>> import linguae
>>> linguae.tts('en','I like to study languages.')
>>> linguae.tts('pt','Gosto de estudar idiomas.')
```

- bark functions:

```python
>>> import linguae
>>> linguae.loadBark()
>>> linguae.playBark("Language learning is great and wonderfull!!", "en_speaker_0")
>>> linguae.playBark("Aprender idiomas é muito divertido!!", "pt_speaker_1")
```