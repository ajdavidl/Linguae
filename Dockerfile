# docker build -t linguae --rm .
# docker run --rm -ti --name linguae linguae
FROM python:3.10.9-bullseye

RUN apt-get -y update && apt-get -y install gcc

RUN useradd --create-home --shell /bin/bash linguae

WORKDIR /home/linguae

COPY requirements.txt .
COPY *.sh /home/linguae/

# install dependencies
RUN pip --no-cache-dir install -r requirements.txt

# Run shell scripts to download data
RUN ./DownloadMUSEWordEmbeddings.sh
RUN ./DownloadTatoebaSentences.sh

COPY . .

RUN mv wiki.multi* ./linguae/data/museWordVectors/
RUN mv sentences.csv ./linguae/data/tatoebaFiles/

# install linguae
RUN pip install -e .

RUN python -m nltk.downloader punkt

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

USER linguae

CMD ["bash"]