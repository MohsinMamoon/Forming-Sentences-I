import pytest

# @pytest.mark.usefixtures('setup')
class TestMainRoutes():
    def test_introduction(self, client):
        resp = client.get('/', follow_redirects=True)
        assert b"Types of Sentences:" in resp.data
        resp = client.get('/introduction', follow_redirects=True)
        assert b"Types of Sentences:" in resp.data

    def test_procedure(self, client):
        resp = client.get('/procedure', follow_redirects=True)
        assert b"STEP 1:" in resp.data

    def test_theory(self, client):
        resp = client.get('/theory', follow_redirects=True)
        assert b"free word order languages" in resp.data

    def test_feedback(self, client):
        resp = client.get('/feedback', follow_redirects=True)
        assert b"http://feedback.vlabs.ac.in/" in resp.data

    def test_objective(self, client):
        resp = client.get('/objective', follow_redirects=True)
        assert b"know how to form logically correct sentences" in resp.data

    def test_q_add(self, client):
        resp = client.get('/q_add', follow_redirects=True)
        assert b"Add a new Question:" in resp.data

    def test_s_add(self, client):
        resp = client.get('/s_add', follow_redirects=True)
        assert b"Add a new Sentence:" in resp.data

    def test_experiment(self, client):
        resp = client.get('/experiment', follow_redirects=True)
        assert b"Sentence(s) Left" in resp.data

    def test_quiz(self, client):
        resp = client.get('/quiz', follow_redirects=True)
        assert b"Questions-panel" in resp.data