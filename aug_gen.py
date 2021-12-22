import os
import numpy as np
from PIL import Image
import shutil
from matplotlib import pyplot as plt
from keras.preprocessing.image import ImageDataGenerator

def mkdir(path):
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        print(path + ' 創建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 路徑已存在')
        return False



def augment(dir_name, DIR):
    # 讀取圖片檔案路徑
    IMG_DIR = DIR + dir_name
    # 設定存檔路徑
    AUG_IMG_DIR = "D:\OneDrive\Learning\AI Class_TibaMe02\Team Project\\1222_Aug\\" + dir_name + "_aug"
    try:
        shutil.rmtree(AUG_IMG_DIR)
    except FileNotFoundError as e:
        a = 1
    mkdir(AUG_IMG_DIR)

    print(IMG_DIR)

    photos = os.listdir(IMG_DIR)
    print(photos)
    # 設定要做Aug幾次，抓大約作出1000張照片
    NUM = 500 // len(photos)
    print(f"NUM: {NUM}")
    # 定義相關參數
    datagen = ImageDataGenerator(
        rotation_range=10,
        zoom_range=0.5,
        horizontal_flip=True,
        fill_mode='nearest'
    )

    for i, name in enumerate(photos):
        print("i:", i)
        # 複製一張原圖
        shutil.copy(os.path.join(IMG_DIR, name), AUG_IMG_DIR)
        img = Image.open(os.path.join(IMG_DIR, name))
        img = np.asarray(img).reshape(1, 224, 224, 3)
        j = 0
        for batch in datagen.flow(img, batch_size=10, save_to_dir=AUG_IMG_DIR,
                                  save_prefix=dir_name, save_format='jpg'):
            plt.subplot(5,4,1 +j)

            aug_image = batch[0]
            aug_image = aug_image.astype('float32')
            aug_image /= 255
            plt.imshow(aug_image)
            j += 1
            if j > NUM:
                break


# 用 pic_name 代入食材名稱/指定資料夾
KEY_DIR = "D:\OneDrive\Learning\AI Class_TibaMe02\Team Project\\resize_224_square_65_classes\\"
all_directories = os.listdir(KEY_DIR)
# print(len(all_directories))
for name in all_directories[:3]:
    augment(name, KEY_DIR)

