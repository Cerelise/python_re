str = r"C:\Users\ALIENWARE\OneDrive\桌面\test.txt"

try:
    with open(str) as file:
        print(file.read())
except FileNotFoundError:
    print("文件不存在")