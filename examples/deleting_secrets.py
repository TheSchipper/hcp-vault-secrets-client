"""
This example shows how to delete a secret.
"""
import asyncio
import aiohttp

from hcp_vault_secrets_client.hcp import HcpClient


async def main() -> None:
    """Async main function."""
    async with aiohttp.ClientSession() as session:
        await HcpClient().delete_app_secret(session, "<add-your-secret-name>")


if __name__ == "__main__":
    asyncio.run(main())
