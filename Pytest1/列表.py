# #列表是从0开始数，-1表示最后一个
# bicycles=['reck','cannondale','redline','specialized']
# print(bicycles[0])
# print(bicycles[1])
# print(bicycles[3])
# print(bicycles[0].title())
# print(bicycles[-1])
# print(bicycles[-2])
#
# message="My frist bicycle was a "+bicycles[0].title()+"."
# print(message)
#
# #更改列表
# motorcycles=['honda','yamaha',"suzuki"]
# print(motorcycles)
# motorcycles[0]='ducati'
# print(motorcycles)
#
#
# #在末尾添加元素 append()
# motorcycles=['honda','yamaha',"suzuki"]
# motorcycles.append('ducati')
# print(motorcycles)

# motorcycles=[]
# motorcycles.append('honda')
# motorcycles.append('yamaha')
# motorcycles.append('suzuki')
# print(motorcycles)
#
# #插入新元素 insert()
# motorcycles=['honda','yamaha',"suzuki"]
# motorcycles.insert(0,'ducati')
# print(motorcycles)

# #删除元素 del
# motorcycles=['honda','yamaha',"suzuki"]
# del motorcycles[0]
# del motorcycles[1]
# print(motorcycles)


# #删除末尾元素 pop()
# motorcycles=['honda','yamaha',"suzuki"]
# popped_mototcycles=motorcycles.pop()
# print(motorcycles)
# print(popped_mototcycles) #删除的元素还是可以找到

# motorcycles=['honda','yamaha',"suzuki"]
# last_owned=motorcycles.pop()
# print("The last motorcycles I owend was a "+last_owned.title()+'.')
#
# #可以指定要删除位置的元素
# motorcycles=['honda','yamaha',"suzuki"]
# first_owned=motorcycles.pop(1)
# print("The last motorcycles I owend was a "+first_owned.title()+'.')


# #根据值删除元素remove()
# motorcycles=['honda','yamaha',"suzuki"]
# motorcycles.remove('yamaha')
# print(motorcycles)

#指定值删除后还可以使用
motorcycles=['honda','yamaha',"suzuki"]
too_expensive="yamaha"
motorcycles.remove('yamaha')
print(motorcycles)
print("\nA "+too_expensive.title()+" is too expensive for me")


112








