import requests
import pytest


API_URL = "https://054d86a1-4ba2-4da5-97b4-7ab202757d10.serverhub.praktikum-services.ru"


def test_create_order():
    response = requests.post(f"{API_URL}/create-order", json={"data": "your_order_data"})
    assert response.status_code == 201
    order_data = response.json()
    global order_track
    order_track = order_data["track"]


def test_get_order():
    response = requests.get(f"{API_URL}/get-order/{order_track}")
    assert response.status_code == 200
    order_data = response.json()

