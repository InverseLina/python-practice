
# encoding=utf-8
__author__ = 'Hinsteny'


class Singleton(type):
    """
    Implements the Singleton pattern by use /__new__/ method, this will be very simple
    """

    def __init__(cls, name, bases, class_dict):
        print("init")
        super(Singleton, cls).__init__(name, bases, class_dict)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        print("call")
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance


class A(object, metaclass=Singleton):
    def __init__(self, name):
        print("initxx")
        self.name = name

    def __call__(self, name):
        print("callxx")
        self.name = name

if __name__ == '__main__':
    a = A('apple')
    a('apple')
    print(id(a))
    print(a.name)

    b = A('pear')
    b('pear')
    print(a.name)
    print(id(b))
    print(a == b)
    print(a is b)
    print(b.name)

    c = A('watermelon')
    c('watermelon')
    print(a.name)
    print(b.name)
    print(id(c))
    print(c.name)

