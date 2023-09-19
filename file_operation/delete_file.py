import os,shutil
path = r"C:\Users\ALIENWARE\OneDrive\桌面\workspace"

# 删除文件
os.remove(f"{path}/TEST.txt")

# 删除空文件夹
os.rmdir(f"{path}/dirc")

# 删除文件夹及其内容
shutil.rmtree(f"{path}")

# 丢到回收站
import send2trash
send2trash.send2trash(fr"{path}\TEST.txt")