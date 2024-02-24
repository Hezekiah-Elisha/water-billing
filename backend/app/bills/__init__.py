from flask import Blueprint

bill = Blueprint('bill', __name__, url_prefix='/api/v1/bills')
charges = Blueprint('charges', __name__, url_prefix='/charges')

bill.register_blueprint(charges)

from . import views