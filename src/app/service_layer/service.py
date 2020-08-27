from app.adapter.repository import SQLRepository
from app.service_layer import serializers


class RequestHandler:
    repository_class = SQLRepository

    def __init__(self, *args, **kwargs):
        self.repository = SQLRepository()

    def get_users(self, page: int) -> dict:
        users = self.repository.get_users(page)

        serializer_data = serializers.users.dump(users)

        return {"results": serializer_data, "page": page}

    def get_projects(self, page: int) -> dict:
        projects = self.repository.get_projects(page=page)

        serializer_data = serializers.projects.dump(projects)

        return {"results": serializer_data, "page": page}

    def get_projects_by_top(self, page: int) -> dict:

        users = self.repository.user_filter_by_top(page)

        serializer_data = serializers.users.dump(users)

        return {"results": serializer_data, "page": page}

    def get_user_by_id(self, _id: int) -> dict:
        user = self.repository.get_user_by_id(_id=_id)

        serializer_data = serializers.user.dump(user)

        return serializer_data
