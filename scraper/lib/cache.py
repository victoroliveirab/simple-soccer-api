from lib.db import Db
from utils import add_datetime_to_object, register_update_to_object


class Cache:
    def __init__(self, service, key_name='_id', strategy_fn=None, limit=100):
        self.key_name = key_name
        self.service = service
        self.strategy_fn = strategy_fn
        self.registry = {}
        self.hits = 0
        self.misses = 0
        self.limit = limit

    def _enter(self, key, value, callback=None):
        self.registry[key] = value
        if callback:
            callback()
        self.check_entries()
        return value

    def check_entries(self):
        if self.strategy_fn is None or len(self.registry.keys()) < self.limit:
            return
        removals = 0
        for key in self.registry.keys():
            if not self.strategy_fn(self.registry[key]):
                self.remove(key)
                removals += 1
        # print('Number of removals: {}'.format(removals))

    def add(self, key, value, callback=None):
        obj = add_datetime_to_object({})
        obj['value'] = value
        return self._enter(key, obj, callback=callback)

    def get(self, key):
        if key not in self.registry.keys():
            obj = self.service.find({self.key_name: key})
            if obj is None:
                raise KeyError('{} does not exist'.format(key))
            self.misses += 1
            self.add(key, obj)
        else:
            self.hits += 1
        return self.registry[key]['value']

    def update(self, key, value, callback=None):
        obj = register_update_to_object({'value': value})
        return self._enter(key, obj, callback=callback)

    def remove(self, key):
        del self.registry[key]

    def clear(self):
        self.registry = {}

    @property
    def stats(self):
        return {
            'hits': self.hits,
            'misses': self.misses,
        }
