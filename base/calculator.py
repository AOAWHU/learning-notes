# 加法器
'''
a = float (input("请输入第一个数字："))
b = float(input("请输入第二个数字："))

c = a + b

print(f"{a} + {b} = {c}")

'''

# 计算器 第一版
a = float (input("请输入第一个数字："))
b = float(input("请输入第二个数字："))


c = a + b

print(f"{a} + {b} = {c}")

d = a - b
print(f"{a} - {b} = {d}")

e = a * b
print(f"{a} * {b} = {e}")

if b != 0:
    f = a / b
    print(f"{a} / {b} = {f}")
else:
    print("除数不能为零！")
