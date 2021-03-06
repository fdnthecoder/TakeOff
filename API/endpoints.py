"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""

from flask import Flask
from flask_restx import Resource, Api  # fields
# from werkzeug.exceptions import NotFound
# import textapp.text_app as ta

# import API.db as db

app = Flask(__name__)
api = Api(app)

HELLO = 'hello'
AVAILABLE = 'Available endpoints:'
MAIN_MENU = "Main Menu"
MAIN_MENU_ROUTE = '/menus/main'
MENU_URL = "MenuURL"
BUSINESS_MENU_ROUTE = '/menus/business'
CREATE_BUSINESS_MENU_ROUTE = '/menus/create_business'
USER_MENU_ROUTE = '/menus/user'


@api.route('/hello')
class HelloWorld(Resource):
    """
    The purpose of the HelloWorld class is to have a simple test to see if the
    app is working at all.
    """
    def get(self):
        """
        A trivial endpoint to see if the server is running.
        It just answers with "hello world."
        """
        return {HELLO: 'world'}

@api.route('/business/create')
class business_create(Resource):
    def get(self):
        return {BUSINESS_MENU_ROUTE: 'CREATE'}

@api.route('/business/list')
class list_business(Resource):
    def get(self):
        return {BUSINESS_MENU_ROUTE: 'LIST'}

@api.route('/business/delete')
class delete_business(Resource):
    def get(self):
        return {BUSINESS_MENU_ROUTE: 'DELETE'}

@api.route('/user/create')
class create_user(Resource):
    def get(self):
        return {USER_MENU_ROUTE: 'CREATE'}

@api.route('/user/login')
class user_login(Resource):
    def get(self):
        return {USER_MENU_ROUTE: 'LOGIN'}

@api.route('/user/logout')
class user_logout(Resource):
    def get(self):
        return {USER_MENU_ROUTE: 'LOGOUT'}

# comment and review, different routes?