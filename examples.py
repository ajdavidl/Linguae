import linguae


def example():
    """
    Text linguae functions
    """
    text_en = 'This is an example sentence.'

    text_pt = linguae.translate(from_language='en',to_language='pt',text=text_en)
    text_es = linguae.translate(from_language='en',to_language='es',text=text_en)

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


if __name__ == "__main__":
   example()
