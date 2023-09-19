# 多循环

"""
for x in range(1,10):
    print(x,end=" ")
print("")

for y in range(5):
    for x in range(1,10):
        print(x,end=" ")
    print()
    
"""

rows = int(input("rows:"))
cols = int(input("cols:"))
symbol = input("symbol:")

for i in range(rows):
    for j in range(cols):
        print(symbol,end=" ")
    print()
