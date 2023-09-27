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
import json

url = "https://www.ptt.cc/bbs/NBA/index.html"

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}
response = requests.get(url,headers=headers)

soup = BeautifulSoup(response.text,"html.parser")
articles = soup.find_all("div",class_='r-ent')
data_list = []
for a in articles:
    data = {}
    title = a.find("div",class_="title")
    if title and title.a:
        title = title.a.text
    else:
        title = "没有标题"
    data["标题"] = title

    # 添加热度
    popular = a.find("div",class_="nrec")
    if popular and popular.span:
        popular = popular.span.text
    else:
        popular = "N/A"
    data["人气"] = popular

    # 日期
    date = a.find("div",class_="date")
    if date:
        date = date.text
    else:
        date = "N/A"
    data["日期"] = date
    data_list.append(data)
    # print(f"{popular} {title} {date}")
with open("ptt_nba_data.json","w",encoding="utf-8") as file:
    json.dump(data_list,file,ensure_ascii=False,indent=4)


