#-----------------------------------
# coding:   utf-8                  
# Author:   zhangwei               
# Time:     2019/12/11 16:49        
# Filename: myturtle.py 
# Notes：               
#-----------------------------------
# 导入turtle包的所有内容:
from turtle import *

# 设置笔刷宽度:
width(4)

# 前进:
forward(200)
# 右转90度:
right(90)

# 笔刷颜色:
pencolor('red')
forward(100)
right(90)

pencolor('green')
forward(200)
right(90)

pencolor('blue')
forward(100)
right(90)

# 调用done()使得窗口等待被关闭，否则将立刻关闭窗口:
done()