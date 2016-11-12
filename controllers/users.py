
from application import *
from bottle import redirect, response, request
import requests
from settings import *
import base64
from helpers import *
from helpers.session import require_session
from models.users import *
import os
import urllib


# @require_session
@jinja2_view('users/index.html', template_lookup=['views'])
def profile():
    return {'trans_ids': trans_ids}
