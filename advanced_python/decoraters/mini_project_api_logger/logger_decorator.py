import time
from datetime import datetime


def api_logger(func):

    def wrapper(*args, **kwargs):

        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()

        execution_time = round(
            end_time - start_time, 2
        )

        log_message = (
            f"\n{'=' * 40}\n"
            f"Time: {datetime.now()}\n"
            f"Function: {func.__name__}\n"
            f"Args: {args}\n"
            f"Kwargs: {kwargs}\n"
            f"Execution Time: {execution_time} sec\n"
        )

        with open(
            "logs.txt",
            "a",
            encoding="utf-8"
        ) as file:
            file.write(log_message)

        print(log_message)

        return result

    return wrapper