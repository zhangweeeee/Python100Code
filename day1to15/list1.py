# day07 python 常用数据结构 字符串、列表、元组、字典、集合

# 字符串
a, b = 5, 10
print(f'{a} * {b} = {a * b}') # 格式化

# 列表list

list = [1,2,3,4,5]


list = list + [100,200] # 合并
list.insert(0,300)      # 插入


print(list)
print(len(list))

list = [0,1,2,3,4,5,6,7,8,9]
print(list[1:4])   #左闭右开
print(list[::-1])  #可以通过反向切片操作来获得倒转后的列表的拷贝
list = ['123','234']
print(list)