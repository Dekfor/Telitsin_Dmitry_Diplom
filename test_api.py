# Телицин Дмитрий, 9-я когорта — Финальный проект. Инженер по тестированию плюс.
import pytest
from configuration import create_order, get_order
from data import headers, user_body

def test_create_order():
    data = {"data": user_body}
    response = create_order(data, headers)
    assert response.status_code == 201
    order_data = response.json()
    global order_track
    order_track = order_data["track"]
def test_get_order():
    response = get_order(order_track)
    assert response.status_code == 200
    order_data = response.json()



