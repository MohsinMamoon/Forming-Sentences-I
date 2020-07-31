import pytest
import os
from app import *
from selenium import webdriver

@pytest.fixture(scope="session")
def setup_db():
    # app.config['SQLALCHEMY_DATABASE_URI']  = 'sqlite:///'+str(os.getcwd())+'/temp.db'
    app.config['TESTING'] = True    
    db = SQLAlchemy(app)
    app.register_blueprint(mod_ques)
    app.register_blueprint(mod_sent)
    db.create_all()

@pytest.fixture(scope="session")
def client():
    client = app.test_client()
    return client

@pytest.fixture(scope="session")
def browser():
    C_options = webdriver.ChromeOptions()
    # C_options.add_argument('--headless')
    browser = webdriver.Chrome(chrome_options=C_options)
    return browser
