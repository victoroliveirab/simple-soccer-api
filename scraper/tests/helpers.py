from bson.objectid import ObjectId

from datetime import datetime


def to_mongodb_document(obj, timestamp=datetime.utcnow()):
    obj['_id'] = ObjectId()
    obj['created_at'] = timestamp
    obj['updated_at'] = timestamp
    return obj
