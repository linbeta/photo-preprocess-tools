import os
import cv2
import shutil

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


# 用ITEM來存哪個食材資料夾及檔名
ITEM = "52_cucumber"
# 設定圖片讀取路徑，該路徑下包含jpg格式的照片
DATADIR = f"D:\OneDrive\Learning\AI Class_TibaMe02\Team Project\original_files\\" + ITEM
# 設定存檔路徑
SAVE_DIR = "D:\OneDrive\Learning\AI Class_TibaMe02\Team Project\\000_resize_224_square\\" + ITEM
# 設定目標畫素大小，專案需一致，為32的倍數
IMG_SIZE = 224

# 使用os.path模組的join方法生成路徑
path = os.path.join(DATADIR)

# 檢查存檔路徑，如果不存在直接創一個
try:
    shutil.rmtree(SAVE_DIR)
except FileNotFoundError as e:
    a = 1
mkdir(SAVE_DIR)

'''使用os.listdir(path)函式，返回path路徑下所有檔案的名字，以及資料夾的名字，
例如，執行下行程式碼後，img_list是一個list，值為['0.jpg','1.jpg','10.jpg','11.jpg','12.jpg','13.jpg','14.jpg',
'2.jpg','3.jpg','4.jg', '5.jpg', '6.jpg', '7.jpg', 
'8.jpg', '9.jpg']，注意這個順序並沒有按照從小到大的順序排列'''
img_list = os.listdir(path)
# print(img_list)
ind = 1
for i in img_list:
    #呼叫cv2.imread讀入圖片，讀入格式為IMREAD_COLOR
    img_array = cv2.imread(os.path.join(path, i), cv2.IMREAD_COLOR)
    # print(img_array)
    try:
        y, x = img_array.shape[:2]
        y = int(y)
        x = int(x)
        # print(y//2, x//2)
        if y > x:
            img_array2 = img_array[(y//2 - x//2):(y//2 + x//2), :img_array.shape[1]]
            # cv2.imshow("1", img_array2)
        else:
            img_array2 = img_array[:img_array.shape[0], (x//2 - y//2):(x//2 + y//2)]
            # cv2.imshow("2", img_array2)

        '''呼叫cv2.resize函式resize圖片'''
        new_array = cv2.resize(img_array2, (IMG_SIZE, IMG_SIZE))
        # cv2.imshow('3', new_array)
        img_name = "_" + str(ind)+'.jpg'
        # 存檔路徑

        save_path = SAVE_DIR + "\\" + ITEM + img_name
    except:
        pass

    print(save_path)
    '''呼叫cv.2的imwrite函式儲存圖片'''
    # print(i)
    cv2.imwrite(save_path, new_array)

    ind = ind+1

# cv2.waitKey(0)
