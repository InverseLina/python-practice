__author__ = 'Hinsteny'


class Student(object):
    """"""

    #----------------------------------------------------------------------
    __slots__ = ("name","age")
    def __init__(self, name, age):
        self.name = name
        self.age = age

s = Student("Wilber", 28)
print(s.name, s.age)
# s.score = 98

class Person(object):
    """

    """
    __slots = ("name", "age")
    # ----------------------------------------------------------------------

    def __init__(self):
        pass


class Girl(Person):
    """

    """
    __slots = ("score")

    # ----------------------------------------------------------------------

    def __init__(self):
        pass

x = Girl()
x.score = 100