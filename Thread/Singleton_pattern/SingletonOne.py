import sys
# encoding=utf-8
__author__ = 'Hinsteny'

# Set maximum recursion depth exceeded value
sys.setrecursionlimit(100)

class Singleton(object):
    """
    Implements the Singleton pattern by use /__new__/ method, this will be very simple
    """

    def __new__(cls, *args, **kwargs):
        print(args)
        if not hasattr(cls, '_instance'):
            print(cls, "Do create!")
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls)
        else:
            print(cls, "Already has instance, so don't create!")

        return cls._instance


class A(Singleton):

    def __init__(self, name):
        self.name = name

    @property
    def age(self):
        return 2016 - self._birth

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value


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
    c.birth = 1992
    print(c.birth)
    # c.age = 1990  # Only read property
    print(c.age)



