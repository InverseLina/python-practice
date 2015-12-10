
# encoding=utf-8
__author__ = 'Hinsteny'


def singleton(cls, *args, **kw):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton


@singleton
class MyClass(object):
    a = 1

    def __init__(self, x=0):
        self.x = x

one = MyClass()
two = MyClass()

two.a = 3
print(one.a)
# 3
print(id(one))
print(id(two))
print(one == two)
# True
print(one is two)
# True
one.x = 1
print(one.x)
# 1
print(two.x)