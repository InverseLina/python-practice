
# encoding=utf-8
__author__ = 'Hinsteny'


class Student(object):

    def __init__(self, name, score):
        self._name = name
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))


bart = Student('Bart Simpson', 98)
print(bart._name)
print(bart._Student__name)
bart.__name = "www"
print(bart.__name)