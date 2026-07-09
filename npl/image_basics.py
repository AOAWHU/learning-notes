from PIL import Image
import numpy as np
import matplotlib
matplotlib.rcParams["font.family"] = "Noto Sans CJK SC"
import matplotlib.pyplot as plt


img = Image.open("text.jpg") #导入图片
arr = np.array(img)

print(f"图片尺寸: {img.size}")
print(f"数组形状: {arr.shape}")
print(f"数据类型: {arr.dtype}")
print(f"数据范围: {arr.min()} - {arr.max()}")
print(f"总元素数: {arr.size}")

img_resized = img.resize((256, 256))     # 缩放
img_gray= img.convert("L")               # 转灰度
img_rotated = img.rotate(45)             # 旋转45度
img_cropped = img.crop((0, 0, 100, 200 ))# 裁剪，左上右下，坐标原点在左上角

arr_flipped_ud = arr[::-1, :, :]
arr_flipped_lr = arr[:, ::-1, :]

img_flipped = img.transpose(Image.FLIP_LEFT_RIGHT) # 左右旋转

#用Numpy做通道分离
r, g, b, =arr[:, :, 0], arr[:, :, 1], arr[:, :, 2]
print(f"\n绿色通道: 均值{g.mean()}, 最大值{g.max()}")

#显示图片
fig, axes = plt.subplots(2, 3, figsize=(10, 7) )
axes[0, 0].imshow(img); axes[0, 0].set_title("原图")
axes[0, 1].imshow(img_resized); axes[0, 1].set_title("缩放 256×256")
axes[0, 2].imshow(img_rotated); axes[0, 2].set_title("旋转45°")
axes[1, 0].imshow(img_flipped); axes[1, 0].set_title("左右翻转")
axes[1, 1].imshow(img_gray, cmap="gray"); axes[1, 1].set_title("灰度")
# 只显示红色通道
axes[1, 2].imshow(r, cmap="Reds"); axes[1, 2].set_title("红色通道")

for ax in axes.flat:
    ax.axis("off")
plt.tight_layout()
plt.savefig("my-first-repo/npl/output_demo.png")  # 保存结果图
print("\n结果已保存为 output_demo.png")