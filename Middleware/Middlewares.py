from flask import request
from functools import wraps
from Classes.Tools import Tools
from Classes.Bridge import is_auth
import requests

Result = Tools.Result
Error = Tools.errors


def validate_request(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # validate access
        return f(*args, **kwargs)

    return decorated_function


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            if not request.headers["Token"] or not request.headers["Id"]:
                return Result(False, Error('TINE'))
        except:
            return Result(False, Error('TINE'))
        if not is_auth(request.headers["Id"], request.headers["Token"]):
            return Result(False, Error("ACCD"))
        return f(*args, **kwargs)

    return decorated_function


def id_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not request.headers["Id"]:
            return Result(False, Error('IDR'))
        return f(*args, **kwargs)

    return decorated_function


def json_body_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # validate access
        if request.get_json() is None:
            return Result(False, Error("JBR"))
        return f(*args, **kwargs)

    return decorated_function


def key_validator(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # validate access
        if request.get_json() is None:
            return Result(False, Error("JBR"))
        return f(*args, **kwargs)

    return decorated_function


def form_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # validate access
        if request.form is None:
            return Result(False, Error("FR"))
        return f(*args, **kwargs)

    return decorated_function

def system_request(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # validate access
        if request.form is None:
            return Result(False, Error("FR"))
        return f(*args, **kwargs)

    return decorated_function
