# How I use this package

When I'm studying German and I want to explore some new words I start the package opening python in the Linguae directory:

```python
>>> import linguae
>>> ger = linguae.German()
```
The commands above create a object from the German language class called `ger`.

In this example, let's explore the word _"Frieden"_.

I can search definitions for that word.

```python
>>> print(ger.wiktionary('Frieden'))
Definitions: Frieden m (strong, genitive Friedens, no plural)
peace

```

I also can query the ConceptNet.io

```python
>>> print(ger.conceptnet('frieden'))
Concepts related to frieden:
1) friedlich (de) DerivedFrom frieden (de)
2) 静ひつ (ja) Synonym frieden (de)
3) 落着き (ja) Synonym frieden (de)
4) 和気あいあい (ja) Synonym frieden (de)
5) frieden (de) RelatedTo frei (de)
6) 靄々 (ja) Synonym frieden (de)
7) 無事 (ja) Synonym frieden (de)
8) friedensgott (de) DerivedFrom frieden (de)
9) friedenstaube (de) DerivedFrom frieden (de)
10) zufrieden (de) DerivedFrom frieden (de)
11) 落ち付き (ja) Synonym frieden (de)
12) 平和 (ja) Synonym frieden (de)
13) 和気靄靄 (ja) Synonym frieden (de)
14) befrieden (de) DerivedFrom frieden (de)
15) 落ち着き (ja) Synonym frieden (de)
16) 靄然 (ja) Synonym frieden (de)
17) friedenspolitik (de) DerivedFrom frieden (de)
18) friedenszeit (de) DerivedFrom frieden (de)
19) 太平 (ja) Synonym frieden (de)
20) 平穏 (ja) Synonym frieden (de) 
```

Word embeddings also can help to learn the words.

```python
>>> print(ger.similarWords('frieden'))
frieden:
frieden - 1.0
friede - 0.851064920425415
friedens - 0.8090165257453918
friedensschluss - 0.7524712681770325
friedensvertrag - 0.7024015188217163
„frieden - 0.6901772618293762
friedensverträge - 0.6860957741737366
vorfrieden - 0.6785338521003723
friedensvertrags - 0.6744495034217834
friedensvertrages - 0.6722211837768555

```

We can put other languages' word embedding models to compare:

```python
>>> en = linguae.loadWordVectors('en')
>>> pt = linguae.loadWordVectors('pt')
>>> print(ger.similarWords('frieden',[en, pt]))
frieden:
frieden - 1.0
friede - 0.851064920425415
friedens - 0.8090165257453918
friedensschluss - 0.7524712681770325
friedensvertrag - 0.7024015188217163
„frieden - 0.6901772618293762
friedensverträge - 0.6860957741737366
vorfrieden - 0.6785338521003723
friedensvertrags - 0.6744495034217834
friedensvertrages - 0.6722211837768555

peace - 0.723686158657074
truce - 0.5650608539581299
hostilities - 0.5593221783638
treaty - 0.5455384850502014
ryswick - 0.5301486849784851
peacemaking - 0.526177167892456
armistice - 0.5199847221374512
peacefulness - 0.5156024098396301
peaceful - 0.5145206451416016
disarmament - 0.4982791841030121

paz - 0.660793662071228
trégua - 0.5516853928565979
armistício - 0.533244252204895
reconciliação - 0.5248205661773682
beligerância - 0.5202039480209351
pacificação - 0.5068607330322266
tréguas - 0.49935710430145264
tratado - 0.49444663524627686
compromisso - 0.49296292662620544
cessar - 0.4924803376197815

```

I often search examples of the word in context (Tatoeba Corpus).

```python
>>> print(ger.textSamples('frieden',5))
Lasst mich in Frieden, Tom und Maria, ich will fernsehen.
Endlich ist Frieden eingekehrt.
Du wünschst Frieden, lebe friedlich, sei ein Friedfertiger.
Die Taube ist das Symbol des Friedens.
Es führt kein Weg zum Frieden, denn Frieden ist der Weg.

```
I can pick one or more sentences to explore the translation and parsing (SpaCy model).

```python
>>> ger.translateTo('en','Die Taube ist das Symbol des Friedens.')
'The pigeon is the symbol of peace.'

>>> ger.translateTo('en','Lasst mich in Frieden, Tom und Maria, ich will fernsehen.')
'Leave me in peace, Tom and Maria, I want to watch TV.'
```

```python
>>> print(ger.parse('Die Taube ist das Symbol des Friedens.'))
Token → POS → Tag → Dep
Die → X → X → ROOT
Taube → NOUN → NOUN → nmod
ist → NOUN → NOUN → flat:foreign
das → ADP → ADP → case
Symbol → PROPN → PROPN → nmod
des → ADP → ADP → case
Friedens → NOUN → NOUN → nmod
. → PUNCT → PUNCT → punct

>>> print(ger.parse('Lasst mich in Frieden, Tom und Maria, ich will fernsehen.'))
Token → POS → Tag → Dep
Lasst → PROPN → PROPN → ROOT
mich → PROPN → PROPN → flat:name
in → X → X → flat:name
Frieden → PROPN → PROPN → flat:name
, → PUNCT → PUNCT → punct
Tom → NOUN → NOUN → appos
und → ADP → ADP → case
Maria → PROPN → PROPN → nmod
, → PUNCT → PUNCT → punct
ich → NOUN → NOUN → det
will → NOUN → NOUN → appos
fernsehen → ADJ → ADJ → amod
. → PUNCT → PUNCT → punct
```

If I wonder how to spell the word I can see the word on Forvo site. The command below will open your default browser on the Forvo site.

```python
>>> ger.audio('Frieden')
https://forvo.com/search/Frieden/de/
```

It's also possible to search for images. This command also opens a new tab on the default browser with the images.

```python
>>> ger.image('Frieden')
https://www.google.com/search?tbm=isch&q=Frieden
```
