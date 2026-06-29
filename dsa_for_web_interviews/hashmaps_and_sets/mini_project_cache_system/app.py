from api import fetch_user
from cache import (
    get_cached_user,
    save_to_cache
)
from analytics import (
    track_request,
    show_stats
)


def get_user(user_id):

    track_request(user_id)

    cached = get_cached_user(user_id)

    if cached:
        print("Cache Hit")
        return cached

    print("Cache Miss")

    user = fetch_user(user_id)

    save_to_cache(user_id, user)

    return user


print(get_user(1))
print()

print(get_user(2))
print()

print(get_user(1))
print()

print(get_user(3))
print()

print(get_user(2))
print()

show_stats()