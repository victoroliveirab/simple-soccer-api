from bson.objectid import ObjectId
from datetime import datetime


def add_datetime_to_object(obj):
    now = datetime.utcnow()
    obj['created_at'] = now
    obj['updated_at'] = now
    return obj


def datetime_from_timestamp(timestamp):
    if timestamp.find(':') == -1:
        return datetime.utcnow()
    hour, minute = map(int, timestamp.split(':'))
    datetime_obj = datetime.utcnow().replace(hour=hour, minute=minute, second=0, microsecond=0)
    return datetime_obj


def register_update_to_object(obj):
    now = datetime.utcnow()
    obj['updated_at'] = now
    return obj


# TODO: find better name
def register_update_to_query(query):
    if '$set' not in query.keys():
        query['$set'] = {}
    query['$set'] = register_update_to_object(query['$set'])
    return query


def id_as_object_id(_id):
    return ObjectId(_id) if type(_id) is str else _id
