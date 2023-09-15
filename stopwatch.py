from time import sleep

my_time = int(input("请输入秒数："))

for x in range(my_time,0,-1):
    # 02:00
    second = x % 60
    minutes = x // 60 % 60
    sleep(1)
    print(f"{minutes:02}:{second:02}",end=" ")

print("时间到")