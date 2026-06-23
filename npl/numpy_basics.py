import numpy as np
#创建数组
arr = np.arange(1,13).reshape(3, 4)
print(arr)

#切片
print("\n第一行: ", arr[0,:])
print("第三列: ", arr[:, 2])

#运算
print("\n每个元素的平方: ", arr ** 2)
print("\n最大值", arr.max())
print("平均值", arr.mean())
print("每行平均值", arr.mean(axis=1))
print("每列最大值", arr.max(axis=0))

#
print("每列减去该列最小值", arr - arr.min(axis=0))