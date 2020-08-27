from marshmallow import Schema, fields


class UserSchema(Schema):

    id = fields.Int()
    username = fields.String()
    email = fields.String()


class Projects(Schema):
    id = fields.Int()
    name = fields.String()

    user_id = fields.Int()
    parent = fields.Nested(UserSchema())

    created_at = fields.DateTime()


user = UserSchema()
users = UserSchema(many=True)

project = Projects()
projects = Projects(many=True)
