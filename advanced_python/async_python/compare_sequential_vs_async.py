import asyncio
import time

async def task(number):
    await asyncio.sleep(2)
    print(f"Task {number} done")


async def async_version():
    await asyncio.gather(
        task(1),
        task(2),
        task(3)
    )


start = time.time()

asyncio.run(async_version())

end = time.time()

print(f"Time Taken: {end-start:.2f} sec")