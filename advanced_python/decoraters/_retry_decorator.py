def retry(max_attempts):

    def decorator(func):

        def wrapper(*args, **kwargs):

            attempts = 0

            while attempts < max_attempts:

                try:
                    return func(*args, **kwargs)

                except Exception as e:

                    attempts += 1

                    print(
                        f"Attempt {attempts} failed: {e}"
                    )

            print("All retries failed")

        return wrapper

    return decorator


counter = 0


@retry(3)
def connect_server():

    global counter

    counter += 1

    if counter < 3:
        raise Exception("Server Busy")

    print("Connected Successfully")


connect_server()