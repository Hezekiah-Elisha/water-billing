from flask import Blueprint

customer = Blueprint('customers', __name__, url_prefix='/api/v1/customers')

from . import views