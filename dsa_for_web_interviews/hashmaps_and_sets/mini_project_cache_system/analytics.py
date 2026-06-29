request_frequency = {}


def track_request(user_id):

    request_frequency[user_id] = (
        request_frequency.get(user_id, 0) + 1
    )


def show_stats():

    print("\nRequest Frequency")

    for user_id, count in request_frequency.items():
        print(
            f"User {user_id}: {count} requests"
        )