import pytest
import json

@pytest.mark.usefixtures('setup_db')

class TestSentencesDatabase(object):
    def test_addSentence(self, client):
        resp = client.post('/sentences/add', data=dict(Words='["word1", "word2", "word3"]', Vars='["word1 word2 word3", "word2 word1 word3", "word2 word3 word1" ]', Var_type='["type1", "type2", "type3"]', Lang='English'), follow_redirects=True)
        resp = json.loads(resp.get_data(as_text=True))
        assert resp['success'] == True
        assert 'Word1' in resp['sentence']['Words']
        client.get('/sentences/delete', query_string=dict(id=resp['sentence']['ID']), follow_redirects=True)

    def test_getAllSentences(self, client):
        resp = client.get('/sentences', follow_redirects=True)
        resp = json.loads(resp.get_data(as_text=True))
        assert resp['success'] == True
    
    def test_getRandom(self, client):
        resp = client.get('/sentences/get', query_string=dict(lang="English"), follow_redirects=True)
        resp = json.loads(resp.get_data(as_text=True))        
        assert resp['success'] == True
        assert resp['sentence']['Language'] == 'English'

    def test_delId(self, client):
        resp = json.loads(client.post('/sentences/add', data=dict(Words='["word1", "word2", "word3"]', Vars='["word1 word2 word3", "word2 word1 word3", "word2 word3 word1" ]', Var_type='["type1", "type2", "type3"]', Lang='English'), follow_redirects=True).get_data(as_text=True))
        resp = client.get('/sentences/delete', query_string=dict(id=resp['sentence']['ID']), follow_redirects=True)
        resp = json.loads(resp.get_data(as_text=True))
        assert resp['success'] == True
        assert 'Word1' in resp['sentence']['Words']