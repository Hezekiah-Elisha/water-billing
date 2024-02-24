from .User import User
from app.extensions import ma, db
from marshmallow import fields, validate


class MaUser(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        include_fk = True
        include_relationships = True
        load_only = ("password",)
        dump_only = ("id", "created_at", "updated_at")
        sqla_session = db.session

    username = fields.Str(required=True, validate=validate.Length(min=4, max=80))
    full_name = fields.Str(required=True, validate=validate.Length(min=4, max=80))
    password = fields.Str(required=True, validate=validate.Length(min=8, max=128))
    email = fields.Email(required=True, validate=validate.Length(min=4, max=120))
    role = fields.Str(required=True, validate=validate.Length(min=4, max=80))
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)


ma_user = MaUser()
ma_users = MaUser(many=True)