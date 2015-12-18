from enum import Enum
from enum import  unique

# encoding=utf-8
__author__ = 'Hinsteny'


def test_enum():
    Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
    print(Month.Jan, " = ",Month.Jan.value)
    for name, member in Month.__members__.items():
        print(name, '=>', member, ',', member.value)

    return "Test enum success!"


@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


def test_enum_two():
    day1 = Weekday.Mon
    print(day1)
    Weekday.Mon
    print(Weekday.Tue)
    Weekday.Tue
    print(Weekday['Tue'])
    Weekday.Tue
    print(Weekday.Tue.value)
    print(day1 == Weekday.Mon)
    print(day1 == Weekday.Tue)
    print(Weekday(1))
    print(day1 == Weekday(1))
    print("6:", Weekday(6))
    # print("7:", Weekday(7))

    for name, member in Weekday.__members__.items():
        print(name, '=>', member)

# Do test
if __name__ == "__main__":
    print(test_enum())
    test_enum_two()

