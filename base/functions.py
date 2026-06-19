'''函数的定义格式
def 函数名(参数):
    """文档字符串：说明这个函数干什么"""
    # 函数体
    return 结果
'''
# 质数判断
def determine_prime(n: int) -> bool:
    count = 0
    if n < 2:
        print(f"{n}不是质数")
        return False
       
    elif n > 2:
        for i in range(3, int(n ** 0.5) + 1):
            if n % i == 0:
                print(f"{n}不是质数")
                count += 1
                return False
    else:
        print(f"{n}是质数")
        return True

# 生成质数列表
def generate_prime(m:int, n:int) -> list:
    primes_list = []
    if m > n:
        m, n = n, m
    
    for i in range(m, n+1):
        if i < 2:
            continue
        else:
            for j in range(2, int(i ** 0.5 + 1)):
                if i % j == 0:
                    break
            else:
                    primes_list.append(i)
    return primes_list


# 计算器函数
'''
def calculator (a, b, operator):
    if operator == '+' :
        c = a + b
    elif operator == '-' :
        c = a - b
    elif operator == '*' :
        c = a * b
    elif operator == '/' and b != 0  :
        c = a / b
    else:
        c = None
    return c

'''
#计算器函数第二版, 优化掉中间变量c, 改进错误提示.
def calculator(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            return "错误：除数不能为零"
        return a / b
    else:
        return "错误：不支持的运算符"


# main()
'''
#生成质数列表
primes = generate_prime(1, 100)
print(primes)
print(f"共有{len(primes)}个")
'''              
# 简易计算器    
d = calculator(8, 3, '/')
print(round(d, 2))
print(f"{d:.2f}")





    