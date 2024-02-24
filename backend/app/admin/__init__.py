from flask import Blueprint

admin = Blueprint(
    'admin', __name__,
    template_folder="templates", url_prefix="/admins",
    static_folder="static"
)

from . import views