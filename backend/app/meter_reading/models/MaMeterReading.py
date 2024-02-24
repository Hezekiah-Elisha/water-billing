from app import db, ma
from marshmallow import fields, validate
from .MeterReading import MeterReading
# from datetime import datetime
from flask_marshmallow import Marshmallow as ma

from .MeterReading import MeterReading

ma = ma()


# class MeterReadingSchema(ma.Schema):
#     class Meta:
#         model = MeterReading
#         fields = ('id', 'meter_id', 'user_id', 'reading', 'reading_image', 'reading_date', 'reading_gps_coordinates', 'comments', 'created_at', 'updated_at')

#         _links = ma.Hyperlinks({
#             'self': ma.URLFor('meter_reading_details', values=dict(id='<id>')),
#             'collection': ma.URLFor('meter_readings')
#         })


# ma_meter_reading = MeterReadingSchema()
# ma_meter_readings = MeterReadingSchema(many=True)

# class CustomDateTimeField(fields.Field):
#     def _deserialize(self, value, attr, data, **kwargs):
#         return datetime.strptime(value, '%Y-%m-%d %H:%M:%S')

class MaMeterReading(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = MeterReading
        load_instance = True
        include_fk = True
        include_relationships = True
        load_only = ()
        dump_only = ("id", "meter_reading_created_at", "meter_reading_updated_at")
        sqla_session = db.session

    id = fields.Integer(dump_only=True)
    meter_id = fields.Integer(required=True)
    user_id = fields.Integer(required=True)
    reading = fields.Integer(required=True)
    reading_image = fields.String(required=True, validate=validate.Length(2))
    reading_date = fields.DateTime(format='%Y-%m-%d %H:%M:%S', required=True)
    reading_gps_coordinates = fields.String(required=True, validate=validate.Length(5))
    comments = fields.String(required=True, validate=validate.Length(2))
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)


ma_meter_reading = MaMeterReading()
ma_meter_readings = MaMeterReading(many=True)