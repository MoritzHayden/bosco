import os
import json
from ..service.trivia import TriviaService
    
def test_trivia_service_init():
    # Get trivia from class
    trivia = TriviaService()
    # Load trivia from file
    filename = os.path.join(os.path.dirname(__file__),'../json/trivia.json')
    with open(file=filename, encoding="utf-8") as f:
        data = f.read()
        loaded_trivia = json.loads(data)['trivia']

    assert trivia.trivia == loaded_trivia
