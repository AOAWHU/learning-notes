# 猜数字游戏
import random

target = random.randint(1, 100)
guess = int(input("请猜一个1-100之间的数字: "))

if guess == target:
    print("答对了！")
elif guess < target:
    print(f"你猜的数字太小了! 正确答案是{target}. ")
else:
    print(f"你猜的数字太大了! 正确答案是{target}. ")

# BMI计算器
height = float(input("请输入您的身高(m)"))
weight = float(input("请输入您的体重(kg)"))
bmi = weight / (height ** 2)
print(f"您的BMI为{bmi: .2f}")

if bmi < 18.5:
    print("体重过轻")
elif 18.5 <= bmi < 24.9:
    print("正常范围")
elif 24.9 <= bmi < 29.9:
    print("超重")
else:
    print("肥胖")