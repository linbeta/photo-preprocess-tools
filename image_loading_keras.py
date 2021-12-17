"""
Keras有一些好用的function來處理圖片和numpy array的轉換
"""
import tensorflow as tf
from keras.preprocessing.image import load_img, img_to_array, array_to_img
# load image
img = load_img('pt1.jpg')
# img.show()
print("Original: ", type(img))

# convert image to np.array
img_array = img_to_array(img)
print(("NumPy array info: ", type(img_array)))
print("type:", img_array.dtype)
print("shape:", img_array.shape)

# convert np.array back to image
img_pil = array_to_img(img_array)
print("Convert back: ", img_pil)

"""
參考資料：https://www.pluralsight.com/guides/importing-image-data-into-numpy-arrays
"""
