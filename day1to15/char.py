# 廖雪峰python 字符串和编码
import sys
print(ord('A'))
print(ord('a'))
print(ord('中'))
print('\u4e2d\u6587')

x = b'ABCd'
y = 'ABCd'

print(len(x))
print(len(y))

p = ['asp','php']
s = ['java','c++',p,'scheme']

print(p[1])
print(s[2][0])