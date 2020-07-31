# Import flask and template operators
from flask import Flask, jsonify, render_template
from flask_cors import CORS

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)
CORS(app)
    
# Configurations    
app.config.from_object('config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Import a module / component using its blueprint handler variable
from app.sentences.controllers import mod_sent
from app.quiz.controllers import mod_ques

# Register blueprint(s)
app.register_blueprint(mod_sent)
app.register_blueprint(mod_ques)

# Build the database:
db.create_all()

# Setup the routes:
@app.route('/')

@app.route('/introduction')
def HOME():
    """Introduction.html

     Redirects to the homepage of the experiment - Introdution.html
     .. :quickref: Home; Get Introduction.html
    
    """
    return render_template('Introduction.html')

@app.route('/experiment')
def EXP():
    """Experiment.html

    Redirects to the experiment page - Experiment.html
    .. :quickref: Experiment; Get Experiment.html

    """
    return render_template('Experiment.html')

@app.route('/procedure')
def PROC():
    """Procedure.html

    Redirects to the page explaining the procedure - Procedure.html
    .. :quickref: Procedure; Get Procedure.html

    """    
    return render_template('Procedure.html')

@app.route('/theory')
def THEO():
    """Theory.html

    Redirects to the page containing the theory - Theory.html
    .. :quickref: Theory; Get Theory.html

    """
    return render_template('Theory.html')

@app.route('/feedback')
def FEED():
    """Feedback.html

    Redirects to the feedback page - Feedback.html
    .. :quickref: Feedback; Get Feedback.html

    """
    return render_template('Feedback.html')

@app.route('/objective')
def OBJ():
    """Objective.html

    Redirects to the page describing the objective of the experiment - Objective.html
    .. :quickref: Objective; Get Objective.html


    """
    return render_template('Objective.html')

@app.route('/quiz')
def QUIZ():
    """Quiz.html

    Redirects to the quiz page - Quiz.html
    .. :quickref: Quiz; Get Quiz.html


    """
    return render_template('Quiz.html')

@app.route('/q_add')
def Q_ADD():
    """Quiz_add.html

    Redirects to page to add Questions to the database - Quiz_add.html
    .. :quickref: Q_Add; Add Questions page


    """
    return render_template('Quiz_add.html')

@app.route('/s_add')
def S_ADD():
    """Sentence_add.html

    Redirects to the page to add Sentences to the database - Sentence_add.html
    .. :quickref: S_Add; Add Sentences page

    """
    return render_template('Sentence_add.html')
