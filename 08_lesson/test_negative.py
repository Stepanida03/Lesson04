import pytest
from Class.you_gine import ProjectPage
from data import (URL, TOKEN, Project_Valid,
                       Project_InValid, Project_Updated)

headers = {
    'Authorization': f'bearer {TOKEN}',
    'Content-Type': 'application/json'
}

@pytest.fixture()
def project_page():
    return ProjectPage(URL, headers)

@pytest.fixture()
def create_project(project_page):
    response = project_page.create_project(Project_Valid)
    assert response.status_code == 201
    project_id = response.json()['id']
    yield project_id

def test_create_project_negative(project_page):
    response = project_page.create_project(Project_InValid)
    assert response.status_code == 400

def test_update_negative(project_page, create_project):
    project_id = create_project
    response = project_page.update_project(project_id, '')
    assert response.status_code == 400
