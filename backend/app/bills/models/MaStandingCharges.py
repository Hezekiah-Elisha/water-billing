from app import db, ma
from .StandingCharges import StandingCharges
from marshmallow import fields, validate


class MaStandingCharges(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = StandingCharges
        include_fk = True
        include_relationships = True
        dump_only = ("id", "created_at", "updated_at")
        sqla_session = db.session
        load_instance = True

    id = fields.Integer(dump_only=True)
    water_rent = fields.Float(required=True)
    sewerage_rent = fields.Float(required=True)
    consumption_charges = fields.Float(required=True)
    billing_date = fields.DateTime(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

ma_standing_charge = MaStandingCharges()
ma_standing_charges = MaStandingCharges(many=True)