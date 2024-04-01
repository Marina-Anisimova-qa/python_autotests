import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
HEADERS = {'Content-Type' : 'application/json'}

def test_status_code():
    response = requests.get (url = f'{URL}/trainers')
    assert response.status_code == 200 #ожидаю статус код 200 на запрос получения списка тренеров

def test_trainer_name():   
    response = requests.get (url = f'{URL}/trainers', params = {"trainer_id" : 2309})
    assert response.json()['data'][0]['trainer_name'] == 'Марина'  #ожидаю имя тренера Марина на запрос получения тренера номер 2309  
