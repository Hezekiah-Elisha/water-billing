from .models.Meter import Meter
from .models.MaMeter import ma_meter, ma_meters
from flask import jsonify, request
from . import meter

@meter.route('/', methods=['GET'])
def get_all():
    meters = Meter.get_all()
    result = ma_meters.dump(meters)
    return jsonify(result)

@meter.route('/<int:id>', methods=['GET'])
def get_by_id(id):
    meter = Meter.get_by_id(id)
    result = ma_meter.dump(meter)
    return jsonify(result)

@meter.route('/', methods=['POST'])
def create():
    """
    Create a meter

    Returns: Json of created meter
    """
    data = request.get_json()
    if not data:
        return jsonify(message="No input data provided"), 400
    errors = ma_meter.validate(data)
    if errors:
        return jsonify(errors), 422

    meter = Meter(**data)
    if not meter.save():
        return jsonify(message="Meter already exists"), 409
    return jsonify(ma_meter.dump(meter)), 201