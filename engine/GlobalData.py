LOGGED_USER = None

def set_logged_user(user):
    global LOGGED_USER
    LOGGED_USER = user

def get_logged_user():
    return LOGGED_USER