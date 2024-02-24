from app.extensions import ma, db
from marshmallow import fields, validate
from .Zone import Zone


class MaZone(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Zone
        load_instance = True
        include_fk = True
        include_relationships = True
        load_only = ()
        dump_only = ("id", "created_at", "updated_at")
        sqla_session = db.session

    name = fields.Str(required=True, validate=validate.Length(min=4, max=80))
    description = fields.Str(required=True, validate=validate.Length(min=4, max=80))
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)


ma_zone = MaZone()
ma_zones = MaZone(many=True)