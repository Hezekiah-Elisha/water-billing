from flask import jsonify, request
from .models.Customer import Customer
from .models.MaCustomer import ma_customer, ma_customers
from . import customer

@customer.route('/', methods=['GET'])
def get_all():
    customers = Customer.get_all()
    result = ma_customers.dump(customers)
    return jsonify(result)

@customer.route('/<int:id>', methods=['GET'])
def get_by_id(id):
    customer = Customer.get_by_id(id)
    result = ma_customer.dump(customer)
    return jsonify(result)

@customer.route('/', methods=['POST'])
def create():
    """
    Create a customer

    Returns: Json of created customer
    """
    data = request.get_json()
    if not data:
        return jsonify(message="No input data provided"), 400
    errors = ma_customer.validate(data)
    if errors:
        return jsonify(errors), 422

    customer = Customer(**data)
    if not customer.save():
        return jsonify(message="Customer already exists"), 409
    return jsonify(ma_customer.dump(customer)), 201