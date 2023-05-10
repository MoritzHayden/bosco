import os
import json
import pytest

from service.salute import SaluteService

@pytest.fixture(name="salute", autouse=True)
def fixture_salute():
    return SaluteService()

@pytest.fixture(name="file_salute", autouse=True)
def fixture_file_salute():
    filename = os.path.join(os.path.dirname(__file__), "../../json/salutes.json")
    with open(file=filename, encoding="utf-8") as f:
        return json.load(f)['salutes']

class TestSaluteService:
    # Test for SaluteService init
    def test_salute_service_init(self, salute, file_salute):
        assert isinstance(salute, SaluteService)
        assert isinstance(salute.salutes, list)
        assert salute.salutes == file_salute

    # Test get one salute by index
    def test_get_salute(self, salute, file_salute):
        assert isinstance(salute.salutes, list)
        assert isinstance(salute.get_salute(1), str)
        assert salute.salutes # Check list if empty
        assert salute.get_salute(1) == file_salute[1]

    # Test get random salute
    def test_get_random_salute(self, salute, file_salute):
        assert isinstance(salute.get_random_salute(), str)
        assert salute.get_random_salute() in file_salute
