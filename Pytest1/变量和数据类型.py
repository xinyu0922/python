
print ("hello word")


#变量打印
a="hello word"
print(a)


#首字母大写
name="ada lovelace"
print(name.title())

name="Ada Lovelace"
print(name.upper()) #全部大写
print(name.lower()) #全部小写

#拼接
first_name="ada"
last_name="lovelace"
full_name=first_name+" "+last_name
print(full_name)
print("hello,"+full_name.title()+"!")
message="hello,"+full_name+"!"
print(message)


#制表符
print("print")
print("\tprint") # + 空格
print("\nprint") #换行
print("languages:\n\tjava\n\tpython\n\tC")


lanuage="python "
print(lanuage)
print(lanuage.rstrip()) #去除末尾空格
lanuage=lanuage.rstrip()  #永久去除末尾空格
print(lanuage)


lanuage2=" pyhon "
print(lanuage2.rstrip()) #去除末尾空格
print(lanuage2.lstrip()) #去除开头空格
print(lanuage2.strip())  #去除2端空格


print(2+3)
print(3-2)
print(2*3)
print(4/2)

print(0.1+0.1)
print(0.2-0.1)
print(2*0.1)
print(2/0.1)
print(3/2)


#str类型
age=23
message="happy "+str(age)+"rd birthday"
print(message)



