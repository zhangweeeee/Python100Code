#-----------------------------------
# coding:   utf-8                  
# Author:   zhangwei               
# Time:     2019/11/25 15:16        
# Filename: normalize.py                
#-----------------------------------
# 函数式编程
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(name):
    name = name.capitalize()
    return name

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)