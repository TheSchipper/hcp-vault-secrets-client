import os
import json
import requests
import configparser

HCP_API_URL = "https://api.cloud.hashicorp.com"


def _read_config(path):
    """Reads the config file from the given path.

       Args:
        path (str): The path to the config file.

       Returns:
        ConfigParser: The ConfigParser instance with the loaded config.
    """
    parser = configparser.ConfigParser()
    parser.read(path)
    return parser


class HcpClient:
    """
    Sets up the client with credentials loaded from environment variables.

    Parameters:
    - local_config : str, optional
      Path to local config file. Defaults to "config.ini".

    Attributes:
    - organization_id (str): HCP organization ID
    - project_name (str): HCP project name
    - project_id (str): HCP project ID
    - access_token (str): HCP API access token
    - api_app_url (str): Base URL for the API application
    - request_headers (dict): Headers for API requests, including auth token

    Reads required HCP credentials from the following environment variables:
    - HCP_ORGANIZATION_ID
    - HCP_PROJECT_NAME
    - HCP_PROJECT_ID
    - HCP_ACCESS_TOKEN
    """
    def __init__(self, config_path="config.ini"):
        self.config = _read_config(config_path)
        self.organization_id = self.config['DEFAULT']['HCP_ORGANIZATION_ID'] or os.environ["HCP_ORGANIZATION_ID"]
        self.project_name = self.config['DEFAULT']['HCP_PROJECT_NAME'] or os.environ["HCP_PROJECT_NAME"]
        self.project_id = self.config['DEFAULT']['HCP_PROJECT_ID'] or os.environ["HCP_PROJECT_ID"]
        self.access_token = self.config['SECRET']['HCP_ACCESS_TOKEN'] or os.environ["HCP_ACCESS_TOKEN"]
        self.api_app_url = (f"{HCP_API_URL}/secrets/2023-06-13/organizations/{self.organization_id}/"
                            f"projects/{self.project_id}/apps/{self.project_name}")
        self.request_headers = {"Authorization": f"Bearer {self.access_token}"}

    def create_app_secret(self, secret_name, secret_value):
        """Creates a new secret for the application.

            Args:
                secret_name (str): The name of the secret to create.
                secret_value (str): The value of the secret to store.

            Returns:
                dict: The JSON response from the HCP API containing details of the
                    newly created secret.

            Raises:
                requests.exceptions.HTTPError: If the request results in an HTTP error.
        """
        url = (f"{HCP_API_URL}/secrets/2023-06-13/organizations/{self.organization_id}/"
               f"projects/{self.project_id}/apps/{self.project_name}/kv")
        body = {"name": secret_name, "value": secret_value}
        resp = requests.post(url, headers=self.request_headers, data=json.dumps(body))
        resp.raise_for_status()
        return resp.json()['secret']

    def get_app_secret(self, secret_name):
        """Gets a secret value for the application.

          Args:
            secret_name (str): The name of the secret to retrieve.

          Returns:
            dict: The JSON response from the HCP API containing the secret value.

          Raises:
            requests.exceptions.HTTPError: If the request results in an HTTP error.
        """
        url = (f"{HCP_API_URL}/secrets/2023-06-13/organizations/{self.organization_id}/"
               f"projects/{self.project_id}/apps/{self.project_name}/open/{secret_name}")
        resp = requests.get(url, headers=self.request_headers)
        resp.raise_for_status()
        return resp.json()['secret']['version']['value']

    def delete_app_secret(self, secret_name):
        """Deletes a secret for the application.

          Args:
            secret_name (str): The name of the secret to delete.

          Returns:
            dict: The JSON response from the HCP API confirming deletion.

          Raises:
            requests.exceptions.HTTPError: If the request results in an HTTP error.
        """
        url = (f"{HCP_API_URL}/secrets/2023-06-13/organizations/{self.organization_id}/"
               f"projects/{self.project_id}/apps/{self.project_name}/secrets/{secret_name}")
        resp = requests.delete(url, headers=self.request_headers)
        resp.raise_for_status()
        return resp.json()

    def get_app(self):
        """Gets details about the configured application.

          Returns:
            dict: The JSON response from the HCP API containing application details.

          Raises:
            requests.exceptions.HTTPError: If the request results in an HTTP error.
        """
        resp = requests.get(self.api_app_url, headers=self.request_headers)
        resp.raise_for_status()
        return resp.json()
