"""
This module provides a client for the HashiCorp Vault API.
"""
import logging
import os
import json
from dataclasses import dataclass

import aiohttp
from dotenv import load_dotenv

HCP_API_BASE_URL = "https://api.cloud.hashicorp.com"
HCP_API_VERSION = "2023-06-13"
HCP_URL = f"{HCP_API_BASE_URL}/secrets/{HCP_API_VERSION}/organizations"

logger = logging.getLogger(__name__)


@dataclass
class HcpClient:
    """
    Sets up the client with credentials loaded from environment variables. Reads required HCP credentials from the
    following environment variables:
    - HCP_ORGANIZATION_ID
    - HCP_PROJECT_NAME
    - HCP_PROJECT_ID
    - HCP_ACCESS_TOKEN
    """

    def __init__(self):
        load_dotenv()
        self.organization_id = os.environ["HCP_ORGANIZATION_ID"]
        self.project_name = os.environ["HCP_PROJECT_NAME"]
        self.project_id = os.environ["HCP_PROJECT_ID"]
        logger.debug("Initializing HCP client with the following config:")
        logger.debug("organization_id: %s ", self.organization_id)
        logger.debug("project_name: %s ", self.project_name)
        logger.debug("project_id: %s ", self.project_id)

    async def create_app_secret(
        self, session: aiohttp.ClientSession, secret_name: str, secret_value: str
    ) -> str:
        """Creates a secret in a vault app."""
        url = f"{HCP_URL}/{self.organization_id}/projects/{self.project_id}/apps/{self.project_name}/kv"
        headers = {"Authorization": f"Bearer {os.environ['HCP_ACCESS_TOKEN']}"}
        body = {"name": secret_name, "value": secret_value}
        logger.debug("Creating secret %s with value %s", secret_name, secret_value)
        async with session.post(url, headers=headers, data=json.dumps(body)) as resp:
            resp_json = await resp.json()
            logger.debug(f"Response from HCP API: %s ", resp_json)
            return resp_json["secret"]

    async def get_app_secret(
        self, session: aiohttp.ClientSession, secret_name: str
    ) -> str:
        """Gets a secret value from a vault app."""
        url = (
            f"{HCP_URL}/{self.organization_id}/projects/{self.project_id}/"
            f"apps/{self.project_name}/open/{secret_name}"
        )
        headers = {"Authorization": f"Bearer {os.environ['HCP_ACCESS_TOKEN']}"}
        logger.debug("Getting secret %s ", secret_name)
        async with session.get(url, headers=headers) as resp:
            resp_json = await resp.json()
            logger.debug("Response from HCP API: %s ", resp_json)
            return resp_json["secret"]["version"]["value"]

    async def delete_app_secret(
        self, session: aiohttp.ClientSession, secret_name: str
    ) -> str:
        """Deletes a secret from a vault app."""
        url = (
            f"{HCP_URL}/{self.organization_id}/projects/{self.project_id}/"
            f"apps/{self.project_name}/secrets/{secret_name}"
        )
        headers = {"Authorization": f"Bearer {os.environ['HCP_ACCESS_TOKEN']}"}
        logger.debug("Deleting secret %s",secret_name)
        async with session.delete(url, headers=headers) as resp:
            resp_json = await resp.json()
            logger.debug("Response from HCP API: %s", resp_json)
            return resp_json
