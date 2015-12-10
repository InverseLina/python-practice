__author__ = 'Hinsteny'


class Parent(object):
    """
    Parent class
    """
    numList = []
    # ----------------------------------------------------------------------

    def __init__(self):
        pass

    def numAdd(self, a, b):
        return a+b


class Child(Parent):
    """
    Child class
    """
    # ----------------------------------------------------------------------
    def __init__(self):
        pass

c = Child()

Child.numList.extend(range(10))
print(Child.numList)
print("2+5=", c.numAdd(2, 5))

print(issubclass(Child, Parent))
print(issubclass(Child, object))

print(Parent.__bases__)
print(Child.__bases__)

print(Parent.__doc__)
print(Child.__doc__)

