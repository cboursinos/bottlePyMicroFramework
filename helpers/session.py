
from bottle import request, response, redirect
import ujson as json
import requests
from settings import *
import base64
from datetime import *
from functools import wraps


def require_session(fn):
    @wraps(fn)
    def require_session(*args, **kwargs):
        cookie_uid = request.get_cookie("")
        if cookie_uid:
            response.set_cookie('sso', '', expires=0)
            response.set_cookie('sso', base64.b64encode(json.dumps('')), path='/', domain='')
            return fn(**kwargs)
        else:
           redirect("/")
    return require_session