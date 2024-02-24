from flask import jsonify, request
from . import bill, charges
from .models.Bill import Bill
from .models.StandingCharges import StandingCharges
from .models.MaBills import ma_bills, ma_bills
from .models.MaStandingCharges import ma_standing_charge, ma_standing_charges

@bill.route('/test', methods=['GET'])
def test():
    return jsonify(message='Billing endpoint working'), 200


@bill.route('/', methods=['GET'])
def get_all_bills():
    bills = Bill.get_all_bills()
    if not bills:
        return jsonify(message='No bills found'), 404
    bills_info = ma_bills.dump(bills)
    return jsonify(bills_info), 200


@bill.route('/<int:id>', methods=['GET'])
def get_bill_by_id(id):
    bill = Bill.get_bill_by_id(id)
    if not bill:
        return jsonify(message='Bill not found'), 404
    bill_info = ma_bills.dump(bill)
    return jsonify(bill_info), 200


@bill.route('/', methods=['DELETE'])
def delete_all_bills():
    bills = Bill.get_all_bills()
    if not bills:
        return jsonify(message='No bills found'), 404
    for bill in bills:
        bill.delete()
    return jsonify(message='All bills deleted'), 200


@charges.route('/', methods=['GET'])
def get_all_charges():
    charges = StandingCharges.get_all()
    if not charges:
        return jsonify(message='No charges found'), 404
    charges_info = ma_standing_charges.dump(charges)
    return jsonify(charges_info), 200


@charges.route('/', methods=['POST'])
def create_charges():
    data = request.get_json()
    if not data:
        return jsonify(message='No input data provided'), 400
    errors = ma_standing_charge.validate(data)
    if errors:
        return jsonify(errors), 422
    charges = StandingCharges(**data)
    info = charges.save()
    return jsonify(info=info), 201

@charges.route('/', methods=['DELETE'])
def delete_all_charges():
    charges = StandingCharges.delete_all()
    if not charges:
        return jsonify(message='No charges found'), 404
    return jsonify(message='All charges deleted'), 200
