
# encoding=utf-8
__author__ = 'Hinsteny'


class Singleton(object):
    """
    Implements the Singleton pattern by make all class instance's  method,s '__dict__' have point to same object;
        1. One class has his '__dict__' and all his instance share that
        2. One class instance has his '__dict__' and he put all his attribute into that
        3. So, the attribution of One class instance = instance's + class's + father class's ;
    """

    # All class instance share this state dictionary
    __share_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Singleton, cls).__new__(cls)
        obj.__dict__ = cls.__share_state
        return obj

    def __init__(self, *args, **kwargs):
        print("init", self, *args)

    def __call__(cls, *args, **kw):
        print("__call__", cls, *args)

    def __hash__(self):
        return 1

    def __eq__(self, other):
            return self.__dict__ is other.__dict__


class A(Singleton):

    def __init__(self, name):
        self.name = name

if __name__ == '__main__':
    a = A('apple')
    print(id(a))
    print(a.name)

    b = A('pear')
    print(a.name)
    print(id(b))
    print(a == b)
    print(a is b)
    print(b.name)

    c = A('watermelon')
    print(a.name)
    print(b.name)
    print(id(c))
    print(c.name)

