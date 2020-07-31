from flask import Blueprint, request, session, jsonify
from app import db
from .models import Sentence
import random
import itertools
import json

mod_sent = Blueprint('sentence', __name__, url_prefix='/sentences')


@mod_sent.route('/add', methods=['POST'])
def add_sentence():
    """Adds a new Sentence to the table.

    .. :quickref: Add Sentence; Add a sentence

    :form Words: (list) Contains the words of the sentence
    :form Vars: (list) Contains the variations of the sentence
    :form Var_type: (list) Contains the types of all the variations
    :form Lang: (string) Language of the sentence

    **Returns**
     JSON object
        The object contains:
            bool
                success = true
            Object
                Sentence added

    """
    words = ''
    for i in json.loads(request.form['Words']):
        words += i + ','
    words = words[:len(words)-1]

    variations = ''
    for (i, j) in zip(json.loads(request.form['Vars']), json.loads(request.form['Var_type'])):
        variations += i + ':' + j + ','
    variations = variations[:len(variations)-1]

    language = request.form['Lang']

    new_sentence = Sentence(words, variations, language)
    db.session.add(new_sentence)
    db.session.commit()

    return jsonify(success=True, sentence=new_sentence.to_dict())


@mod_sent.route('/', methods=['GET'])
def get_all_sentences():
    """Fetches all sentences from the database.

    .. :quickref: Sentences_get; Get All Sentences

    **Returns**
     JSON object
        The object contains:
            bool
                success = true
            list
                List contains objects of every sentence in the database
    """
    sentences = Sentence.query.all()

    return jsonify(success=True, sentences=[sent.to_dict() for sent in sentences])


@mod_sent.route('/get', methods=['GET'])
def get_random():
    """Fetches a random sentence for the experiment.

    .. :quickref: Sentence_get; Get A Random Sentence

    :query lang: (string) Language of the sentence to be sent

    **Returns**
     JSON object
        The object contains:
            bool
                success = true
            Object 
                A sentence

    """
    lang = request.args.get('lang')
    sent = Sentence.query.filter_by(Language=lang).all()
    sent = random.choice(sent)

    return jsonify(success=True, sentence=sent.to_dict())


@mod_sent.route('/delete', methods=['GET'])
def del_id():
    """Deletes a sentence of given ID.

    .. :quickref: Sentence_Delete; Delete a Sentence

    :query id: (int) ID of the sentence to delete

    **Returns**     
     JSON object
        The object contains:
            bool
                success = true
            Object
                Deleted Sentence
    """
    id_to_del = request.args.get('id')
    sent = Sentence.query.filter_by(id=id_to_del).first()
    db.session.delete(sent)
    db.session.commit()

    return jsonify(success=True, sentence=sent.to_dict())
