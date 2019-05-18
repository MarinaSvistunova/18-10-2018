# from collections import deque  # queue LIFO & FIFO
#
#
# # LIFO - Last in first out
#
# # FIFO - First in first out
#
# class MemorizingDict(dict):
#     history = deque(maxlen=10)
#
#     def set(self, key, value):
#         self.history.append(key)  # MemorizingDict.history
#         self[key] = value  # memDict = dict() memDict[key] = value
#
#     def get_history(self):
#         return self.history
#
#
# # print(MemorizingDict.__bases__)
# d = MemorizingDict()
# d.set("boo", 500100)  # 1
# print(d.get_history())
#
# d1 = MemorizingDict()
# d1.set("baz", 100500)  # 2
# print(d1.get_history())


# import functools
#
#
# def singleton(cls):
#     instance = None
#
#     @functools.wraps(cls)
#     def inner(*args, **kwargs):
#         nonlocal instance
#         if instance is None:
#             instance = cls(*args, **kwargs)
#         return instance
#
#     return inner
#
#
# @singleton
# class Connection:
#     pass
#
#
# print(Connection())
# print(id(Connection()))


import warnings
import functools

def deprecated(cls):
    orig_init = cls.__init__

    @functools.wraps(cls.__init__)
    def new_init(self, *args, **kwargs):
        warnings.warn(cls.__name__ + " is deprecated", category=DeprecationWarning)
        orig_init(self, *args, **kwargs)

    cls.__init__ = new_init
    return cls


@deprecated
class Counter:
    def __init__(self, initial=0):
        self.value = initial
        print(initial)


c = Counter(10)