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