str = r"C:\Users\ALIENWARE\OneDrive\桌面\TEXT.txt"

# text = 'hi\nworld'
"""
 w write 只写  使用它原本的文件内容将会被覆盖
 a       写入
"""
with open(str,'a') as file:

    file.write('\n go go go')
