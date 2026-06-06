import asyncio

async def send_email():
    await asyncio.sleep(3)
    print("Email sent")


async def main():
    task = asyncio.create_task(send_email())

    print("Processing order...")
    await asyncio.sleep(1)

    print("Generating invoice...")
    await asyncio.sleep(1)

    print("Invoice generated")

    await task

asyncio.run(main())