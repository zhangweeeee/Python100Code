#-----------------------------------
# coding:   utf-8                  
# Author:   zhangwei               
# Time:     2019/12/2 10:00        
# Filename: usingproperty.py                
#-----------------------------------

class Student(object):

  @property
  def score(self):
      return self._score

  @score.setter
  def score(self,value):
      if not isinstance(value,int):
          raise ValueError('score must be a integer')
      if value < 0 or value > 100:
        raise ValueError('score must between 0 ~ 100!')
        self._score = value
