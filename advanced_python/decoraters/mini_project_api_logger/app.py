import time

from logger_decorator import api_logger


@api_logger
def get_users(limit):

    time.sleep(2)

    return f"{limit} users fetched"


@api_logger
def get_products():

    time.sleep(1)

    return "Products fetched"


print(get_users(10))

print(get_products())