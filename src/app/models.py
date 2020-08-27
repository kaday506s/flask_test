from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, validates

from settings.extensions import db, bcrypt
from datetime import datetime


PAGINATION_PAGE = 10


class DataBaseMethods:

    @classmethod
    def _commit(cls, orm_obj):
        db.session.add(orm_obj)
        db.session.commit()


class User(db.Model, DataBaseMethods):
    __tablename__ = "User"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(120), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.Binary(128), nullable=True)

    @validates('email')
    def validate_email(self, key, address):
        assert '@' in address
        return address

    def __init__(self, username, email, password=None, **kwargs):
        """Create instance."""
        db.Model.__init__(self, username=username, email=email, **kwargs)
        if password:
            self.set_password(password)
        else:
            self.password = None

    def set_password(self, password):
        """
        Set password.
        """
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, value):
        """
        Check password.
        """
        return bcrypt.check_password_hash(self.password, value)

    def __repr__(self):
        """
        Represent instance as a unique string.
        """
        return '<User({username!r})>'.format(username=self.username)

    @classmethod
    def create_user(cls, username: str, password: str, email: str):
        user = User(username=username, email=email)
        user.set_password(password)

        cls._commit(user)
        return user

    @classmethod
    def get_by_id(cls, _id: int):
        user = db.session.query(User).filter_by(id=_id).first()
        return user

    @classmethod
    def get_users(cls, page: int = 1):
        users = User.query.order_by(User.id).paginate(
            int(page),
            PAGINATION_PAGE,
            error_out=False
        )
        return users.items

    @classmethod
    def filter_by_top(cls, page):

        # TODO not right -> think
        qry = User.query.filter(
            User.id == Projects.user_id
        ).paginate(
            int(page),
            PAGINATION_PAGE,
            error_out=False
        )
        return qry.items


class Projects(db.Model, DataBaseMethods):
    __tablename__ = "Projects"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), unique=True,)

    user_id = db.Column(db.Integer, ForeignKey("User.id"))
    parent = relationship("User", backref=db.backref('Users'))

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    @classmethod
    def create_project(cls, name: str, user_id: int):
        projects = Projects(name=name, user_id=user_id)

        cls._commit(projects)
        return projects

    @classmethod
    def get_projects(cls, page: int = 1):
        projects = Projects.query.order_by(Projects.id).paginate(
            int(page),
            PAGINATION_PAGE,
            error_out=False
        )
        return projects.items