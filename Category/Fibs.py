#Fibs modle
#encoding=utf-8
########################################################################
class Fibs:
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        self.a = 0
        self.b = 1
    def next(self):
        self.a, self.b = self.b, self.a + self.b
        return self.b
    def __iter__(self):
        return self


fibs = Fibs()
print(fibs.next())
for f in fibs:
    if f > 1000:
        print(f)
        break
        
        
    
    