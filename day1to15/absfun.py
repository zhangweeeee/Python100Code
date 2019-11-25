#-----------------------------------
# coding:   utf-8                  
# Author:   zhangwei               
# Time:     2019/11/25 11:40        
# Filename: absfun.py                
#-----------------------------------

# 函数式编程：编写高阶函数，就是让函数的参数能够接收别的函数。
def add(x,y,fun):
    return fun(x)+fun(y)
m = add(-5,6,abs)

print(m)
