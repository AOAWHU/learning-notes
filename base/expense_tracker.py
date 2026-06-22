# 个人记账本-综合练习
DATA_FILE = "/home/xingxin/project/my-first-repo/base/expenses.txt"
expenses = []

def load_expenses():
    # 从文件读取历史账目
    try:
        with open(DATA_FILE, "r", encoding = "utf-8") as f:
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
            line = f"{exp['category']}|{exp['amount']}|{exp['note']}\n"
            f.write(line)
    print(f"💾已保存{len(expenses)}条记录到{DATA_FILE}")

def add_expense():
    # 录入一笔新帐目
    category = input("类别: ")
    amount_str = input("金额")
    try:
        amount = float(amount_str)
    except ValueError:
        print("金额无效, 已跳过. \n")
        return
    
    if amount <= 0:
        print("金额必须大于零. \n")
        return
    
    note = input("备注")

    expense = {
        "category": category if category else "其他",
        "amount": amount,
        "note": note if note else "无备注"
    }
    expenses.append(expense)
    print(f"已记录: {expense['category']} {expense['amount']}元\n")    

def view_expenses():
    #展示所有账目
    if not expenses:
        print("还没有任何记录。\n")
        return

    print(f"\n  {'序号':<5}{'类别':<8}{'金额':<10}{'备注'}")
    print("  " + "-" * 40)

    for i, exp in enumerate(expenses, 1):
        print(f"  {i:<5}{exp['category']:<8}{exp['amount']:<10.2f}{exp['note']}")

    print()

def summary():
    """按类别统计消费"""
    if not expenses:
        print("还没有任何记录。\n")
        return

    
    totals = {}
    for exp in expenses:
        cat = exp["category"]
        if cat in totals:
            totals[cat] += exp["amount"]   
        else:
            totals[cat] = exp["amount"]

    total_all = 0
    print(f"\n  {'类别':<10}{'合计':<10}{'占比'}")
    print("  " + "-" * 35)

    for cat, amount in totals.items():     
        total_all += amount

    
    for cat, amount in totals.items():
        percent = amount / total_all * 100 if total_all > 0 else 0
        bar = "█" * int(percent / 5)       # 简易进度条
        print(f"  {cat:<10}{amount:<10.2f}{bar} {percent:.1f}%")

    print(f"\n总计: {total_all:.2f} 元\n")

def main():
    """主程序"""
    print("=" * 40)
    print("个人记账本 v1.0")
    print("=" * 40)

    load_expenses()   # 启动时加载文件

    #  while 循环 —— 让程序一直跑
    while True:
        print("┌─────────────────────────┐")
        print("│  1. 记一笔账            │")
        print("│  2. 查看所有记录        │")
        print("│  3. 按类别汇总          │")
        print("│  4. 保存并退出          │")
        print("└─────────────────────────┘")

        choice = input("请选择 (1-4): ")   

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            summary()
        elif choice == "4":
            save_expenses()
            print("再见！")
            break                           
        else:
            print("无效选择，请输入 1-4\n")


# 启动
main()