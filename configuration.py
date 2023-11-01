import requests

API_URL = "https://111976b7-a9d7-4cdd-aa7d-22e24edea547.serverhub.praktikum-services.ru"

def create_order(data, headers):
    response = requests.post(f"{API_URL}/create-order", json=data, headers=headers)
    return response


def get_order(track):
    response = requests.get(f"{API_URL}/get-order/{track}")
    return response
