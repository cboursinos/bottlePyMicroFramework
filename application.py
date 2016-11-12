
import bottle
from bottle import jinja2_view, request, response
import functools
import ujson as json
import settings
import requests


application = bottle.Bottle()


filter_dict = {}


def template_filter(func):
    """Decorator to add the function to filter_dict"""
    filter_dict[func.__name__] = func
    return func


jinja2_view = functools.partial(jinja2_view, template_settings={'filters': filter_dict})


# usr_lang = "el-GR"
global trans_db
json_data = open('locale/translations.json')
trans_db = json_data

json_data = open('locale/translation_ids.json')
trans_ids = json_data

json_data = open('locale/translations_codes.json')
trans_codes = json.load(json_data)


@application.hook('before_request')
def lang_setter():
    if bottle.request.get_cookie('lang'):
        lang = request.get_cookie('lang')
    else:
        lang = 'en-US'
    response.set_cookie('lang', lang, path='/', domain=settings.website_domain)


# @application.hook('before_request')
# def read_session():
#     session_data = {}
#     if bottle.request.get_cookie('session'):
#         session_data = json.loads(bottle.request.get_cookie('session'))
#     session_data['ref'] = bottle.request.get_cookie('ref')