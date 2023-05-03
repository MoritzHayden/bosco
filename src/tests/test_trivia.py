import os
import json
import pytest
from ..service.trivia import TriviaService

@pytest.fixture(name="trivia",autouse=True)
def fixture_trivia():
    # setUp TriviaService
    return TriviaService()

@pytest.fixture(name="file_trivia",autouse=True)
def fixture_file_trivia():
    # SetUp trivias from file
    filename = os.path.join(os.path.dirname(__file__),'../json/trivia.json')
    with open(file=filename, encoding="utf-8") as f:
        data = f.read()
        return json.loads(data)['trivia']

class TestTriviaService:
    # Test for TriviaService init
    def test_trivia_service_init(self, trivia, file_trivia):
        assert trivia.trivia == file_trivia
    # Test get one trivia by index
    def test_get_trivia(self, trivia, file_trivia):
        assert trivia.get_trivia(1) == file_trivia[1]
    # Test get random trivia
    def test_get_random_trivia(self, trivia, file_trivia):
        assert trivia.get_random_trivia() in file_trivia
