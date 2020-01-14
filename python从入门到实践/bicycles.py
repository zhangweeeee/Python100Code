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
#     Apple.append(product)
# print(Apple)

del motorcycles[0]
print(motorcycles)

pop_motorbicycles = motorcycles.pop();
print(pop_motorbicycles)

motorcycles.sort()
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)