# 求阶乘


def fun(num):
    result = 1
    for x in range(1 , num+1):
        result *= x
    return result


print(fun(5))


# 可变参数

def add(*args):
    total = 0
    for val in args:
        total += val
    return total


print(add(1, 2, 3, 4, 5))

def is_prime(num):
    """判断一个数是不是素数"""
    for factor in range(2, num):
        if num % factor == 0:
            return False
    return True if num != 1 else False

print(is_prime(1))

def foo():
    global a
    a = 200
    print(a)  # 200


if __name__ == '__main__':
    a = 100
    foo()
    print(a)  # 200