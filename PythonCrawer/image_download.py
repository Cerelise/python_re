import requests
from bs4 import BeautifulSoup
import os 

def download_img(url,save_path):
    print(f"正在下载图片：{url}")
    response = requests.get(url)
    with open(save_path,'wb') as file:
        file.write(response.content)
    print("-"*30)

def main():
    url = "https://www.ptt.cc/bbs/miHoYo/M.1695812737.A.47E.html"
    # headers = {"Cookie":"over18=1"}
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"html.parser")
    # print(soup.prettify())

    # comments = soup.find_all("span",class_="f3 push-content")
    # print(comments)

    spans = soup.find_all("span",class_="article-meta-value")
    title = spans[2].text
    # print(spans[2].text)

    # 建立一个图片文件夹
    dir_name = f"images/{title}"
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    # 找到网页中的所有图片
    # 1 通过遍历链接
    links = soup.find_all('a')
    allow_file_name = ["jpg","png","jpeg","gif"]
    for link in links:
        href = link.get("href")
        if not href:
            continue
        file_name = href.split("/")[-1]
        extension = href.split(".")[-1].lower()
        # print(extension)
        if extension in allow_file_name:
            print(f"file type:{extension}")
            print(f"url:{href}")
            download_img(href,f"{dir_name}/{file_name}")



# links = soup.find_all("img")
# for link in links:
#     src = link.get("src")
#     if not src:
#         continue
#     print(src)

if __name__ == "__main__":
    main()