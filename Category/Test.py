

class Student(object):
    count = 0
    books = []

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def printClassInfo(cls):
        print(cls.__name__)
        print(dir(cls))

    @staticmethod
    def printClassAttr():
        print(Student.count)
        print(Student.books)
    pass



Student.books.extend(["python","javascript"])
print(Student.books)
Student.hobbies = ["reading","jogging","swimming"]
print(Student.hobbies)
print(dir(Student))

wilber = Student("Wilber", 28)
print("name:",wilber.name,"age:",wilber.age)
print(dir(wilber))
print(wilber.books)
print(wilber.count)
print(wilber.hobbies)
wilber.gender = "male"

print("name:",wilber.name,"gender:",wilber.gender)
wilber.count = 2
print(wilber.count)
print(Student.count)
wilber.books = "java"
print(wilber.books)
print(Student.books)

Student.printClassInfo()
wilber.printClassInfo()
Student.printClassAttr()
wilber.printClassAttr()

