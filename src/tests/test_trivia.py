import os
import json
import pytest
from ..service.trivia import TriviaService

@pytest.fixture(autouse=True)
def trivia():
    # setUp TriviaService
    yield TriviaService()

@pytest.fixture(autouse=True)
def file_trivia():
    # SetUp trivias from file
    filename = os.path.join(os.path.dirname(__file__),'../json/trivia.json')
    with open(file=filename, encoding="utf-8") as f:
        data = f.read()
        yield json.loads(data)['trivia']  
 
class TestTriviaService():
    # Test file exist
    def test_trivia_file_exists(self):
        path = "../json/trivia.json"
        assert os.path.isfile(path)
    # Test for TriviaService init
    def test_trivia_service_init(self, trivia, file_trivia):
        assert trivia.trivia == file_trivia
    # Test get one trivia by index
    def test_get_trivia(self, trivia, file_trivia):
        assert trivia.get_trivia(1) == file_trivia[1]
    # Test get random trivia 
    def test_get_random_trivia(self, trivia, file_trivia):
        assert trivia.get_random_trivia() in file_trivia
    
