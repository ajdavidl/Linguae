"""
Named Entity Recognition module
"""
import spacy
import spacy_dbpedia_spotlight


def nerSpacy(model, sentence):
    """
        Get entities from text using spaCy model

        Parameters
        ----------
        model : spacy.lang
            SpaCy Language model. Load from linguae.parsing.parse.loadSpacyModel function

        sentence : str
            Text to be parsed

        Returns
        -------
        str
            String with the entities.
        """
    doc = model(sentence)
    text = "Token → Label\n"
    for ent in doc.ents:
        text += ent.text + ' → ' + ent.label_ + '\n'
    return text


def dbpediaEntityLink(language, sentence):
    """
        Link entities from sentence to dbpedia knowledge base

        Parameters
        __________
        language : str
            Language of the text.
            example: 'en', 'pt', 'es', 'fr', 'de', 'ro', 'it'

        sentence : str
            Sentence to be queried

        Returns
        _______
        str
            String with the entities extracted from the sentence.

    """
    nlp = spacy_dbpedia_spotlight.create(language)
    doc = nlp(sentence)
    listEntities = [(ent.text, ent.kb_id_, ent._.dbpedia_raw_result['@similarityScore'])
                    for ent in doc.ents]
    textOutput = ""
    for tup in listEntities:
        textOutput = textOutput + \
            tup[0] + " - " + tup[1] + " - " + str(tup[2]) + "\n"
    return textOutput
