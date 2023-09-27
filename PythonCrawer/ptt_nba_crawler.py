"""
爬虫的流程

- 确定要从网页中爬取哪些资料
- 分析html 提取数据
- 用Python编写爬虫
- 储存成结构化资料 json xls...

- requests 下载网页
- BeautifulSoup 解析网页，获得数据
"""

import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/NBA/index.html"

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}
response = requests.get(url,headers=headers)

# if response.status_code == 200:
#     with open('output.html','w',encoding='utf-8') as f:
#         f.write(response.text)
#     print("写入成功")
# else:
#     print("没有获取到网页")

soup = BeautifulSoup(response.text,"html.parser")
articles = soup.find_all("div",class_='r-ent')
for a in articles:
    title = a.find("div",class_="title")
    if title and title.a:
        title = title.a.text
    else:
        title = "没有标题"
   

    # 添加热度
    popular = a.find("div",class_="nrec")
    if popular and popular.span:
        popular = popular.span.text
    else:
        popular = "N/A"

    # 日期
    date = a.find("div",class_="date")
    if date:
        date = date.text
    else:
        date = "N/A"

    print(f"{popular} {title} {date}")


"""
  反爬虫：
  - 检查请求的Header
  - 输入验证码
  - 滑动解锁
"""