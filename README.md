# Forming-Sentences-I
Remake of Virtual Labs: Computational Linguistics lab experiment - Forming Sentences I

## Installation and Usage:
- In your terminal enter: git clone https://github.com/MohsinMamoon/Forming-Sentences-I.git
- Then go to the folder Forming-Sentences-I: cd Forming-Sentences-I
- Setup a virtual environment: virrtualenv env; source ./env/bin/activate
- Run: pip3 install -r requirements.txt
- Then run the python server by: python3 run.py
- To run the tests run "install_Chrome_webdriver.sh" first and then run: pytest

## Structure of the code

### File Description

-- run.py –> The main python file which runs the server <br/>
-- config.py –> Sets the config for the Flask object <br/>
-- app/ –> All the code for the application (Controllers / Models / Views / Static files) <br/>
-- app/templates/ –> Contains all the html files:
<dl>
<dt>Experiment.html</dt>
<dd>This is the html file for the main experiment</dd>
<dt>Feedback.html</dt>
<dd>This is the page for feedback</dd>
<dt>Introduction.html</dt>
<dd>This is the file for the homepage of the experiment</dd>
<dt>Objective.html</dt>
<dd>This is the file for the page listing the objective of the experiment</dd>
<dt>Procedure.html</dt>
<dd>This is the file which contains the porocedure of the experiment</dd>
<dt>Quiz.html</dt>
<dd>This is the html file for the quiz</dd>
<dt>Theory.html</dt>
<dd>This page contains the theory for the experiment</dd>

</dl><br/>
-- app/static/ –> Contains external vendor's css and js files along with the custom css and javascript for the pages.
<br> The js folder includes:
<br> Experiment.js which includes the code to retrieve the sentences and handles user interaction including validation of sentences, 
<br>Quiz.js which contains the code to retrieve the questions from the database and validate the user inputs. 
<br>Classes.js which handle the interaction with the retrieved items from the database.
<br> The css folder includes:
<br>Experiment.css which contains the custom css for the Experiment page,
<br>Quiz.css which contains the custom css for the Quiz page<br/>
-- app/sentences/ –> Directory containing controllers and models for Sentences(for Experiments) <br/>
-- app/quiz/ –> Directory containing controllers and models for Questions(for Quiz) <br/>
-- app/__init__.py –> Contains initializing for Flask object and handles importing of controllers and models from various modules defined above and handle the main routes<br/>

### Blueprints

-- The app uses two blueprints: <br/>
<dl>
<dt> mod_sent </dt>
<dd> This blueprint is for the models and controllers of the table which stores the sentences for the experiment </dd>
<dt> mod_ques </dt>
<dd> This blueprint is for the models and controllers of the table which stores the questions for the quiz </dd>
</dl>

### Bringing it together

-- User requests a page. <br/>
-- The Flask App decides on the basis of this which page needs to be rendered. <br/>
-- Most of the files don't use backend but Experiment.html and Quiz.html make the respective AJAX calls to the routes defined in the backend. <br/>
-- Backend validates the request returns the response based on the request. <br/>
-- This response is parsed and then put in the respective html file. <br/>

## Routing

--@app.route('/')-Redirects to Introduction.html  <br/>
--@app.route('/introduction')-Redirects to Introduction.html <br/>
--@app.route('/experiment')-Redirects to Experiment.html which contains the main experiment <br/>
--@app.route('/procedure')-Redirects to Procedure.html <br/>
--@app.route('/theory')-Redirects to Theory.html <br/>
--@app.route('/feedback')-Redirects to Feedback.html <br/>
--@app.route('/objective')-Redirects to Objective.html <br/>
--@app.route('/quiz')-Redirects to Quiz.html <br/>
--@mod_sent.route('/sentences/add', methods=['POST'])-Adds a new Sentence to the table <br/>
--@mod_sent.route('/sentences/', methods=['GET'])-Fetches all sentences from the database <br/>
--@mod_sent.route('/sentences/get', methods=['GET'])-Fetches a random sentence for  the experiment <br/>
--@mod_sent.route('/sentences/delete', methods=['GET'])-Deletes a sentence of given ID <br/>
--@mod_ques.route('/quiz/add', methods=['POST'])-Adds a new Question to the table <br/>
--@mod_ques.route('/quiz/', methods=['GET'])-Fetches all question from the database <br/>
--@mod_ques.route('/quiz/get', methods=['GET'])-Fetches all questions of a particular language <br/>
--@mod_ques.route('/delete', methods=['GET'])-Deletes a Question of given ID <br/>
