from typing import Any, Iterable


class ValueDict(dict):
    def key_of(self, value: Any) -> Any:
        for key in self:
            if self[key] == value:
                return key

    def keys_of(self, value: Any) -> Iterable:
        for key in self:
            if self[key] == value:
                yield key
                
