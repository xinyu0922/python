# #[] 方括号表示列表元素
# bicycles=['trek','cannondale','redline','specialized']
# print(bicycles)
# print(bicycles[0]) #选取第一个
# print(bicycles[1]) #选取第二个
# print(bicycles[0].title()) #首字母大写
# message="My frist bicycle was a " + bicycles[0].title() + "."
# print(message)

# motorcycles=['honda','yamaha','suzuki']
# print(motorcycles)
# motorcycles[0]='ducati' #修改元素值
# print(motorcycles)

# motorcycles=['honda','yamaha','suzuki']
# motorcycles.append('ducati') #.appeng()在末尾添加元素
# print(motorcycles)

# motorcycles=[]
# motorcycles.append('honda') #在末尾添加元素
# motorcycles.append('yamaha')
# motorcycles.append('suzuki')
# print(motorcycles)

# motorcycles=['honda','yamaha','suzuki']
# motorcycles.insert(0,'ducati')  #.insert(0,'') 在列表的任何位置添加新元素
# print(motorcycles)

# motorcycles=['honda','yamaha','suzuki']
# del motorcycles[0]  #删除元素[] 方括号指定位置
# print(motorcycles)


# motorcycles=['honda','yamaha','suzuki']
# popped_motorcycles=motorcycles.pop() #.pop() 删除末尾元素 并让你能够继续使用它
# print(motorcycles) #删除末尾元素
# print(popped_motorcycles) #打印删除的元素

motorcycles=['honda','yamaha','suzuki']
last_motorcycles=motorcycles.pop()
print("The lasr motorcycles I owned was a "+last_motorcycles.title()+".")


