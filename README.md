# Linguae

Python package to explore natural languages.

This is a hobby project to learn natural language processing and text mining tools exploring natural languages.

The available features are parsing, translation, word embeddings similarities, text generation, concordance, verb conjugation, fill mask, wiktionary queries, wikipedia queries, word frequency queries, conceptnet queries, news from Google, browse images and audio samples, text samples, word sentiment, stemming and chatbot.

## Installation

Create a python enviroment using a tool like conda, pyenv or similar. Then open a terminal and insert the commands.

```bash
git clone https://github.com/ajdavidl/Linguae.git
cd Linguae
pip install -r requirements.txt
```

The parse function uses SpaCy models. The commands above install a few SpaCy models. If you need to install other models you can edit the shell script [`InstallSpacyModels.sh`](InstallSpacyModels.sh) to install the models or you can type the following command on the terminal with the model you need. See [SpaCy Models](https://spacy.io/models) for more information.

```bash
python -m spacy download name_of_the_model
```

If you want to play with word embeddings, you need the MUSE word vectors. The links are in [MUSE](https://github.com/facebookresearch/MUSE#download) repository.
Download the languages you wish and put the files in the `Linguae/linguae/data/museWordVectors` directory. You can edit the shell script [`DownloadMUSEWordEmbeddings.sh`](DownloadMUSEWordEmbeddings.sh) to download the data.

To use the concordance and the text sample functions you need the Tatoeba's sentences.
Download the sentences in [Tatoeba](https://tatoeba.org/en/downloads) (clicking in the [sentences.tar.bz2](https://downloads.tatoeba.org/exports/sentences.tar.bz2) link). 
Extract the csv file (`sentences.csv`) and save it in the `Linguae/linguae/data` directory. You can use the shell script [`DownloadTatoebaSentences.sh`](DownloadTatoebaSentences.sh) to download the sentences.

After the above steps, you already can use the `linguae` package inside the root folder. You can also install the package in your python enviroment with the command:

```bash
pip install -e .
```

### Installing in a docker container

It's possible to install this package in a docker container. First edit the scripts [`DownloadMUSEWordEmbeddings.sh`](DownloadMUSEWordEmbeddings.sh) to download the languages you wish and follow the commands in a terminal:

```bash
docker build -t linguae --rm .
docker run --rm -ti --name linguae linguae
```

Keep in mind that the docker image can take up a lot of disk space because of word embeddings data and tatoeba sentences.

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

## License

GNU General Public License v3.0
