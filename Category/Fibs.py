# Fibs modle
# encoding=utf-8

class Fibs(object):
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self): # 这里的环境是python3.x，如果是2.x的环境，那就是"next"方法名称啦
        self.a, self.b = self.b, self.a + self.b
        # 给迭代器设置终点值
        if self.a > 100000:
            raise StopIteration()
        return self.a

fib = Fibs()
for f in fib:
    print(f,end='\t')
    if f > 10:
        break
        
        
    
    