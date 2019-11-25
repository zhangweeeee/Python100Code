#-----------------------------------
# coding:   utf-8                  
# Author:   zhangwei               
# Time:     2019/11/25 14:14        
# Filename: map.py                
#-----------------------------------

# map和reduce高阶函数使用实例
def FUN(x):
    return x*x

r = list(map(FUN,[1,2,3,4,5,6,7,8,9,0]))

print(r)