from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        value = self.cache.get(key)
        if value is not None:
            self.cache.move_to_end(key)
            return value
        return -1

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)