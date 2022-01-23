from abc import ABC

from lib.db import Db
from utils import add_datetime_to_object, id_as_object_id, \
    register_update_to_query


class BaseService(ABC):
    ID_FIELD = '_id'
    NAME_FIELD = 'name'

    def __init__(self, name, plural_name=None):
        self.name = name
        self.plural_name = name + 's' if not plural_name else plural_name

    def _create_name_index(self):
        Db.conn[self.name].create_index(
            [self.NAME_FIELD],
            unique=True
        )

    def _create_one(self, obj):
        obj = add_datetime_to_object(obj)
        doc = Db.conn[self.plural_name].insert_one(obj)
        obj[self.ID_FIELD] = doc.inserted_id
        return obj

    def _create_bulk(self, objs):
        objs = list(add_datetime_to_object(obj) for obj in objs)
        docs = Db.conn[self.plural_name].insert_many(objs)
        for _id, obj in zip(docs.inserted_ids, objs):
            obj[self.ID_FIELD] = _id
        return objs

    def create(self, info):
        return self._create_bulk(info) if type(info) is list \
            else self._create_one(info)

    def delete(self, params, return_obj=True):
        if return_obj:
            return self.find_one_and_delete(params)
        return Db.conn[self.plural_name].delete_one(params)

    def delete_by_id(self, _id, return_obj=True):
        if return_obj:
            return self.find_one_and_delete({
                self.ID_FIELD: _id
            })
        return self.delete({self.ID_FIELD: id_as_object_id(_id)})

    def delete_by_name(self, name, return_obj=True):
        if return_obj:
            return self.find_one_and_delete({
                self.NAME_FIELD: name
            })
        return self.delete({self.NAME_FIELD: name})

    def delete_many(self, params):
        return Db.conn[self.plural_name].delete_many(params)

    def find_one(self, params):
        return Db.conn[self.plural_name].find_one(params)

    def find(self, params):
        return list(Db.conn[self.plural_name].find(params))

    def find_all(self):
        return list(Db.conn[self.plural_name].find({}))

    def find_one_by_id(self, _id):
        return self.find_one({self.ID_FIELD: id_as_object_id(_id)})

    def find_one_by_name(self, name):
        return self.find_one({self.NAME_FIELD: name})

    def find_one_and_update(self, query, params):
        params = register_update_to_query(params)
        return Db.conn[self.plural_name].find_one_and_update(
            query, params, return_document=True
        )

    def find_one_and_delete(self, query):
        return Db.conn[self.plural_name].find_one_and_delete(query)

    def update(self, query, params, return_obj=True):
        params = register_update_to_query(params)
        if return_obj:
            return self.find_one_and_update(query, params)
        return Db.conn[self.plural_name].update_one(query, params)

    def update_by_id(self, _id, params, return_obj=True):
        if return_obj:
            return self.find_one_and_update({
                self.ID_FIELD: id_as_object_id(_id)
            }, params)
        return self.update({self.ID_FIELD, id_as_object_id(_id)}, params)

    def update_by_name(self, name, params, return_obj=True):
        if return_obj:
            return self.find_one_and_update({
                self.NAME_FIELD: name
            }, params)
        return self.update({self.NAME_FIELD: name}, params)

    def update_many(self, query, params):
        return list(Db.conn[self.plural_name].update_many(query, params))
