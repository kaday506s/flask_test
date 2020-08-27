from flask import Flask

from settings.configs import Config
from settings.extensions import bcrypt, cache, db, migrate, cors, api

from app import models

from app.views import UserSimple, ProjectsSimple, UserIdSimple, ProjectsFilterSimple


class FlaskApp:

    def create_app(self, config_object: object = Config):
        """
        An application factory, as explained here:
        """

        app = Flask(__name__)
        app.url_map.strict_slashes = False
        app.config.from_object(config_object)

        self._register_extensions(app)
        # self._register_blueprints(app)
        self._register_shellcontext(app)
        self._register_api(app)

        return app

    def _register_api(self, app):
        api.add_resource(UserSimple, '/user')
        api.add_resource(UserIdSimple, '/user/<some_id>')
        api.add_resource(ProjectsSimple, '/projects')
        api.add_resource(ProjectsFilterSimple, '/projects/top')
        api.init_app(app)

    def _register_extensions(self, app):
        """Register Flask extensions."""

        bcrypt.init_app(app)
        cache.init_app(app)
        db.init_app(app)
        migrate.init_app(app, db)
        # jwt.init_app(app)

    def _register_blueprints(self, app):
        """
            Register Flask blueprints.
        """
        # origins = app.config.get('CORS_ORIGIN_WHITELIST', '*')

        # cors.init_app(api, origins=origins)

        # app.register_blueprint(blueprint)

        pass

    def _register_shellcontext(self, app):
        """
        Register shell context objects.
        """

        def shell_context():
            """Shell context objects."""
            return {
                'db': db,
                'User': models.User,
                'Projects': models.Projects,
            }

        app.shell_context_processor(shell_context)
