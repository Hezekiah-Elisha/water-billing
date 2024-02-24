from app.extensions import db, ma
from marshmallow import fields, validate
from .Meter import Meter

class MaMeter(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Meter
        load_instance = True
        include_fk = True
        include_relationships = True
        load_only = ()
        dump_only = ("id", "meter_created_at", "meter_updated_at")
        sqla_session = db.session


    id = fields.Integer(dump_only=True)
    meter_type = fields.String(required=True, validate=validate.Length(1))
    meter_number = fields.String(required=True, validate=validate.Length(1))
    meter_status = fields.String(required=True, validate=validate.Length(1))
    meter_created_at = fields.DateTime(dump_only=True)
    meter_updated_at = fields.DateTime(dump_only=True)


ma_meter = MaMeter()
ma_meters = MaMeter(many=True)