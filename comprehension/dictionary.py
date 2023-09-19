"""
字典推导式
dictionary = 
{ key:expression for key,value in iterable }
"""

# cities_in_F = { 'LA':120,'New Yorks':65,'Chicago':50,'Miami':150 }
# cities_in_c = { key:(value - 32) * 5 / 9 for key,value in cities_in_F.items()}

# print(cities_in_F)
# print(cities_in_c)

# weather = { "北京":"晴天","杭州":"晴天","长沙":"有雨","成都":"多云" }

# sunny_weather = { key:value for key,value in weather.items() if value == '晴天'}

# print(sunny_weather)


cities_in_f = { 'LA':120,'New Yorks':65,'Chicago':50,'Miami':150 }

def check_temp(value):
    if value >= 70:
        return '热'
    elif value >= 40:
        return '温暖'
    else:
        return '冷'

description_cities = { key:check_temp(value) for key,value in cities_in_f.items()}
print(description_cities)