import pytest
import json

@pytest.mark.usefixtures('setup_db')

class TestQuestionsDatabase(object):
    def test_addQuestion(self, client):
        resp = client.post('/questions/add', data=dict(Question="Is this working?", Option1="Definitely", Option2="Maybe", Option3="Not at all", Option4="Sometimes", Language="English", Answer=0), follow_redirects=True)
        resp = json.loads(resp.get_data(as_text=True))
        assert resp['success'] == True
        assert resp['question']['Answer'] == 0
        assert resp['question']['Options'][0] == "Definitely"
        client.get('/questions/delete', query_string=dict(id=resp['question']['ID']), follow_redirects=True)

    def test_showAllQuestions(self, client):
        resp = client.get('/questions', follow_redirects=True)
        resp = json.loads(resp.get_data(as_text=True))
        assert resp['success'] == True

    def test_getLang(self, client):
        resp = client.get('/questions/get', query_string=dict(lang="English"), follow_redirects=True)
        resp = json.loads(resp.get_data(as_text=True))        
        assert resp['success'] == True
        assert resp['questions'][0]['Language'] == 'English'

    def test_delId(self, client):
        resp = json.loads(client.post('/questions/add', data=dict(Question="Is this working?", Option1="Definitely", Option2="Maybe", Option3="Not at all", Option4="Sometimes", Language="English", Answer=0), follow_redirects=True).get_data(as_text=True))
        resp = client.get('/questions/delete', query_string=dict(id=resp['question']['ID']), follow_redirects=True)
        resp = json.loads(resp.get_data(as_text=True))
        assert resp['success'] == True
        assert 'Is this working?' in resp['question']['Question']
        assert 'Definitely' in resp['question']['Options']
