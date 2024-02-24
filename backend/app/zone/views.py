from flask import jsonify, request
from . import zone
from .models.MaZone import ma_zone, ma_zones

from .models.Zone import Zone

@zone.route('/', methods=['GET'])
def get_all():
    zones = Zone.get_all()
    return jsonify(ma_zones.dump(zones)), 200

@zone.route('/', methods=['POST'])
def create():
    data = request.get_json()
    zone = ma_zone.load(data)
    result = zone.save()
    if result == False:
        return jsonify({'message': 'Error creating zone'}), 500
    return jsonify(ma_zone.dump(zone)), 201


@zone.route('/<int:id>', methods=['GET'])
def get_by_id(id):
    zone = Zone.get_by_id(id)
    if zone is None:
        return jsonify({'message': 'Zone not found'}), 404
    return jsonify(ma_zone.dump(zone)), 200
