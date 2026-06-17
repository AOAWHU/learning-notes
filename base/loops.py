'''
# 9 * 9 乘法表(顺序打印)
print("9 * 9 乘法表:")
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j} * {i} = {i * j}", end = "\t")
    print() #换行
print() #换行    
# 9 * 9 乘法表(倒序打印)
print("9 * 9 乘法表(倒序打印):")
for i in range(9, 0, -1):
    for j in range(1, i + 1):
        print(f"{j} * {i} = {j * i}", end = "\t")
    print() #换行 
print() #换行    

'''
# 猜数字游戏

'''


'''
#猜数字加强版（用户可以多次猜测，直到猜对为止）
'''
import random
target = random.randint(1, 10)
guess = input("请猜一个1-10之间的数字: ")

while guess != target:
    guess = int(input("请继续猜: "))
print(f"答对了！,正确答案是{target}. ")
'''
#猜数字加强版1.1版（用户可以多次猜测，根据提示直到猜对为止，并统计猜测的次数）
import random
target = random.randint(1, 10)
guess = int(input("请猜一个1-10之间的数字: "))
count = 1
while target != guess:
    
    if guess < target:
        print("你猜的数字太小了!")
    elif guess > target:
     print("你猜的数字太大了!")

    guess = int(input("请继续猜: "))
    count += 1
print(f"答对了！,正确答案是{target}. 你总共猜了{count}次.")