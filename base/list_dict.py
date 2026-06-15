# 创建列表
matrix1_3 = [4, 6, 2.5]
phone = ['iPhone', 'Xiaomi', 'Huawei']
Hybrid = [1, 'Xingxin', 3.14, '苹果', True]

## 访问列表元素 list_name[顺序]
print(phone[0])
print(matrix1_3[1])
print(Hybrid[-1])

## 增删改 .append() .remove() 
phone.append('OPPO')
phone.append('Vivo')
print(phone)
phone.remove('Huawei')
print(phone)




# 字典
student = {
    'name': 'Xingxin',
    'age': 23,
    'major': 'Computer Science',
    'scores': [92, 93, 95]
}
#取值
print(student['name'])
print(student['scores'][0])
#修改
student['age'] = 24
print(student['age'])
#添加
student['graduated'] = True
print(student)
#删除
del student['major']

#遍历
for key, value in student.items():
    print(f"{key}: {value}")



# 通讯录练习
contacts = []  # 空列表，准备装多个联系人

# 添加联系人
contacts.append({"name": "张三", "phone": "13800138000", "city": "北京"})
contacts.append({"name": "李四", "phone": "13900139000", "city": "上海"})
contacts.append({"name": "王五", "phone": "13700137000", "city": "广州"})

# 显示所有联系人
print("===== 通讯录 =====")
for person in contacts:
    print(f"姓名：{person['name']}，电话：{person['phone']}，城市：{person['city']}")

# 查询功能
search = input("\n输入要查询的名字：")
found = False
for person in contacts:
    if person["name"] == search:
        print(f"找到了！电话：{person['phone']}，城市：{person['city']}")
        found = True
        break

if not found:
    print(f"未找到{search}")