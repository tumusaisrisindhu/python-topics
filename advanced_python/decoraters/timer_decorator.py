import time

def timer(func):

    def wrapper(*args, **kwargs):

        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print(f"Execution Time: {end - start:.2f} seconds")

        return result

    return wrapper


@timer
def download_file():
    time.sleep(2)
    print("File Downloaded")


download_file()