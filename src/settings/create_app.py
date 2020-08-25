from flask import Flask

from settings.configs import Config
from settings.extensions import bcrypt, cache, db, migrate, cors

# from conduit import commands, user, profile, articles
# from conduit.settings import ProdConfig
# from conduit.exceptions import InvalidUsage

from src.app.views import blueprint


def create_app(config_object: object = Config):
    """An application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/.

    :param config_object: The configuration object to use.
    """
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config.from_object(config_object)

    register_extensions(app)
    register_blueprints(app)
    # register_errorhandlers(app)
    # register_shellcontext(app)
    # register_commands(app)
    return app


def register_extensions(app):
    """Register Flask extensions."""
    bcrypt.init_app(app)
    cache.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    # jwt.init_app(app)


def register_blueprints(app):
    """Register Flask blueprints."""
    origins = app.config.get('CORS_ORIGIN_WHITELIST', '*')

    cors.init_app(blueprint, origins=origins)

    app.register_blueprint(blueprint)


