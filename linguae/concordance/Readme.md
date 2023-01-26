# Concordance module

Module to create concordance views for a given word. It uses [NLTK](https://github.com/nltk/nltk) under the hood.

The main function is `concordance` that receives a word and a list of text and create the concordance view.

Example:

```python
>>> import linguae
>>> EngSentences = linguae.loadLanguageTatoeba('eng')
>>> conc = linguae.concordance(EngSentences,'language')
>>> print(conc)
ou tell them they translate it into their own language and turn it into something totally different 
 released , regardless of price . The profane language used on network television makes many parents
 gracefully . Bill Clinton spoke in ambiguous language when asked to describe his relationship with 
 . It is important for you to learn a foreign language . I 'll open the curtain for you to look out 
ifficult to understand a lecture in a foreign language . The students have taken no notice of these 
 'll find it your advantage to know a foreign language . It is almost impossible to learn a foreign 
>>> PorSentences = linguae.loadLanguageTatoeba('por')
>>> conc = linguae.concordance(PorSentences,'idioma')
>>> print(conc)
 estou muito feliz de te ver ! Aprender bem um idioma estrangeiro requer uma grande quantidade de tr
l é ? O livro mais importante para aprender um idioma é , naturalmente , um dicionário . Odeio meu v
eu cavalo . Que língua é falada no Egito ? Que idioma falam no Egito ? Que língua é utilizada no Egi
rante três dias a partir da meia-noite . O meu idioma não está na lista ! Parte da ilha ficou devast
sabe como ganhar dinheiro . O inglês não é meu idioma nativo . Inglês não é minha língua nativa . Bi
, eu fico . Ela está costurando um vestido . O idioma Na'vi é usado em Avatar . Vamos continuar com 
```
