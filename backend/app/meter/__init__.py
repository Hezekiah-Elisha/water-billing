from flask import Blueprint

meter = Blueprint('meters', __name__, url_prefix='/api/v1/meters')

from . import views