"""
基本影像處理練習，每個區塊可以註解/反註解依序看
"""
from PIL import Image

# 使用PIL套件來讀取和顯示照片
img = Image.open('pt1.jpg')
print(img.format)
print(img.mode)
print(img.size)
img.show()

# 使用matplotlib套件來讀讀取和顯示照片
from matplotlib import image, pyplot

image = image.imread('pt1.jpg')
print(image.dtype)
print(image.shape)
# 本機端除了讀圖片也要用pyplot.show()讓圖片在新視窗開啟
pyplot.imshow(image)
pyplot.show()

'''用NumPy裡面的array來將圖片轉為numpy array'''
import numpy as np

# 轉成numpy.ndarray
data = np.array(img)
print(type(data))
print(data.shape)

# 把ndarray轉回圖片
img_2 = Image.fromarray(data)
print(type(img_2))
print(img_2.mode)
print(img_2.size)
# 開啟照片
img_2.show()

# 裁切圖片
print("原始檔:", data.shape)
img_trim = data[150:650, 750:1250]
print("處理後:", img_trim.shape)
Image.fromarray(img_trim).show()

