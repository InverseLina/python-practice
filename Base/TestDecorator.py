import functools

# encoding=utf-8
__author__ = 'Hinsteny'


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def now_one():
    print('2015-3-25')
    return "now_one"


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log('execute')
def now_two():
    print('2015-3-25')
    return "now_two"


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            print("begin call")
            result = func(*args, **kw)
            print("end call")
            return result
        return wrapper
    return decorator


@log('execute')
def now_three():
    print('2015-3-25')
    return "now_three"


def begin():
    print('begin call')


def end():
    print('end call')


def log(func):
    def test():
        def fu():
            print('exec function name: %s' % func.__name__)
            return func()
        return begin(), fu(), end()
    return test


@log
def fc():
    print('yes')
    return "fc"


# 偏函数，构造自定义默认参数的封装函数
def test_partial_function():
    def int8(x, base=8):
        return int(x, base)
    print(int8('123456'))
    int2 = functools.partial(int, base=2)
    print(int2('1000000'))


# Do test
if __name__ == "__main__":
    print(now_one())
    print(now_one.__name__)
    print(now_two())
    print(now_two.__name__)
    print(now_three())
    print(now_three.__name__)
    print(fc())
    print(test_partial_function())


