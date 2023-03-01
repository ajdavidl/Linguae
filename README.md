# Linguae

Python package to explore natural languages.

This is a hobby project to learn natural language processing and text mining tools exploring natural languages.

The available features are parsing, translation, word embeddings similarities, text generation, concordance, verb conjugation, fill mask, wiktionary queries, wikipedia queries, word frequency queries, conceptnet queries, news from Google, browse images and audio samples, text samples, word sentiment and stemming.

## Status

In construction!!

## Installation

```bash
git clone https://github.com/ajdavidl/Linguae.git
cd Linguae
pip install -r requirements.txt
```

After that you need some SpaCy models to use the parse function. You can use the shell script [`InstallSpacyModels.sh`](InstallSpacyModels.sh) to install the models or type the following commands on the terminal.

```bash
python -m spacy download en_core_web_sm
python -m spacy download pt_core_news_sm
python -m spacy download es_core_news_sm
python -m spacy download it_core_news_sm
python -m spacy download fr_core_news_sm
```

If you want to play with word embeddings, you need the MUSE word vectors. The links are in [MUSE](https://github.com/facebookresearch/MUSE#download) repository.
Download some of it and put the files on `Linguae/linguae/data` folder. You can use the shell script [`DownloadMUSEWordEmbeddings.sh`](DownloadMUSEWordEmbeddings.sh) to download the data.

To use the concordance function you need the Tatoeba's sentences.
Download the sentences in [Tatoeba](https://tatoeba.org/en/downloads).
Extract the csv file (`sentences.csv`) and put it on `Linguae/linguae/data` folder. You can use the shell script [`DownloadTatoebaSentences.sh`](DownloadTatoebaSentences.sh) to download the sentences.

## Usage

In the Linguae directory open python.

```python
import linguae
# translation example
text_en = 'This is an example sentence.'
text_pt = linguae.translate(from_language='en',to_language='pt',text=text_en)
print(text_pt)

# parsing
nlp_en = linguae.loadSpacyModel('en')
pos_en = linguae.parseSpacy(nlp_en,text_en)
print(pos_en)
nlp_pt = linguae.loadSpacyModel('pt')
pos_pt = linguae.parseSpacy(nlp_pt,text_pt)
print(pos_pt)

# get real text examples from news
print(linguae.googleNews('en', 10)) # news in English language
print(linguae.googleNews('pt', 10)) # news in Portuguese language
print(linguae.googleNews('es', 10)) # news in Spanish language

```

See the [`examples.py`](examples.py) and [`Use_case.md`](Use_case.md) files for more examples.

## Contributing

Pull requests are welcome.
