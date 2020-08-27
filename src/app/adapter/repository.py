import abc
from typing import List, Optional, Union

from app.domain import model as domain_models
from app import models as orm_models


class BasicRepository:
    @abc.abstractmethod
    def get_user_by_id(self, _id: int) -> domain_models.User:
        """
        :param _id:
        :return: domain_models.User
        """
        raise NotImplemented

    @abc.abstractmethod
    def get_project_by_id(self, _id: int) -> domain_models.Projects:
        """
        :param _id:
        :return: domain_models.Post
        """
        raise NotImplemented

    @abc.abstractmethod
    def get_users(self, page: int) -> List[domain_models.User]:
        """
        :return: Optional[domain_models.Users]
        """
        raise NotImplemented

    @abc.abstractmethod
    def get_projects(self, page: int) -> Optional[domain_models.Projects]:
        """
        :return: Optional[domain_models.Posts]
        """
        raise NotImplemented

    @abc.abstractmethod
    def create_projectw(self, title: str, author: orm_models.User, text: str)\
            -> domain_models.Projects:
        """
        :param title:
        :param author:
        :param text:
        :return: domain_models.Post
        """
        raise NotImplemented

    # TODO append create user
    @abc.abstractmethod
    def create_user(self, username: str, email: str, password: str)\
            -> domain_models.User:
        """
        :param password:
        :param username:
        :param email:
        :return: domain_models.User
        """
        raise NotImplemented

    @abc.abstractmethod
    def update_project_by_id(self, _id: int, )\
            -> domain_models.Projects:
        """
        :param _id:
        :return: domain_models.Post
        """
        raise NotImplemented

    @abc.abstractmethod
    def delete_user_by_id(self, _id: int):
        raise NotImplemented

    @abc.abstractmethod
    def delete_project_by_id(self, _id: int, user: orm_models.User):
        raise NotImplemented


class SQLRepository(BasicRepository):
    """
        ORM models can change in future
    """
    orm_map = {
        domain_models.User: orm_models.User,
        domain_models.Projects: orm_models.Projects,
    }

    def _to_domain_user(self, orm_obj):
        return domain_models.User(
            id=orm_obj.id,
            username=orm_obj.username,
            email=orm_obj.email,
        )

    def _to_domain_post(self, orm_obj):
        return domain_models.Projects(
            id=orm_obj.id,
            name=orm_obj.name,
            user_id=orm_obj.user_id,
            parent=orm_obj.parent,
            created_at=orm_obj.created_at,
        )

    def _get_by_id_from_orm(self, _orm_model, _id: int) -> \
            Union[orm_models.User, orm_models.Projects]:
        """
            Get Django * model by id
        """
        try:
            orm_obj = _orm_model.get_by_id(_id=_id)
        except AttributeError as err:
            raise Exception('asdasd')

        if not orm_obj:
            raise Exception("None obj")
        return orm_obj

    def get_user_by_id(self, _id: int) -> domain_models.User:
        orm_obj = self._get_by_id_from_orm(orm_models.User, _id=_id)

        return self._to_domain_obj(orm_obj)

    def get_post_by_id(self, _id: int) -> domain_models.Projects:
        orm_obj = self._get_by_id_from_orm(orm_models.Projects, _id=_id)

        return self._to_domain_obj(orm_obj)

    def delete_post_by_id(self, _id: int, user: orm_models.User):
        try:
            obj_delete = orm_models.Projects.objects.get(
                author=user,
                pk=_id
            )
        except orm_models.Projects.DoesNotExist as err:
            # raise _response_err(err)
            raise Exception('asd')
        obj_delete.delete()

    def _update_by_id(self, domain_class, _id: int, **kwargs):
        django_model = self.orm_map.get(domain_class)
        orm_obj = self._get_by_id_from_orm(django_model, _id=_id)

        for key in kwargs.keys():
            if key not in domain_class.__dataclass_fields__.keys():
                # raise _response_err(
                #     f"Can not update field {key}"
                # )
                raise Exception('asd')

        for name, value in kwargs.items():
            setattr(orm_obj, name, value)

        orm_obj.save()

    def _get_orm_class(self, domain_obj):

        return self.orm_map.get(type(domain_obj))

    def _domain_to_orm_obj(self, domain_obj):
        orm_class = self._get_orm_class(domain_obj)

        if orm_class is None:
            raise Exception('asd')
            # raise _response_err(f'Unknown class {type(domain_obj)}')

        return orm_class.objects.get(id=domain_obj.id)

    def _to_domain_list(self, orm_objs) \
            -> List[Union[domain_models.User, domain_models.Projects]]:

        domain_items = []
        for item in orm_objs:
            domain_items.append(self._to_domain_obj(item))

        return domain_items

    def _to_domain_obj(self, orm_obj):
        mapper = {
            orm_models.Projects: self._to_domain_post,
            orm_models.User: self._to_domain_user,
        }

        func = mapper.get(type(orm_obj))
        if func is None:
            raise Exception('asdasd')
            # raise _response_err(f'There is not domain model for {type(orm_obj)}')

        return func(orm_obj)

    def get_users(self, page: int) -> List[domain_models.User]:
        try:
            orm_objs = orm_models.User.get_users(page=page)

        # TODO change Exception
        except Exception as err:
            raise Exception(err)

        return self._to_domain_list(orm_objs)

    def get_projects(self, page: int) -> List[domain_models.Projects]:

        try:
            orm_objs = orm_models.Projects.get_projects(page=page)
        # TODO change Exception
        except Exception as err:
            raise Exception(err)

        return self._to_domain_list(orm_objs)

    def user_filter_by_top(self, page: int):
        try:
            orm_objs = orm_models.User.filter_by_top(page=page)
        # TODO change Exception
        except Exception as err:
            raise Exception(err)

        return self._to_domain_list(orm_objs)