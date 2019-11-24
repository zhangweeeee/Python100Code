# 列表生成式
import os
L = [x*x for x in range(1,10) if x%2 == 0]

print(L)

M = [m+n for m in 'abc' for n in '123']
print(M)

# 利用列表生成式，列出当前文件夹下的文件
N = [d for d in os.listdir('.')]
print(N)

# 利用列表生成式，生成lower()字符
O = ['Hello', 'World', 'IBM', 'Apple']
s = [k.lower() for k in O]
print(s)
