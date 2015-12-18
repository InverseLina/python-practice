
# encoding=utf-8
__author__ = 'Hinsteny'
'''
关于高阶函数的使用示例，即函数式编程
'''
from functools import reduce
from operator import itemgetter

def test_map():
    def f(x):
        return x * x

    r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(list(r))

    return "Test map success!"


def test_reduce():
    def f(x, y):
        return x * 10 + y

    r = reduce(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(r)

    return "Test reduce success!"


def test_filter():
    def is_odd(n):
        return n % 2 == 1

    r = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(list(r))

    return "Test reduce success!"


def test_sorted():
    def sort_by_name(*args):
        return itemgetter(0)

    students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
    # 自定义排序函数
    r = sorted(students, key=sort_by_name(0))
    print(list(r))

    # itemgetter函数可以实现多维排序
    r = sorted(students, key=itemgetter(0))
    print(list(r))

    # lambda表达式
    r = sorted(students, key=lambda t: t[1])
    print(list(r))

    # 倒置排序好的列表
    r = sorted(students, key=itemgetter(1), reverse=True)
    print(list(r))

    return "Test sort success!"


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum


def test_return_fun(*args):
    f1 = lazy_sum(1, 3, 5, 7, 9)
    f2 = lazy_sum(1, 3, 5, 7, 9)
    print(f1 == f2)
    print(f1())
    print(f2())


# 闭包实现
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


def test_closure():
    f1, f2, f3 = count()
    print(f1())
    print(f2())
    print(f3())


def test_anonymous_function():
    # 匿名函数
    f = lambda x: x * x
    print(f(5))


# Do test
if __name__ == "__main__":
    test_map()
    test_reduce()
    test_filter()
    test_sorted()
    test_return_fun()
    test_closure()
    test_anonymous_function()

