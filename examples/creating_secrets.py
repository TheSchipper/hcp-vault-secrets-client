"""
This example shows how to create a secret in HCP Vault.
"""
import asyncio
import aiohttp

from hcp_vault_secrets_client.hcp import HcpClient


async def main() -> None:
    """Async main function."""
    async with aiohttp.ClientSession() as session:
        await HcpClient().create_app_secret(
            session, "<add-your-secret-name>", "<add-your-secret-value>"
        )


if __name__ == "__main__":
    asyncio.run(main())
