bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)
print(bicycles[0].title())
print(bicycles[-1]) #倒数第一个元素

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[1] = 'ducati'

print(motorcycles)

motorcycles.append('BMW')
print(motorcycles)

#
# i = 0
# Apple = []
# while i<3:
#     i = i + 1
#     product  = input()
#     Apple.append(product)   #添加
# print(Apple)

del motorcycles[0]  #删除
print(motorcycles)

pop_motorbicycles = motorcycles.pop()  #弹出
print(pop_motorbicycles)

motorcycles.sort() #永久性改变了列表元素的顺序
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']
print(sorted(motorcycles))
