from bson.objectid import ObjectId
from datetime import datetime


def add_datetime_to_object(obj):
    now = datetime.utcnow()
    obj['created_at'] = now
    obj['updated_at'] = now
    return obj


def register_update_to_object(obj):
    now = datetime.utcnow()
    obj['updated_at'] = now
    return obj


def id_as_object_id(_id):
    return ObjectId(_id) if type(_id) is str else _id
