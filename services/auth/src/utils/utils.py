from flask import abort
import logging







# decorator for authentication

def is_user_logged_in():
    pass


def login_required(func):
    def wrapper(*args, **kwargs):
        if is_user_logged_in():
            return func(*args, **kwargs)
        else:
            abort(403, description="User must be logged in")
            
    
    return