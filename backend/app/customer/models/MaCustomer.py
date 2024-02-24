from app.extensions import db, ma
from marshmallow import fields, validate
from .Customer import Customer

class MaCustomer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Customer
        load_instance = True
        include_fk = True
        include_relationships = True
        load_only = ()
        dump_only = ("id", "created_at", "updated_at")
        sqla_session = db.session


    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(1))
    email = fields.String(required=True, validate=validate.Length(1))
    phone_number = fields.String(required=True, validate=validate.Length(1))
    meter_id = fields.Integer(required=True)
    zone_id = fields.Integer(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

    
ma_customer = MaCustomer()
ma_customers = MaCustomer(many=True)