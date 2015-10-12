# File modle
#encoding=utf-8
import sys,pprint
import os
import string
from Category.Apple import Apple

########################################################################
class  File:
    """
    文件工具类，包含一些常用的文件，文件夹操作方法
    """
    #----------------------------------------------------------------------
    def __init__(self, path):
        self.currentUrl = os.getcwd()
        if os.path.exists(path):
            if os.path.isfile(path):
                self.operateUrl = os.path.split(path)[0]
                print(self.operateUrl)
            elif os.path.isdir(path) :
                self.operateUrl = path
        else :
            raise Exception("Here has a error!")
        
    
    #类实例的方法 
    def changeFileExtension(self, oldEx, newEx):  
        File.ChangeFileExtension(self.operateUrl, oldEx, newEx)
        
    #类方法          
    @classmethod  
    def class_foo(cls, flag):  
        print("executing class_foo({0}) and flag {1}".format(cls, flag))
    
    #类的静态方法修改特定文件夹下的文件后缀名，采用递归的方法哈
    @staticmethod
    def  ChangeFileExtension(path, oldEx, newEx):
        ChangeFileExtension(path, oldEx, newEx)
        
#模块的静态方法修改特定文件夹下的文件后缀名，采用递归的方法哈
def  ChangeFileExtension(path, oldEx, newEx):
    if os.path.exists(path):
        if os.path.isfile(path):
            fileName,ex = path.split('.' , maxsplit=1)
            if oldEx == ex:
                os.replace(path, ".".join([fileName, newEx]))
        elif os.path.isdir(path) :
            for fileName in os.listdir(path):
                ChangeFileExtension(os.path.join(path,  fileName), oldEx, newEx)
    else :
        raise Exception("Here has a error!")        

        
    
    
# File test
def test():
    pprint. pprint(sys.path)
    file = File(r"E:\MobileFile\icon.jpeg")
    file.changeFileExtension("web.png", "png")
    print(file.currentUrl)
    print(file.operateUrl)
    file.class_foo("love")
    
# Do test
if __name__ == "__main__":
    test()