# 求阶乘


def fun(num):
    result = 1
    for x in range(1 , num+1):
        result *= x
    return result


print(fun(5))
