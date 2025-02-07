import requests
import pytest

BASE_URL = "https://ru.yougile.com/api-v2"
TOKEN = "AOR-CaDrzCgkR1M1wkN3Jeem12+XGNbHa6yLiehd3koFHXz3nwGy3HVwleEmf-dy"  

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

class YougileAPI:
    @staticmethod
    def create_project(data):
        response = requests.post(f"{BASE_URL}/projects", json=data, headers=HEADERS)
        return response

    @staticmethod
    def get_projects():
        response = requests.get(f"{BASE_URL}/projects", headers=HEADERS)
        return response

    @staticmethod
    def update_project(project_id, data):
        response = requests.put(f"{BASE_URL}/projects/{project_id}", json=data, headers=HEADERS)
        return response

    @staticmethod
    def get_project(project_id):
        response = requests.get(f"{BASE_URL}/projects/{project_id}", headers=HEADERS)
        return response
    
    def test_create_project():
     project_data = {
        "name": "Test Project",
        "description": "This is a test project."
    }
     response = YougileAPI.create_project(project_data)
     assert response.status_code == 201
     assert "id" in response.json()

def test_get_projects():
    response = YougileAPI.get_projects()
    assert response.status_code == 200
    assert isinstance(response.json(), list)

    def test_create_project_without_name():
     project_data = {
        "description": "This is a test project without a name."
    }
     response = YougileAPI.create_project(project_data)
     assert response.status_code == 400  # Предполагается, что 400 - это ошибка, если имя отсутствует

def test_get_non_existing_project():
    response = YougileAPI.get_project(99999)  # Предполагаем, что это несуществующий ID
    assert response.status_code == 404  # Ожидаем, что проект не найден

    