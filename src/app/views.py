
from flask import Blueprint
from app.models import User, Projects
# from flask_apispec import marshal_with
# from flask_jwt_extended import current_user, jwt_required, jwt_optional
from flask_restful import reqparse, Resource
from app.service_layer.service import RequestHandler


class UserSimple(Resource):

    def __init__(self, **kwargs):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'data',
            type=str,
            required=False,
            location='json'
        )
        self.reqparse.add_argument(
            'name',
            type=str,
            required=False,
            location='json'
        )
        self.reqparse.add_argument('page')
        self.handler = RequestHandler()
        super().__init__(**kwargs)

    # TODO create user
    def post(self):
        args = self.reqparse.parse_args()
        # Projects.create_project('asd1', 4)

        return {'data': 'test - user'}

    def get(self):
        args = self.reqparse.parse_args()
        page = args.get('page', 1)
        if page is None:
            page = 1
        data = self.handler.get_users(page)
        return data


class UserIdSimple(Resource):

    def __init__(self, **kwargs):

        self.handler = RequestHandler()

        super().__init__(**kwargs)

    def get(self, some_id):
        data = self.handler.get_user_by_id(some_id)
        return data


class ProjectsSimple(Resource):

    # TODO append JWT - > get user
    def __init__(self, **kwargs):
        self.reqparse = reqparse.RequestParser()

        self.reqparse.add_argument('page')
        self.handler = RequestHandler()
        super().__init__(**kwargs)

    # TODO create Project
    def post(self):
        args = self.reqparse.parse_args()

        return {'data': 'test - project'}

    def get(self):
        args = self.reqparse.parse_args()

        page = args.get('page', 1)
        if page is None:
            page = 1
        data = self.handler.get_projects(page)
        return data


class ProjectsFilterSimple(Resource):

    # TODO append JWT - > get user
    def __init__(self, **kwargs):
        self.reqparse = reqparse.RequestParser()

        self.reqparse.add_argument('page')
        self.handler = RequestHandler()

        super().__init__(**kwargs)

    def get(self):
        args = self.reqparse.parse_args()
        page = args.get('page', 1)
        if page is None:
            page = 1

        data = self.handler.get_projects_by_top(page)

        return data
