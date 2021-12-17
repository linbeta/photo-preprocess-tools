import os
import numpy as np
from PIL import Image
import shutil

import imgaug as ia
from imgaug import augmenters as iaa

ia.seed(1)


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

# 用 pic_name 代入食材名稱/指定資料夾
pic_name = '28_sweet-potato'

if __name__ == "__main__":
    # 讀取圖片檔案路徑
    IMG_DIR = "D:\OneDrive\Learning\AI Class_TibaMe02\Team Project\\000_resize_224_square\\" + pic_name
    # 存檔路徑
    AUG_IMG_DIR = "D:\OneDrive\Learning\AI Class_TibaMe02\Team Project\\000_resize_224_square\\Augment_to_500\\" + pic_name + "_aug_500"
    try:
        shutil.rmtree(AUG_IMG_DIR)
    except FileNotFoundError as e:
        a = 1
    mkdir(AUG_IMG_DIR)

    # 設定要做Aug幾次，如果抓50張照片，做9次augmentation就可以得到500張了
    NUM = 84
    AUGLOOP = 5

    # 影像增强
    seq = iaa.Sequential([
        iaa.Flipud(0.5),  # vertically flip 20% of all images
        iaa.Fliplr(0.5),  # 镜像
        iaa.Multiply((1.2, 1.5)),  # change brightness, doesn't affect BBs
        iaa.GaussianBlur(sigma=(0, 3.0)),  # iaa.GaussianBlur(0.5),
        iaa.Affine(
            translate_px={"x": 15, "y": 15},
            scale=(0.8, 0.95),
            rotate=(-30, 30)
        )  # translate by 40/60px on x/y axis, and scale to 50-70%, affects BBs
    ])

    for root, sub_folders, files in os.walk(IMG_DIR):

        for i, name in enumerate(files[:NUM]):
            # print("i:", i)
            shutil.copy(os.path.join(IMG_DIR, name[:-4] + '.jpg'), AUG_IMG_DIR)

            for epoch in range(AUGLOOP):
                # print("epoch:", epoch)
                seq_det = seq.to_deterministic()
                # 读取图片
                img = Image.open(os.path.join(IMG_DIR, name[:-4] + '.jpg'))
                img = np.asarray(img)

                # 儲存變化後的圖片
                image_aug = seq_det.augment_images([img])[0]
                # 設定存檔的jpg檔案名稱數字規則：%06d指的是不滿6位數字的左邊補0
                num_gen = str("%06d" % int(i * 100 + epoch))
                path = os.path.join(AUG_IMG_DIR, pic_name + '.' + num_gen + '.jpg')

                Image.fromarray(image_aug).save(path)

                print(pic_name + '.' + num_gen + '.jpg')
