import linguae


def example():
    """
    Text linguae functions
    """
    text_en = 'This is an example sentence.'

    text_pt = linguae.translate(from_language='en',to_language='pt',text=text_en)
    text_es = linguae.translate(from_language='en',to_language='es',text=text_en)

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
    print(linguae.wordFreq(language='en',word='the'))
    print('English: house')
    print(linguae.wordFreq(language='en',word='house'))
    print()
    print('Portuguese: de')
    print(linguae.wordFreq(language='pt',word='de'))
    print('Portuguese: casa')
    print(linguae.wordFreq(language='pt',word='casa'))
    print()
    print('Spanish: de')
    print(linguae.wordFreq(language='es',word='de'))
    print('Spanish: casa')
    print(linguae.wordFreq(language='es',word='casa'))

    print("Word Vectors")
    print("Loading models")
    por = linguae.loadVectors('pt')
    print('Portuguese Word Vectors loaded.')
    eng = linguae.loadVectors('en')
    print('English Word Vectors loaded.')
    esp = linguae.loadVectors('es')
    print('Spanish Word Vectors loaded.')
    print(linguae.similar(por,'casa', [eng,esp]))
    print(linguae.similar(eng,'cat', [por,esp]))
    print(linguae.similar(esp,'perro', [por,eng]))

if __name__ == "__main__":
   example()
