# -*- coding: utf-8 -*-

import bottle
from application import *
from router import *

from bottle import jinja2_view, route, request, static_file, redirect, response, error
import sys


reload(sys)
sys.setdefaultencoding('utf-8')


# make the connection
if __name__ == '__main__':
    bottle.debug(True)
    bottle.run(app=application, server='cherrypy', port=8081, reloader=True, host='0.0.0.0')
