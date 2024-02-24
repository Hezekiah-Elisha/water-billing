from flask import Blueprint

meter_reading = Blueprint('meter_reading', __name__, url_prefix='/api/v1/meter-readings')

from . import views