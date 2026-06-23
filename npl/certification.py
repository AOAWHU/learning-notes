import numpy as np

# 从列表创建
a = np.array([1, 2, 3, 4, 5])
print(a)  # [1 2 3 4 5]

# 全零、全一
zeros = np.zeros((3, 4))
ones = np.ones((2, 5))

# 指定范围
arr = np.arange(0, 10, 2)    # [0 2 4 6 8]

# 随机数
rand_arr = np.random.rand(3, 3)  # 3×3，0到1之间

img = np.zeros((224, 224, 3))  # 模拟一张图片：224×224 像素，3 通道
print(img.shape)   # (224, 224, 3)
print(img.dtype)   # float64
print(img.ndim)    # 3（三维）
print(img.size)    # 224×224×3 = 150528

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr[0, 0])      # 1
print(arr[1, :])      # 第2行：[4 5 6]
print(arr[:, 2])      # 第3列：[3 6 9]
print(arr[:2, :2])    # 左上角2×2


a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)      # [5 7 9]
print(a * b)      # [4 10 18]
print(a.mean())   # 2.0
print(a.max())    # 3
print(a.sum())    # 6

arr = np.arange(1, 13).reshape(3, 4)
print(arr)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]