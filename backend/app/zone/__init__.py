from flask import Blueprint

v1 = '/api/v1'

zone = Blueprint('zone', __name__, url_prefix=f'{v1}/zones')

from . import views

