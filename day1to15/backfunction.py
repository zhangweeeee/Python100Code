#-----------------------------------
# coding:   utf-8                  
# Author:   zhangwei               
# Time:     2019/11/26 10:11        
# Filename: backfunction.py                
#-----------------------------------

# 返回函数,高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    # 当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数：
    return sum
f2 = lazy_sum(1,3,5,7,9)
# 调用函数f时，才真正计算求和的结果：
print(f2())


# 闭包
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs
# fs是可以迭代的，所以可以如下赋值形式（暂时未找到资料，个人理解）
f1, f2, f3 = count()
print(f1(),f2(),f3())
# 全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。

# 一个函数可以返回一个计算结果，也可以返回一个函数。
#
# 返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量