import os
import unittest

from hcp_vault_secrets_client.hcp import HcpClient
from unittest.mock import patch


def _set_env_vars():
    os.environ["HCP_ORGANIZATION_ID"] = "ORG_ID"
    os.environ["HCP_PROJECT_NAME"] = "PROJECT_NAME"
    os.environ["HCP_PROJECT_ID"] = "PROJECT_ID"
    os.environ["HCP_ACCESS_TOKEN"] = "ACCESS_TOKEN"


class TestHcpClient(unittest.TestCase):

    def setUp(self):
        _set_env_vars()

    @patch('requests.post')
    def test_create_app_secret(self, mock_post):
        # Arrange
        mock_client = HcpClient()
        mock_post.return_value.status_code = 201
        mock_post.return_value.json.return_value = {
            'id': 'secret123',
            'name': 'mysecret',
            'secret': 'mocked value'
        }

        # Act
        mock_client.create_app_secret('mysecret', 'secretvalue')

        # Assert
        mock_post.assert_called_with(
            'https://api.cloud.hashicorp.com/secrets/2023-06-13/organizations/ORG_ID/projects/PROJECT_ID/apps'
            '/PROJECT_NAME/kv',
            headers={'Authorization': 'Bearer ACCESS_TOKEN'},
            data='{"name": "mysecret", "value": "secretvalue"}'
        )

    @patch('requests.get')
    def test_get_app_secret(self, mock_get):
        mock_client = HcpClient()
        mock_get.return_value.json.return_value = {
            'id': 'secret123',
            'name': 'mysecret',
            'secret': {
                'version': {
                    'value': 'mocked value'
                }
            }
        }

        mock_secret = mock_client.get_app_secret('mysecret')

        mock_get.assert_called_with(
            'https://api.cloud.hashicorp.com/secrets/2023-06-13/organizations/ORG_ID/projects/PROJECT_ID/apps'
            '/PROJECT_NAME/open/mysecret',
            headers={'Authorization': 'Bearer ACCESS_TOKEN'}
        )
        assert mock_secret == 'mocked value'

    @patch('requests.delete')
    def test_delete_app_secret(self, mock_delete):
        # Arrange
        mock_client = HcpClient()
        mock_delete.return_value.json.return_value = {
            'id': 'secret123',
            'name': 'mysecret',
            'secret': 'mocked value'
        }

        # Act
        mock_client.delete_app_secret('mysecret')

        # Assert
        mock_delete.assert_called_with(
            'https://api.cloud.hashicorp.com/secrets/2023-06-13/organizations/ORG_ID/projects/PROJECT_ID/apps'
            '/PROJECT_NAME/secrets/mysecret',
            headers={'Authorization': 'Bearer ACCESS_TOKEN'}
        )


if __name__ == '__main__':
    unittest.main()
