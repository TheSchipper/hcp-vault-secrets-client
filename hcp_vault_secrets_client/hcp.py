import os
import json
import requests

HCP_API_URL = "https://api.cloud.hashicorp.com"


class HcpClient:

    def __init__(self):
        self.organization_id = os.environ["HCP_ORGANIZATION_ID"]
        self.project_name = os.environ["HCP_PROJECT_NAME"]
        self.project_id = os.environ["HCP_PROJECT_ID"]
        self.access_token = os.environ["HCP_ACCESS_TOKEN"]
        self.api_app_url = (f"{HCP_API_URL}/secrets/2023-06-13/organizations/{self.organization_id}/"
                            f"projects/{self.project_id}/apps/{self.project_name}")
        self.request_headers = {"Authorization": f"Bearer {self.access_token}"}

    def create_app_secret(self, secret_name, secret_value):
        url = (f"{HCP_API_URL}/secrets/2023-06-13/organizations/{self.organization_id}/"
               f"projects/{self.project_id}/apps/{self.project_name}/kv")
        body = {"name": secret_name, "value": secret_value}
        resp = requests.post(url, headers=self.request_headers, data=json.dumps(body))
        resp.raise_for_status()
        return resp.json()

    def get_app_secret(self, secret_name):
        url = (f"{HCP_API_URL}/secrets/2023-06-13/organizations/{self.organization_id}/"
               f"projects/{self.project_id}/apps/{self.project_name}/secrets/{secret_name}")
        resp = requests.get(url, headers=self.request_headers)
        resp.raise_for_status()
        return resp.json()

    def delete_app_secret(self, secret_name):
        url = (f"{HCP_API_URL}/secrets/2023-06-13/organizations/{self.organization_id}/"
               f"projects/{self.project_id}/apps/{self.project_name}/secrets/{secret_name}")
        resp = requests.delete(url, headers=self.request_headers)
        resp.raise_for_status()
        return resp.json()

    def get_app(self):
        resp = requests.get(self.api_app_url, headers=self.request_headers)
        resp.raise_for_status()
        return resp.json()

    def update_app(self, body):
        resp = requests.patch(self.api_app_url, headers=self.request_headers, data=json.dumps(body))
        resp.raise_for_status()
        return resp.json()

    def delete_app(self, body):
        resp = requests.delete(self.api_app_url, headers=self.request_headers, data=json.dumps(body))
        resp.raise_for_status()
        return resp.json()
