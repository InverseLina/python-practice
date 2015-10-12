#encoding=utf-8
#fruit.py
import sys,pprint

class Fruit(object):
    
    def __init__(self, name = "name_fruit"):
        self.name = name
        
    def getName(self):
        return self.name


# Fruit test
def test():
    pprint. pprint(sys.path)
    f = Fruit("Test_fruit")
    name = f.getName()
    print(name)
    print("你好，世界！")
    
# Do test
if __name__ == "__main__":
    test()
