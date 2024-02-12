import json
import logging
import os
import pytest
import unittest

from hcp_vault_secrets_client.hcp import HcpClient
from unittest import IsolatedAsyncioTestCase
from unittest.mock import patch

logger = logging.getLogger(__name__)


def _set_mock_vars():
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

    async def json(self):
        return json.loads(self._text)


class HcpClientTests(IsolatedAsyncioTestCase):

    def setUp(self):
        _set_mock_vars()

    @patch('aiohttp.ClientSession')
    async def test_a_create_app_secret(self, mock_session):
        pytest.logger.info("Starting test_a_create_app_secret")
        # Arrange
        expected = {"id": "unit_test_secret"}
        mock_session.post.return_value = MockResponse('{"secret":{"id":"unit_test_secret"}}', 200)
        # Act
        actual = await HcpClient().create_app_secret(mock_session, "unit_test_secret", "abc123")
        # Assert
        assert actual == expected

    @patch('aiohttp.ClientSession')
    async def test_b_get_app_secret(self, mock_session):
        pytest.logger.info("Starting test_b_get_app_secret")
        expected = "abc123"
        mock_session.get.return_value = MockResponse('{"secret":{"version":{"value": "abc123"}}}', 200)
        actual = await HcpClient().get_app_secret(mock_session, "unit_test_secret")
        assert actual == expected

    @patch('aiohttp.ClientSession')
    async def test_c_delete_app_secret(self, mock_session):
        pytest.logger.info("Starting test_c_delete_app_secret")
        # Arrange
        expected = {}
        mock_session.delete.return_value = MockResponse('{}', 200)
        # Act
        actual = await HcpClient().delete_app_secret(mock_session, "unit_test_secret")
        # Assert
        assert actual == expected


if __name__ == "__main__":
    unittest.main()
