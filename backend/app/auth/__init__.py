from flask import Blueprint

v1 = '/api/v1'
auth = Blueprint('auth', __name__, url_prefix=f'{v1}/auth')
user = Blueprint('user', __name__, url_prefix=f'/users')
auth.register_blueprint(user)

from . import views