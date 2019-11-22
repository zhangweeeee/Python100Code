# 廖雪峰python 函数的默认参数
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

enroll('张三', '男')
enroll('张四', '男', 7, '天津')

# 可变参数
# 可变参数定义形式
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
num = [1,2,3,4,5,6,7]
# 可变参数传入list，*nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。
print(calc(*num))

# 关键字参数
def person1(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

print(person1('Adam', 45, gender='M', job='Engineer'))

# 限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数
# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错
def person(name, age, *, city, job):
    print(name, age, city, job)

print(person('Jack', 24, city='Beijing', job='Engineer'))

# 在Python中定义函数，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

# 小结
#
# Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。
#
# 默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
#
# 要注意定义可变参数和关键字参数的语法：
#
# *args是可变参数，args接收的是一个tuple；
#
# **kw是关键字参数，kw接收的是一个dict。
#
# 以及调用函数时如何传入可变参数和关键字参数的语法：
#
# 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
#
# 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
#
# 使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
#
# 命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
#
# 定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。