import requests
import pytest

def test_status_code_is_200():
    response = requests.get("https://api.pokemonbattle.ru/v2/trainers")
    assert response.status_code == 200

def test_trainer_name_present():
    response = requests.get("https://api.pokemonbattle.ru/v2/trainers", params={"trainer_id": "33496"})
    assert response.status_code == 200
    assert "Ребарбора" in response.text

URL = 'https://api.pokemonbattle.ru/v2'
TRAINER_ID = '33496'

@pytest.mark.parametrize('key, value', [
    ("name", "Пика"),
    ("stage", "1")
])
def test_parametrize(key, value):
    response = requests.get(
        url=f"{URL}/pokemons",
        params={"trainer_id": TRAINER_ID}
    )
    assert response.status_code == 200
    assert response.json()["data"][0][key] == value