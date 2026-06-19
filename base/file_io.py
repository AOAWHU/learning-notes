# 1.写入文件
scores= [
    "zhangsan, 85,90,78",
    "lisi, 92,88,95",
    "wangwu, 76,33,24",
]

with open("my-first-repo/base/scores.csv", "w", encoding= "utf-8") as f:
    f.write("name, yuwen, math, english\n")
    for line in scores:
        f.write(line + "\n")
print("已写入 scores.csv")

# 一次性读取全部内容
with open("my-first-repo/base/scores.csv", "r", encoding = "utf-8")as f:
    content = f.read()
    print(content)
'''
# 逐行读取
with open("scores.csv", "r", encoding = "uft-8")as f:
    for line in f:
        print(line.strip()) #strip()去掉换行符
'''
# 读取并计算每个人的平均分
with open("my-first-repo/base/scores.csv", "r", encoding = "utf-8")as f:
    next(f) #跳过表头
    for line in f:
        name, *scores_strs = line.strip().split(",")
        score_nums = [int(s) for s in scores_strs]
        avg = sum(score_nums) / len(score_nums)
        print(f"{name}:{score_nums},平均分{avg:.1f}")