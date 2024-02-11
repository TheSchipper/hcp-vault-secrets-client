import os
import unittest
import json
import pytest

from hcp_vault_secrets_client.hcp import HcpClient
from unittest.mock import Mock

HASHICORP_URL = "https://api.cloud.hashicorp.com/secrets/2023-06-13/organizations"


def _set_hcp_env_vars():
    os.environ["HCP_ORGANIZATION_ID"] = "ORG_ID"
    os.environ["HCP_PROJECT_NAME"] = "PROJECT_NAME"
    os.environ["HCP_PROJECT_ID"] = "PROJECT_ID"
    os.environ["HCP_ACCESS_TOKEN"] = "ACCESS_TOKEN"


class MockResponse:
    def __init__(self, text, status):
        self._text = text
        self.status = status

    async def text(self):
        return self._text

    async def __aexit__(self, exc_type, exc, tb):
        pass

    async def __aenter__(self):
        return self


class TestHcpClient(unittest.TestCase):

    def setUp(self):
        _set_hcp_env_vars()

    @pytest.mark.asyncio
    @Mock()
    async def test_create_app_secret(self, mocker):
        # Arrange
        data = {'id': 'secret123',
                'name': 'mysecret',
                'secret': 'mocked value'}
        resp = MockResponse(json.dumps(data), 200)

        # Act
        async with mocker.patch('aiohttp.ClientSession.post', return_value=resp) as mocker:
            resp_dict = await HcpClient().create_app_secret(mocker, "test_secret", "test_value")

        # Assert
        print(resp_dict)
        mocker.assert_called_with(
            f'{HASHICORP_URL}/ORG_ID/projects/PROJECT_ID/apps'
            '/PROJECT_NAME/kv',
            headers={'Authorization': 'Bearer ACCESS_TOKEN'},
            data='{"name": "mysecret", "value": "secretvalue"}'
        )

    @pytest.mark.asyncio
    @Mock()
    async def test_get_app_secret(self, mocker):
        # Arrange
        data = {'id': 'secret123',
                'name': 'mysecret',
                'secret': {
                    'version': {
                        'value': 'mocked value'
                    }
                }}
        resp = MockResponse(json.dumps(data), 200)

        # Act
        async with mocker.patch('aiohttp.ClientSession.post', return_value=resp) as mocker:
            mock_secret = await HcpClient().get_app_secret(mocker, "test_secret")

        # Assert
        print(mock_secret)
        mocker.assert_called_with(
            f'{HASHICORP_URL}/ORG_ID/projects/PROJECT_ID/apps'
            '/PROJECT_NAME/open/mysecret',
            headers={'Authorization': 'Bearer ACCESS_TOKEN'}
        )
        assert mock_secret == 'mocked value'


    @pytest.mark.asyncio
    @Mock()
    async def test_get_app_secret_version(self, mocker):
        # Arrange
        data = {
            'id': 'secret123',
            'name': 'mysecret',
            'secret': 'mocked value'
        }
        resp = MockResponse(json.dumps(data), 200)

        # Act
        async with mocker.patch('aiohttp.ClientSession.post', return_value=resp) as mocker:
            dict_resp = await HcpClient().get_app_secret(mocker, "test_secret")

        # Assert
        print(dict_resp)
        mocker.assert_called_with(
            f'{HASHICORP_URL}/ORG_ID/projects/PROJECT_ID/apps'
            '/PROJECT_NAME/secrets/mysecret',
            headers={'Authorization': 'Bearer ACCESS_TOKEN'}
        )


if __name__ == '__main__':
    unittest.main()
