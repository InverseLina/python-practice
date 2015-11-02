__author__ = 'Hinsteny'


class A(object):
    """"""
    #----------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        print("init_for:",self.__class__)
    def __new__(cls, *args, **kwargs):
        print("new_for:",cls)
        return object.__new__(cls, *args, **kwargs)

a = A()
print()

class Foo(object):
    """

    """
    #----------------------------------------------------------------------
    def __new__(cls, *args, **kwargs):
        # obj = object.__new__(cls, *args, **kwargs)
        obj = Bar.__new__(cls, *args, **kwargs)
        # obj = super(Foo, cls).__new__(cls, *args, **kwargs)
        print("Call_new_Foo:", obj.__class__)
        return obj
    def __init__(self):
        print("Call_init_for_Foo:", self.__class__)

class Bar(Foo):
    """

    """
    #----------------------------------------------------------------------
    def __new__(cls, *args, **kwargs):
        obj = Car.__new__(cls, *args, **kwargs)
        print("Call_new_Bar:", obj.__class__)
        return obj
    def __init__(self):
        print("Call_init_Bar:", self.__class__)

class Student(object):
    """

    """
    #----------------------------------------------------------------------
    def __init__(self):
        pass

class Car(object):
    """

    """
    #----------------------------------------------------------------------
    def __new__(cls, *args, **kwargs):
        obj = object.__new__(cls, *args, **kwargs)
        print("Call_new_Car:", obj.__class__)
        return obj
    def __init__(self):
       print("Call_init_Car:", self.__class__)

foo = Foo()
bar = Bar()
car = Car()

print()

class X(object):
    """
    X class
    """
    flag = 521
    #----------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        print("Call_init_from:", self.__class__)
    def __new__(cls, *args, **kwargs):
        obj = object.__new__(cls, *args, **kwargs)
        print("Call_new_for:", cls.__class__)
        return obj

class Y(object):
    """
    Y class
    """
    #----------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        print("Call_init_from:", self.__class__)
    def __new__(cls, *args, **kwargs):
        obj = object.__new__(X, *args, **kwargs)
        print("Call_new_for:", cls.__class__)
        return obj

y = Y()
print(type(y))
print(y.flag)

print()

class RoundFloat(float):
    """

    """
    #----------------------------------------------------------------------
    def __new__(cls, num):
        num = round(num, 2)
        print(num)
        return float.__new__(RoundFloat, num)
    def __init__(self, num):
        print(num)
        pass

f = RoundFloat(9.2143464)
print(f)
print()