
import shutil

"""
copyfile 仅复制文件内容
copy 
copy2 全面，功能更强大
"""

path = r"C:\Users\ALIENWARE\OneDrive\桌面\workspace"
source = f"{path}/source_file.txt"
destination = f"{path}/destination_file.txt"
shutil.copyfile(source,destination)


