import glob
import os

# 批次改檔名的小工具：
# DATADIR 為檔案路徑，注意需要全英文
DATADIR = "D:\OneDrive\Learning\AI Class_TibaMe02\Team Project\\1214_5_classes\\56_loofah"
# 在原檔名前面加上名稱
PRE = "/loofah_"

path = os.path.join(DATADIR)

img_list = os.listdir(path)
for file_name in img_list:
    # 指定新舊檔名規則：
    old_file = DATADIR + "/" + file_name
    rename_file = DATADIR + PRE + file_name
    os.rename(old_file, rename_file)
