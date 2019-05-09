[] 方括号表示列表元素
bicycles=['trek','cannondale','redline','specialized']
print(bicycles)
print(bicycles[0]) #选取第一个
print(bicycles[1]) #选取第二个
print(bicycles[-1]) #选取最后一个
print(bicycles[0].title()) #首字母大写
message="My frist bicycle was a " + bicycles[0].title() + "."
print(message)

motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[0]='ducati' #修改元素值
print(motorcycles)

motorcycles=['honda','yamaha','suzuki']
motorcycles.append('ducati') #.appeng()在末尾添加元素
print(motorcycles)

motorcycles=[]
motorcycles.append('honda') #在末尾添加元素
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles=['honda','yamaha','suzuki']
motorcycles.insert(0,'ducati')  #.insert(0,'') 在列表的任何位置添加新元素
print(motorcycles)

motorcycles=['honda','yamaha','suzuki']
del motorcycles[0]  #删除元素[] 方括号指定位置
print(motorcycles)


motorcycles=['honda','yamaha','suzuki']
popped_motorcycles=motorcycles.pop() #.pop() 删除末尾元素 并让你能够继续使用它
print(motorcycles) #删除末尾元素
print(popped_motorcycles) #打印删除的元素

motorcycles=['honda','yamaha','suzuki']
last_motorcycles=motorcycles.pop()
print("The lasr motorcycles I owned was a "+last_motorcycles.title()+".")

motorcycles=['honda','yamaha','suzuki']
first_owned=motorcycles.pop(0)  #删除制定位置的元素
print('The first motorcycle I owned was a '+first_owned.title()+'.')

del 删除法是永久删除，不在使用。pop是删除后继续可使用


motorcycles = ['honda', 'yamaha', 'suzuki','ducati']
motorcycles.remove('ducati') # remove（）删除指定值 也可是使用这值
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki','ducati']
too_expensive='ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA "+too_expensive.title()+"is too expensive for me.") #\n  换行

cars=['bwn','audi','toyota','subaru']
cars.sort() # .sort() 按照字母大小排列
print(cars)

cars=['bwn','audi','toyota','subaru']
cars.sort(reverse=True)   # reverse=True 字母倒序排列 T 必须大写
print(cars)

cars=['bwn','audi','toyota','subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the original list:")
print(sorted(cars))   #sorted() 按照特定的顺序显示列表元素，同时不影响它们在列表中原始的排列

print("\nHere is the original list:")
print(cars)

cars=['bwn','audi','toyota','subaru']
cars.sort(reverse=True)
print(sorted(cars,reverse=True)) #倒序临时排序


cars=['bwn','audi','toyota','subaru']
cars.reverse()  #.reverse() 反转列表元素排序，不是按照字母倒序排序
print(cars)

cars=['bwn','audi','toyota','subaru']
len(cars)  # len() 确认元素个数
print(len(cars))
