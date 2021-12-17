# 使用說明

main.py讀取檔名已中心切成正方形後resize
```buildoutcfg
# 用ITEM來存哪個食材資料夾及檔名
ITEM = "28_sweet-potato"
DATADIR = f"D:\OneDrive\Learning\AI Class_TibaMe02\Team Project\original_files\\" + ITEM
# 設定存檔路徑
SAVE_DIR = "D:\OneDrive\Learning\AI Class_TibaMe02\Team Project\\000_resize_224_square\\" + ITEM
# 設定目標畫素大小，專案需一致，為32的倍數
IMG_SIZE = 224
```


augmentation.py讀取resize過後的資料夾，設定需要讀幾張照片、做幾次aug
```buildoutcfg
# 用 pic_name 代入食材名稱/指定資料夾
pic_name = '28_sweet-potato'
```
47-49行
```buildoutcfg
# 設定要做Aug幾次，如果抓50張照片，做9次augmentation就可以得到500張了
NUM = 84
AUGLOOP = 5
```
