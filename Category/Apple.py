# Apple modle
#encoding=utf-8
from Category.Fruit import Fruit

class Apple(Fruit):
    def __init__(self, name, size):
        super(Apple, self).__init__(name)
        self.size = size
    
    def getSize(self):
        return self.size
    
apple = Apple("apple", 12)

print(apple.getName())
print(apple.getSize())