#-----------------------------------
# coding:   utf-8                  
# Author:   zhangwei               
# Time:     2019/11/27 10:10        
# Filename: Decorator.py                
#-----------------------------------
import time

def now():
    localtime = time.asctime(time.localtime(time.time()))
    print(localtime)

# 假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，
# 但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。

print(now.__name__)
