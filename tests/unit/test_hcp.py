"""
Unit tests for the HCP client.
"""

import json
import logging
import os
import unittest
from unittest import IsolatedAsyncioTestCase
from unittest.mock import patch

import pytest
from hcp_vault_secrets_client.hcp import HcpClient

logger = logging.getLogger(__name__)


def _set_mock_vars():
    os.environ["HCP_ORGANIZATION_ID"] = "ORG_ID"
    os.environ["HCP_PROJECT_NAME"] = "PROJECT_NAME"
    os.environ["HCP_PROJECT_ID"] = "PROJECT_ID"
    os.environ["HCP_ACCESS_TOKEN"] = "ACCESS_TOKEN"


class MockResponse:
    def __init__(self, text, status):
        """Initialize mock response"""
        self._text = text
        self.status = status

    async def text(self):
        """Mock response text"""
        return self._text

    async def __aexit__(self, exc_type, exc, tb):
        """Mock response __aexit__"""
        pass

    async def __aenter__(self):
        """Mock response __aenter__"""
        return self

    async def json(self):
        """Mock response json"""
        return json.loads(self._text)


class HcpClientTests(IsolatedAsyncioTestCase):
    def setUp(self):
        """Set up test environment"""
        _set_mock_vars()

    @patch("aiohttp.ClientSession")
    async def test_create_app_secret(self, mock_session):
        """Unit test for create_app_secret"""
        pytest.logger.info("Starting test_a_create_app_secret")
        # Arrange
        expected = {"id": "unit_test_secret"}
        mock_session.post.return_value = MockResponse(
            '{"secret":{"id":"unit_test_secret"}}', 200
        )
        # Act
        actual = await HcpClient().create_app_secret(
            mock_session, "unit_test_secret", "abc123"
        )
        # Assert
        assert actual == expected

    @patch("aiohttp.ClientSession")
    async def test_get_app_secret(self, mock_session):
        """Unit test for get_app_secret"""
        pytest.logger.info("Starting test_b_get_app_secret")
        # Arrange
        expected = "abc123"
        mock_session.get.return_value = MockResponse(
            '{"secret":{"version":{"value": "abc123"}}}', 200
        )
        # Act
        actual = await HcpClient().get_app_secret(mock_session, "unit_test_secret")
        # Assert
        assert actual == expected

    @patch("aiohttp.ClientSession")
    async def test_delete_app_secret(self, mock_session):
        """Unit test for delete_app_secret"""
        pytest.logger.info("Starting test_c_delete_app_secret")
        # Arrange
        expected = {}
        mock_session.delete.return_value = MockResponse("{}", 200)
        # Act
        actual = await HcpClient().delete_app_secret(mock_session, "unit_test_secret")
        # Assert
        assert actual == expected


if __name__ == "__main__":
    unittest.main()
