# 关键字参数

def hello(greeting,title,first_name,last_name):
    print(f"{greeting},{title}:{first_name} {last_name}")

# hello("你好！","Mr","Cerelise","Wong")
# hello(greeting="你好！",title="Mr",first_name="Cerelise",last_name="Wong")

def set_phone(country_code,area_code,first,last):
    return f"{country_code}-{area_code}-{first}-{last}"

str = set_phone(country_code="886",area_code="02",first="1234",last="5678")
print(str)