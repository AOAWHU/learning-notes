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
