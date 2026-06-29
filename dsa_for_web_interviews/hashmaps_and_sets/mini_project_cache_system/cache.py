cache = {}


def get_cached_user(user_id):
    return cache.get(user_id)


def save_to_cache(user_id, user_name):
    cache[user_id] = user_name