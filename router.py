
import bottle
import controllers.users

from application import application

application.route(
    '/', name='profile'
)(controllers.users.profile)
