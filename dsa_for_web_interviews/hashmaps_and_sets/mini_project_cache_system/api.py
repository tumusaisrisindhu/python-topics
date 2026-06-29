import time
from data import users


def fetch_user(user_id):

    print("Fetching from database...")

    time.sleep(2)

    return users.get(user_id, "User Not Found")