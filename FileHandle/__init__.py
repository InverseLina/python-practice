#encoding=utf-8
import sys
import os
currentUrl = os.path.dirname(__file__)
parentUrl = os.path.abspath(os.path.join(currentUrl, os.pardir))
print(parentUrl)

#把某个文件夹路径添加到path下，以引入该目录下的模块
sys.path.append(parentUrl)