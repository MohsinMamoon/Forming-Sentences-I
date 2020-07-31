from flask import Blueprint, request, session, jsonify
from app import db
from .models import Questions

mod_ques = Blueprint('questions', __name__, url_prefix='/questions')


@mod_ques.route('/add', methods=['POST'])
def add_question():
    """Adds a new Question to the table.

    .. :quickref: Add Question; Add a Question

    :form Question: (string) Text of the question  
    :form Answer: (int) Correct Option number  
    :form Language: (string) Language of the question  
    :form Option[1-4]: (strings) Options of the question  

    **Returns**
     JSON object
        The object contains:
            bool
                success = true
            object
                Question added

    """
    ques = request.form['Question']
    answer = int(request.form['Answer'])
    lang = request.form['Language']
    options = [request.form['Option'+str(i)] for i in range(1, 5)]

    new_question = Questions(ques, options, answer, lang)
    db.session.add(new_question)
    db.session.commit()

    return jsonify(success=True, question=new_question.to_dict())


@mod_ques.route('/', methods=['GET'])
def show_all_questions():
    """ Fetches all question from the database.

    .. :quickref: Questions_get; Get All Questiones


    **Returns**
     JSON object
        The object contains:    
            bool
                success = true
            list
                Objects of every question in the database

    """
    questions = Questions.query.all()

    return jsonify(success=True, questions=[ques.to_dict() for ques in questions])


@mod_ques.route('/get', methods=['GET'])
def get_lang():
    """Fetches all questions of a particular language.

    .. :quickref: Question_get; Get Question of a one Language

    :query lang: (string) Language of the sentences to fetch  

    **Returns**
     JSON object
        The object contains:    
            bool
                success = true
            list
                Objects of every question with given language

    """
    lang = request.args.get('lang')
    questions = Questions.query.filter_by(Language=lang).all()

    return jsonify(success=True, questions=[ques.to_dict() for ques in questions])


@mod_ques.route('/delete', methods=['GET'])
def del_id():
    """Deletes a Question of given ID.

    .. :quickref: Question_Delete; Delete a Question

    :query id: (int) ID of the question to delete  

    **Returns**
     JSON object
        The object contains:    
            bool
                success = true
            object
                Deleted Question

    """
    id_to_del = request.args.get('id')
    ques = Questions.query.filter_by(id=id_to_del).first()
    db.session.delete(ques)
    db.session.commit()

    return jsonify(success=True, question=ques.to_dict())
