import asyncio
import aiohttp

from fetcher import fetch
from urls import URLS


async def main():

    async with aiohttp.ClientSession() as session:

        tasks = []

        for url in URLS:
            tasks.append(
                fetch(session, url)
            )

        results = await asyncio.gather(*tasks)

        print("\nFETCHED DATA\n")

        for item in results:

            if "error" in item:
                print(item["error"])
                continue

            print("-" * 40)
            print("ID:", item["id"])
            print("TITLE:", item["title"])
            print()


asyncio.run(main())