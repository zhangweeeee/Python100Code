# day 7list 生成式和生成器

f = [x for x in range(1,10)]
print(f)
f = [x + y for x in 'ABCDE' for y in '1234567']
print(f)



 # yield 生成器
def fib(n):
    a, b = 0,1
    for x in range(n):
        a, b =  b ,a +b
        yield a     #yield关键字构造生成器

for x in fib(20):
    print(x)