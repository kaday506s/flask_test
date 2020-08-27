from flask_bcrypt import Bcrypt
from flask_caching import Cache
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

bcrypt = Bcrypt()
db = SQLAlchemy()
migrate = Migrate()
cache = Cache()
cors = CORS()
api = Api()

# from conduit.utils import jwt_identity, identity_loader  # noqa
#
# jwt = JWTManager()
# jwt.user_loader_callback_loader(jwt_identity)
# jwt.user_identity_loader(identity_loader)