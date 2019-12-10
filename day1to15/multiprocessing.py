#-----------------------------------
# coding:   utf-8                  
# Author:   zhangwei               
# Time:     2019/12/10 10:33        
# Filename: multiprocessing 
# Notes：多进程
#-----------------------------------

import os

print("Process %s start " % os.getppid())

pid = os.fork()

if pid ==0:
    print('I am child process %s  and my parent %s.'(os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
