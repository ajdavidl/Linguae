import linguae


def example():
    """
    Text linguae functions
    """
    text_en = 'This is an example sentence.'

    text_pt = linguae.translate(
        from_language='en', to_language='pt', text=text_en)
    text_es = linguae.translate(
        from_language='en', to_language='es', text=text_en)

    print()
    print('English sentence:')
    print(text_en)
    print(linguae.parse(language='en', sentence=text_en))
    print()
    print('Protuguese sentence:')
    print(text_pt)
    print(linguae.parse(language='pt', sentence=text_pt))
    print()
    print('Spanish sentence:')
    print(text_es)
    print(linguae.parse(language='es', sentence=text_es))

    print('Frequencies')
    print('English: the')
    print(linguae.wordFreq(language='en', word='the'))
    print('English: house')
    print(linguae.wordFreq(language='en', word='house'))
    print()
    print('Portuguese: de')
    print(linguae.wordFreq(language='pt', word='de'))
    print('Portuguese: casa')
    print(linguae.wordFreq(language='pt', word='casa'))
    print()
    print('Spanish: de')
    print(linguae.wordFreq(language='es', word='de'))
    print('Spanish: casa')
    print(linguae.wordFreq(language='es', word='casa'))
    print()

    print("Word Vectors")
    print("Loading models")
    por = linguae.loadWordVectors('pt')
    print('Portuguese Word Vectors loaded.')
    eng = linguae.loadWordVectors('en')
    print('English Word Vectors loaded.')
    esp = linguae.loadWordVectors('es')
    print('Spanish Word Vectors loaded.')
    print(linguae.similarWords(por, 'casa', [eng, esp]))
    print(linguae.similarWords(eng, 'cat', [por, esp]))
    print(linguae.similarWords(esp, 'perro', [por, eng]))
    print()

    print("Text generation")
    bloom = linguae.loadBloom()
    print("Bloom language model loaded.")
    print(linguae.generateText(
        bloom, "Linguae is a Python package that helps one to learn a language. The package is ", 100))
    print()
    print(linguae.generateText(
        bloom, "Aprender um idioma deve ser divertido. Por isso, uso o pacote Linguae para explorar ", 100))
    print()

    print("Concordance")
    eng = linguae.loadLanguageTatoeba("eng")
    print(linguae.concordance(eng, "listen"))
    print()
    por = linguae.loadLanguageTatoeba("por")
    print(linguae.concordance(por, "escutar"))
    print()
    spa = linguae.loadLanguageTatoeba("spa")
    print(linguae.concordance(spa, "escuchar"))
    print()

    print("Text samples")
    print(linguae.textSamples(eng, 'learn '))
    print(linguae.textSamples(por, 'aprender '))
    print(linguae.textSamples(spa, 'aprender '))
    print()

    print("Verb conjugation")
    print(linguae.conjugation('pt', 'aprender'))
    print()

    print("wiktionary")
    print(linguae.wiktionaryQuery('en', 'time'))
    print(linguae.wiktionaryQuery('en', 'ship'))
    print()

    print("Conceptnet")
    print(linguae.conceptnetQuery('en', 'language'))
    print(linguae.conceptnetQuery('pt', 'idioma'))
    print(linguae.conceptnetQuery('es', 'lenguaje'))
    print()

    print("News")
    print(linguae.googleNews('en', 10))
    print(linguae.googleNews('pt', 10))
    print(linguae.googleNews('es', 10))
    print()

    print("Fill Mask")
    mBert = linguae.loadBertMultilingual()
    print(linguae.fillMaskBert(mBert, "I'm going to study [MASK]"))
    print(linguae.fillMaskBert(mBert, "No almo??o ela comeu [MASK]"))
    xlm = linguae.loadXLMRoberta()
    print(linguae.fillMaskXLMRoberta(xlm, "I'm going to study <mask>"))
    print(linguae.fillMaskXLMRoberta(xlm, "No almo??o ela comeu <mask>"))
    print()

    print("Wikipedia Queries")
    print(linguae.wikipediaQuery('en', 'Earth'))
    print(linguae.wikipediaQuery('pt', 'Sol'))
    print(linguae.wikipediaQuery('es', 'Luna'))
    print()

    print("Syllables")
    h = linguae.loadHyphenator('en')
    print(linguae.syllables(h, 'languages'))
    h = linguae.loadHyphenator('pt')
    print(linguae.syllables(h, 'idiomas'))
    print()


if __name__ == "__main__":
    example()
