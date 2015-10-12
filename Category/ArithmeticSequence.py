#encoding=utf-8
########################################################################
def checkIndex(key):
    """
    所给的键是能接受的索引吗？
    为了能被接受，键应该是一个非负的整数。如果它不是一个整数，会引发TypeError; 如果它是负数，则会引发IndexError(因为序列是无限长的)
    """
    if not isinstance(key, (int)): raise TypeError
    if key < 0: raise IndexError

class  ArithmeticSequence:
    """"""

    #----------------------------------------------------------------------
    def __init__(self, start = 0, step = 0):
        """
        初始化算术序列
        
        起始值------序列中的第一值
        步长-----两个相邻值之间的差别
        改变-----用户修改的值的字典
        """
        self.start = start
        self.step = step
        self.changed = {}
    def  __getitem__(self, key):
        """
        Get an item from the arithmetic sequence.
        """
        checkIndex(key)
        
        try: return self.changed[key]              #修改了吗？
        except KeyError:                                #否则...
            return self.start + key*self.step      #.......计算值
    
    def __setitem__(self, key, value):
        """
        修改算术序列中的一个项
        """
        checkIndex(key)
        self.changed[key] = value
    
# Test method
def test_ArithmeticSequence():
    s = ArithmeticSequence(1,2)
    print(s[4])
    s[4] = 2
    print(s[4])
    print(s[5])
    del s[4]
    s["four"]
    s[-3]

# Do test
if __name__ == "__main__":
        test_ArithmeticSequence()