
# encoding=utf-8
__author__ = 'Hinsteny'


def fact(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


def move(n, a, b, c):
    if n == 1:
        print('%s --> %s' % (a, c))
        return
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)


# Do test
if __name__ == "__main__":
    print(fact(5))
    move(4, 'A', 'B', 'C')


