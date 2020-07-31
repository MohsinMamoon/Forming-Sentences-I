from flask_sqlalchemy import SQLAlchemy
from app import db


class Questions(db.Model):
    """Table which stores the Questions for quiz


    Parameters
    ----------
    id: int
        ID of a particular Question
    Question: string
        Text of the Question
    Option1: string
        First Option
    Option2: string
        Second option
    Option3: string
        Third Option
    Option4: string
        Fourth Option
    Language: string
        Language of the question
    Answer: int
        Answer to the question(Option number)

    Returns
    -------
    """
    id = db.Column(db.Integer, primary_key=True)
    Question = db.Column(db.String, unique=False)
    Option1 = db.Column(db.String, unique=False)
    Option2 = db.Column(db.String, unique=False)
    Option3 = db.Column(db.String, unique=False)
    Option4 = db.Column(db.String, unique=False)
    Language = db.Column(db.String, unique=False)
    Answer = db.Column(db.Integer, unique=False)

    def __init__(self, ques, options, answer, lang):
        """Intializes a record in the table questions.


        Parameters
        ----------
        ques: string
            Question text
        options: list
            List of 4 strings each of which represent an option
        answer: int
            Correct Option number in the range(0-3)
        lang: string
            Language of the question

        Returns
        -------

        """
        self.Question = ques
        self.Language = lang
        self.Answer = answer
        self.Option1 = options[0]
        self.Option2 = options[1]
        self.Option3 = options[2]
        self.Option4 = options[3]

    def to_dict(self):
        """Returns a question parsed as an object.

        Parameters
        ----------
        self

        Returns
        -------
        object
           Object contains:
            1. Question
            2. Array of 4 options
            3. Answer to the question
            4. Language of the question

        """
        return {
            'ID' : self.id,
            'Question' : self.Question,
            'Options' : [self.Option1, self.Option2, self.Option3, self.Option4],
            'Answer' : self.Answer,
            'Language' : self.Language
        }
