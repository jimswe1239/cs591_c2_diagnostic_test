# project/server/users/views.py

from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView

from project.server import bcrypt, db
from project.server.models import User

users_blueprint = Blueprint('users', __name__)

class IndexAPI(MethodView):
    """
    User Index Resource
    """

    def get(self):
        users = list(User.query.all())
        users = [x.email for x in users]
        responseObject = {'users': users}
        return make_response(jsonify(responseObject)), 201


# define the API resources
index_view = IndexAPI.as_view('index_api')

# add Rules for API Endpoints
users_blueprint.add_url_rule(
    '/users/index',
    view_func=index_view,
    methods=['GET']
)