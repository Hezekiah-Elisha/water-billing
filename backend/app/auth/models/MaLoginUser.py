from marshmallow import fields, validate

from app.extensions import ma


class MaLoginUser(ma.Schema):
    email = fields.Str(required=True, validate=validate.Length(min=4, max=80))
    password = fields.Str(required=True, validate=validate.Length(min=8, max=128))
    
    class Meta:
        fields = ("email", "password")
        load_only = ("password",)


ma_login_user = MaLoginUser()