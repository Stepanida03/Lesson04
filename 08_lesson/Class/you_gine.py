import requests


class ProjectPage:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def create_project(self, title):
        project_data = {'title': title}
        response = requests.post(self.base_url + 'projects',
                                 json=project_data, headers=self.headers)
        return response

    def get_projects(self):
        response = requests.get(
            self.base_url + 'projects', headers=self.headers)
        return response

    def get_project_by_id(self, project_id):
        response = requests.get(
            self.base_url + f'projects/{project_id}', headers=self.headers)
        return response

    def update_project(self, project_id, title):
        update_data = {'title': title}
        response = requests.put(self.base_url + f'projects/{project_id}',
                                json=update_data, headers=self.headers)
        return response