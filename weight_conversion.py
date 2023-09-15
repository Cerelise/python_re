# python 体重转换器

weight = float(input("请输入你的体重："))
unit = input("你的体重是公斤还是磅？（kg/lb）").upper()

if unit == 'KG':
    weight *= 2.2
    new_unit = '磅'
elif unit == 'LB':
    weight /= 2.2
    new_unit = '公斤'
else:
    print('单位不正确')
    exit()

print(f'你的体重是 {round(weight)} {new_unit}')