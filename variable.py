name = "行心"      # 字符串
name1 = 'AWAHO'    # 字符串
age = 23           # 整数
height = 1.70      # 浮点数
is_student = False  # 布尔值

print(type(is_student))  # <class 'bool'>
print(type(height))       # <class 'float'>

num_str = '714'
num_int = int(num_str)
name_float = float(6.28) 
text = str(42)


# 变量练习
name = str(input("你的名字是："))
age = int(input("你的年龄是："))

print(f"你好，{name}!")
print(f"3年后你将{age + 3}岁。")
