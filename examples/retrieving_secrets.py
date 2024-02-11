import aiohttp
import asyncio

from hcp_vault_secrets_client.hcp import HcpClient


async def main() -> None:
    async with aiohttp.ClientSession() as session:
        print("SECRET:", await HcpClient().get_app_secret(session, "<add-your-secret-name-here>"))


if __name__ == "__main__":
    asyncio.run(main())
