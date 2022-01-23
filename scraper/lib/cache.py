from utils import add_datetime_to_object


class Cache:
    def __init__(self, strategy_fn):
        self.strategy_fn = strategy_fn
        self.registry = {}

    def _check_entries(self):
        keys = self.registry.keys()
        for entry_key in keys:
            if not self.strategy_fn(self.registry[entry_key]):
                self.remove(entry_key)

    def add(self, key, value):
        obj = add_datetime_to_object({})
        obj['value'] = value
        self.registry[key] = obj
        self._check_entries()

    def remove(self, key):
        del self.registry[key]

