import pytest
import json
from model.deepdives import Anomaly, Biome, DeepDives, Stage, DiveType, Variant, Warning
from model.salutes import Salutes
from model.trivia import Trivia
from service.drg import DRGService


@pytest.fixture
def requests_mock(mocker):
    return mocker.patch("requests.get")

@pytest.fixture
def logger_mock(mocker):
    return mocker.Mock()

@pytest.fixture
def drg_service(logger_mock):
    return DRGService(logger=logger_mock)

def test_get_deepdives_success(requests_mock, drg_service):
    # Arrange
    mock_response = {
        "startTime": "2023-05-11T11:00:00Z",
        "endTime": "2023-05-18T11:00:00Z",
        "variants": [
            {
                "type": "Deep Dive",
                "name": "Corroded Reserve",
                "biome": "Radioactive Exclusion Zone",
                "seed": 259722398,
                "stages": [
                    {
                        "id": 1,
                        "primary": "Escort Duty",
                        "secondary": "2 Eggs",
                        "anomaly": "Low Gravity",
                        "warning": None
                    },
                    {
                        "id": 2,
                        "primary": "2 Mini-Mules",
                        "secondary": "Dreadnought",
                        "anomaly": None,
                        "warning": "Shield Disruption"
                    },
                    {
                        "id": 3,
                        "primary": "Twins + Dreadnought",
                        "secondary": "150 Morkite",
                        "anomaly": None,
                        "warning": "Low Oxygen"
                    }
                ]
            },
            {
                "type": "Elite Deep Dive",
                "name": "Naked Burrow",
                "biome": "Salt Pits",
                "seed": 797585550,
                "stages": [
                    {
                        "id": 1,
                        "primary": "200 Morkite",
                        "secondary": "Black Box",
                        "anomaly": "Volatile Guts",
                        "warning": "Exploder Infestation"
                    },
                    {
                        "id": 2,
                        "primary": " 3 Mini-Mules",
                        "secondary": "150 Morkite",
                        "anomaly": None,
                        "warning": "Elite Threat"
                    },
                    {
                        "id": 3,
                        "primary": " 225 Morkite",
                        "secondary": "Dreadnought",
                        "anomaly": None,
                        "warning": "Swarmageddon"
                    }
                ]
            }
        ]
    }
    requests_mock.return_value.status_code = 200
    requests_mock.return_value.text = json.dumps(mock_response)

    # Act
    deepdives = drg_service.get_deepdives()

    # Assert
    assert isinstance(deepdives, DeepDives)
    assert deepdives.startTime == "2023-05-11T11:00:00Z"
    assert deepdives.endTime == "2023-05-18T11:00:00Z"
    assert len(deepdives.variants) == 2
    
    dd: Variant = deepdives.get_variant(DiveType.DEEP_DIVE)
    assert isinstance(dd, Variant)
    assert dd.type == DiveType.DEEP_DIVE
    assert dd.name == "Corroded Reserve"
    assert dd.biome == Biome.RADIOACTIVE_EXCLUSION_ZONE
    assert dd.seed == 259722398
    assert str(dd) == "Deep Dive | Corroded Reserve | Radioactive Exclusion Zone"
    assert len(dd.stages) == 3
    dd_stage1: Stage = dd.get_stage(1)
    assert dd_stage1.id == 1
    assert dd_stage1.primary == "Escort Duty"
    assert dd_stage1.secondary == "2 Eggs"
    assert dd_stage1.anomaly == Anomaly.LOW_GRAVITY
    assert dd_stage1.warning == None
    dd_stage2: Stage = dd.get_stage(2)
    assert dd_stage2.id == 2
    assert dd_stage2.primary == "2 Mini-Mules"
    assert dd_stage2.secondary == "Dreadnought"
    assert dd_stage2.anomaly == None
    assert dd_stage2.warning == Warning.SHIELD_DISRUPTION
    dd_stage3: Stage = dd.get_stage(3)
    assert dd_stage3.id == 3
    assert dd_stage3.primary == "Twins + Dreadnought"
    assert dd_stage3.secondary == "150 Morkite"
    assert dd_stage3.anomaly == None
    assert dd_stage3.warning == Warning.LOW_OXYGEN

    edd: Variant = deepdives.get_variant(DiveType.ELITE_DEEP_DIVE)
    assert isinstance(edd, Variant)
    assert edd.type == DiveType.ELITE_DEEP_DIVE
    assert edd.name == "Naked Burrow"
    assert edd.biome == Biome.SALT_PITS
    assert edd.seed == 797585550
    assert str(edd) == "Elite Deep Dive | Naked Burrow | Salt Pits"
    edd_stage1: Stage = edd.get_stage(1)
    assert edd_stage1.id == 1
    assert edd_stage1.primary == "200 Morkite"
    assert edd_stage1.secondary == "Black Box"
    assert edd_stage1.anomaly == Anomaly.VOLATILE_GUTS
    assert edd_stage1.warning == Warning.EXPLODER_INFESTATION
    edd_stage2: Stage = edd.get_stage(2)
    assert edd_stage2.id == 2
    assert edd_stage2.primary == " 3 Mini-Mules"
    assert edd_stage2.secondary == "150 Morkite"
    assert edd_stage2.anomaly == None
    assert edd_stage2.warning == Warning.ELITE_THREAT
    edd_stage3: Stage = edd.get_stage(3)
    assert edd_stage3.id == 3
    assert edd_stage3.primary == " 225 Morkite"
    assert edd_stage3.secondary == "Dreadnought"
    assert edd_stage3.anomaly == None
    assert edd_stage3.warning == Warning.SWARMAGEDDON

def test_get_deepdives_failure(requests_mock, drg_service):
    # Arrange
    requests_mock.return_value.status_code = 500

    # Act
    deepdives = drg_service.get_deepdives()

    # Assert
    assert deepdives is None

def test_get_salutes_success(requests_mock, drg_service):
    # Arrange
    mock_response = {
        "salutes": [
            "Rock on!",
            "For Karl!",
            "Rock and Stone!",
        ]
    }
    requests_mock.return_value.status_code = 200
    requests_mock.return_value.text = json.dumps(mock_response)

    # Act
    salutes = drg_service.get_salutes()

    # Assert
    assert isinstance(salutes, Salutes)
    assert len(salutes.salutes) == 3
    assert salutes.get_random_salute() in mock_response["salutes"]
    assert salutes.get_salute_at(0) == "Rock on!"
    assert salutes.get_salute_at(1) == "For Karl!"
    assert salutes.get_salute_at(2) == "Rock and Stone!"

def test_get_salutes_failure(requests_mock, drg_service):
    # Arrange
    requests_mock.return_value.status_code = 500

    # Act
    salutes = drg_service.get_salutes()

    # Assert
    assert salutes is None

def test_get_trivia_success(requests_mock, drg_service):
    # Arrange
    mock_response = {
        "trivia": [
            "Deep Dives were added in the September 26th, 2019 update.",
            "If you are falling at a height that would hurt you, and you fall on a fellow dwarf, you dont get hurt."
        ]
    }
    requests_mock.return_value.status_code = 200
    requests_mock.return_value.text = json.dumps(mock_response)

    # Act
    trivia = drg_service.get_trivia()

    # Assert
    assert isinstance(trivia, Trivia)
    assert len(trivia.trivia) == 2
    assert trivia.get_random_trivia() in mock_response["trivia"]
    assert trivia.get_trivia_at(0) == "Deep Dives were added in the September 26th, 2019 update."
    assert trivia.get_trivia_at(1) == "If you are falling at a height that would hurt you, and you fall on a fellow dwarf, you dont get hurt."

def test_get_trivia_failure(requests_mock, drg_service):
    # Arrange
    requests_mock.return_value.status_code = 500

    # Act
    trivia = drg_service.get_trivia()

    # Assert
    assert trivia is None
