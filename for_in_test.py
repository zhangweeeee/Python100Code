"""
用for循环实现0~100求和
day04循环
"""
sum = 0
for x in range(101):
    presum = sum
    sum += x
    print(sum , "=" , presum , "+" , x)
