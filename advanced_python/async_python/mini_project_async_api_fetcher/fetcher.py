import aiohttp


async def fetch(session, url):
    try:
        async with session.get(url) as response:
            return await response.json()

    except Exception as e:
        return {
            "error": str(e)
        }