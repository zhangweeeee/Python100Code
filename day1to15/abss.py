# 函数式编程
def add(x,y,fun):
    return fun(x)+fun(y)
m = add(-5,6,abs)

print(m)
