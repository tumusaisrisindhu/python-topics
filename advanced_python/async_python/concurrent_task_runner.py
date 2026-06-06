import asyncio

async def download_image():
    print("Downloading image...")
    await asyncio.sleep(2)
    print("Image downloaded")


async def download_video():
    print("Downloading video...")
    await asyncio.sleep(3)
    print("Video downloaded")


async def download_document():
    print("Downloading document...")
    await asyncio.sleep(1)
    print("Document downloaded")


async def main():
    await asyncio.gather(
        download_image(),
        download_video(),
        download_document()
    )

asyncio.run(main())