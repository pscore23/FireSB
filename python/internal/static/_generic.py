# -*- coding: utf-8 -*-


class GenericData:
    def __init__(self, *_, **data):
        self.__dict__.update(data)

    def __repr__(self):
        return (self._repr(self)
                if callable(getattr(self, "_repr", ""))
                else getattr(self, "_repr", ""))

    __str__ = __repr__

    def __getitem__(self, key):
        return self.__dict__.__getitem__(key)

    def __setitem__(self, key, value):
        return self.__dict__.__setitem__(key, value)

    def __delitem__(self, key):
        return self.__dict__.__delitem__(key)


class NameRepr(GenericData):
    def __repr__(self):
        return f"<{self.__class__.__name__} {self.name}>"


def _define(name):
    return type(name, (NameRepr,), {})
