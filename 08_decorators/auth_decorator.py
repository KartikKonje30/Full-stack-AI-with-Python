from functools import wraps

def auth_decorator(func):
    @wraps(func)
    def wrapper(user_role):
        if(user_role == "admin"):
            return func(user_role)
        else:
            print("Access Denied! Only admins allowed") 
            return None
    return wrapper

@auth_decorator
def auth_login(user_role):
    print("Welcome to Dashboard")


auth_login("user")
auth_login("admin")