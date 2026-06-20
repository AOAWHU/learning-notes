# 个人记账本-综合练习
DATA_FILE = "expenses.txt"
expenses = []

def load_expenses():
    # 从文件读取历史账目
    try:
        with open(DATA_FILE, "r", encoding = "utf-8") as f
            for line in f:
                line = line.strip()
                if not line:

                    continue
                # 格式：类别|金额|备注
                parts = line.split("|")
                expense = {
                    "category": parts[0],
                    "amount": float(parts[1]),
                    "note": parts[2]
                }
                expenses.append(expense)
        print(f"📂已加载{len(expenses)}条历史记录. \n")
    except FileNotFoundError:
        print("没有找到历史文件，从空白开始记账. \n")

def save_expenses():
    # 把账目写入到文件
    with open (DATA_FILE, "w", encoding = "utf-8")as f:
        for exp in expenses: 
            line = f"{exp["category"]}|{exp["amount"]}|{exp["note"]}\n"
            f.write(line)
    print(f"💾已保存{len(expenses)}条记录到{DATA_FILE}")



