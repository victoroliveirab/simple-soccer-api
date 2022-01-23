from utils import add_datetime_to_object, register_update_to_object


class Cache:
    def __init__(self, strategy_fn=None):
        self.strategy_fn = strategy_fn
        self.registry = {}

    def _enter(self, key, value, callback=None):
        self.registry[key] = value
        if callback:
            callback()
        self.check_entries()
        return value

    def check_entries(self):
        if self.strategy_fn is None:
            return
        keys = self.registry.keys()
        for entry_key in keys:
            if not self.strategy_fn(self.registry[entry_key]):
                self.remove(entry_key)

    def add(self, key, value, callback=None):
        obj = add_datetime_to_object({})
        obj['value'] = value
        return self._enter(key, obj, callback=callback)

    def get(self, key):
        if key not in self.registry.keys():
            raise KeyError('{} not found'.format(key))
        return self.registry[key]['value']

    def update(self, key, value, callback=None):
        obj = register_update_to_object({'value': value})
        return self._enter(key, obj, callback=callback)

    def remove(self, key):
        del self.registry[key]

    def clear(self):
        self.registry = {}
