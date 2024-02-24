from flask import Flask
from .extensions import db, ma, cors, jwt, bcrypt
from config import config


def create_app(config_name):
    app = Flask(__name__)
    app.url_map.strict_slashes = False

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    # register extensions
    db.init_app(app)
    ma.init_app(app)
    cors.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)


    # register blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .zone import zone as zone_blueprint
    app.register_blueprint(zone_blueprint)

    from .meter import meter as meter_blueprint
    app.register_blueprint(meter_blueprint)

    from .customer import customer as customer_blueprint
    app.register_blueprint(customer_blueprint)

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint)

    from .meter_reading import meter_reading as meter_reading_blueprint
    app.register_blueprint(meter_reading_blueprint)

    from .bills import bill as bills_blueprint
    app.register_blueprint(bills_blueprint)


    return app

