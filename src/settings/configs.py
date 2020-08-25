"""Application configuration."""
import os


class Config(object):
    """Base configuration."""

    SECRET_KEY = os.environ.get('CONDUIT_SECRET', 'secret-key')

    APP_DIR = os.path.abspath(os.path.dirname(__file__))

    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))

    BCRYPT_LOG_ROUNDS = 13

    DEBUG_TB_INTERCEPT_REDIRECTS = False

    CACHE_TYPE = 'simple'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_AUTH_USERNAME_KEY = 'email'
    JWT_AUTH_HEADER_PREFIX = 'Token'

    CORS_ORIGIN_WHITELIST = ["*"]

    JWT_HEADER_TYPE = 'Token'
