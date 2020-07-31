from flask_sqlalchemy import SQLAlchemy
from app import db

class Sentence(db.Model):
    """Table which stores the sentences for simulation.


    Parameters
    ----------
    id: int
        ID of a particular sentence
    Words: string
        Words of the sentence concatenated together
    Variations: string
        Variations of the sentence (with their types) concatenated together
    Language: string
        Language of the sentence

    Returns
    -------

    """
    id = db.Column(db.Integer, primary_key=True)
    Words = db.Column(db.String, unique=False)
    Variations = db.Column(db.String, unique=False)
    Language = db.Column(db.String, unique=False)

    def __init__ (self, words, variations, language):
        """ Intializes a record in the table sentences.

        Parameters
        ----------
        words: string
            A list of words concatenated into a string (words seperated by ',')
        variations: string
            A list of variations and their types concatenated into a string (different variations seperated by ',', variation sentence and type seperated by ':')
        language: string
            Language of the Sentence

        Returns
        -------

        """
        self.Words = words.lower()
        self.Variations = variations.lower()
        self.Language = language

    def to_dict(self):
        """Returns a sentence parsed as an object.

        Parameters
        ----------
        self

        Returns
        -------
        object
            Object that contains:
            1. Array of words.
            2. Dictionary of sentence variations and their types.
            3. Language of the sentence

        """
        sent = {}

        sent['Words'] = self.Words.split(',')
        for i,j in enumerate(sent['Words']):
            sent['Words'][i] = j.capitalize()

        sent_vars = {}
        for j in self.Variations.split(','):
            sent_pres = j.split(':')
            sent_vars[sent_pres[0]] = sent_pres[1].capitalize()
        sent['Variations'] = sent_vars

        sent['Language'] = self.Language

        sent['ID'] = self.id
                
        return sent
