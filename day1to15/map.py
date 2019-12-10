#-----------------------------------
# coding:   utf-8                  
# Author:   zhangwei               
# Time:     2019/11/25 14:14        
# Filename: map.py                
#-----------------------------------
from functools import reduce
# map和reduce高阶函数使用实例
def FUN(x):
    return x*x

r = list(map(FUN,[1,2,3,4,5,6,7,8,9,0]))

print(r)

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
#
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

def add(x,y):
    return x+y
m = reduce(add,[1,2,3,4,5])

print(m)