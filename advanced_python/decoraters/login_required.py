is_logged_in = True


def login_required(func):

    def wrapper(*args, **kwargs):

        if not is_logged_in:
            print("Access Denied")
            return

        return func(*args, **kwargs)

    return wrapper


@login_required
def dashboard():
    print("Welcome to Dashboard")


dashboard()