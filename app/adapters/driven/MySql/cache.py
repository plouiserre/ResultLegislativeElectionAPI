from typing import Any


class CacheMeta(type) :
    _instances = {}
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        if self not in self._instances:
            instance = super().__call__(*args, **kwds)
            self._instances[self] = instance
        return self._instances[self]
        

class Cache(metaclass = CacheMeta) :
    def __init__(self) -> None:
        self.datas = {}
    
    def is_datas_cached(self, key) :
        return key in self.datas
    
    def get_datas(self, key) : 
        return self.datas[key] 
    
    def add_datas(self, value, key) : 
        self.datas[key] = value