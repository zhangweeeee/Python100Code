#-----------------------------------
# coding:   utf-8                  
# Author:   zhangwei               
# Time:     2019/11/28 15:24        
# Filename: object.py                
#-----------------------------------

class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def get_score(self):
         return self.__score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

stu1  = Student('Tom', 98)
print(stu1.__name)