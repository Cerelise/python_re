# 文件搜索

import os

str = r"C:\Users\ALIENWARE\OneDrive\桌面"
# str = "C:\\Users\\ALIENWARE\\OneDrive\\桌面"
print(str)

# exists
# if os.path.exists(str):
#     print("路径存在！")
# else:
#     print("路径不存在！")

if os.path.isfile(str):
    print("该路径为文件！")
elif os.path.isdir(str):
    print("路径为目标！")
else:
    print("其他")