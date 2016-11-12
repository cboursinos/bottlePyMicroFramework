# -*- coding: utf-8 -*-
"""Facebook login implementation action layer
"""

import facebook
import ujson as json
import bottle
import requests
from models.users import *
import settings

host=settings.host
client_id=settings.client_id


def facebook_auth(token):
    graph = facebook.GraphAPI(token)
    try:
        profile = graph.get_object("me")
    except:
        profile = None
    return profile


def fb_login(*args, **kwargs):
    req_data = bottle.request.json

    params = {
        'grant_type': 'fb_exchange_token',
        'client_id': '',
        'client_secret': '',
        'fb_exchange_token': req_data.get('accessToken'),
        'scope': 'email'
    }
    fb_response = requests.get("https://graph.facebook.com/oauth/access_token",
                               params=params,
                               verify=True)
    try:
        user_data = facebook_auth(fb_response.content.split('=')[1].split('&')[0])
        data = {}
        data['username'] = user_data['email']
        data['email'] = user_data['email']
        data['password'] = user_data['id']
        data['first_name'] = user_data['first_name']
        data['last_name'] = user_data['last_name']
        data['image'] = "https://graph.facebook.com/{}/picture?width=320&height=320".format(user_data['id'])
        data['social_user'] = True
        data['active'] = True
        data['verified'] = True
        data['mobile'] = False
        data['language'] = 1
        if 'type' not in data:
            data['type'] = "unknown"
        try:
            user = get_user_by_username(user_data['email'])
            data['description'] = user['description']
            data['gender'] = user['gender']
            data['newsletter'] = user['newsletter']
            data['country'] = user['country']
            data['language'] = user['default_language']
        except:
            data['country'] = user_data['locale'].split("_")[1]
            data['gender'] = 'undefined'
            data['newsletter'] = True
            add_user(data)
    except IndexError:
        return json.dumps({'fb_error': fb_response.content})
    return json.dumps(data)
