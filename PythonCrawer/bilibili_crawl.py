"""
 - 访问网站
 - 返回HTML(空白页面)
 - JS发出Ajax请求
 - 服务器返回数据，JS渲染页面
"""

import requests
import pandas as pd

url = "https://app.bilibili.com/x/topic/web/dynamic/rcmd?source=Web&page_size=9"
headers = {
  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
  'Cookie':"buvid3=29F3B911-79E8-4E64-BDED-2024905C3AA8167613infoc; LIVE_BUVID=AUTO8416298657231611; CURRENT_BLACKGAP=0; buvid4=C2F997C5-D3AA-D32E-447E-01446BA4FAC922861-022012119-693OIUdrVYCxGUYRtt9kwQ%3D%3D; buvid_fp_plain=undefined; DedeUserID=15689358; DedeUserID__ckMd5=4971d58f09e69c6d; b_nut=100; rpdid=|(um~lJumkYu0J'uYY)lmJYl~; header_theme_version=CLOSE; i-wanna-go-feeds=-1; i-wanna-go-back=-1; b_ut=5; is-2022-channel=1; hit-new-style-dyn=1; CURRENT_PID=6e24cf70-ce38-11ed-9460-af5c768951e9; CURRENT_QUALITY=80; FEED_LIVE_VERSION=V8; hit-dyn-v2=1; nostalgia_conf=-1; CURRENT_FNVAL=4048; SESSDATA=25664a0c%2C1707154564%2C86893%2A82TxsO9_PUcLHiVuyg8l0mbsE-itPgCKoT03HuAS3CGm8zhn7xOCYrNt7J0PQHrtAVacYb2AAAOgA; bili_jct=25df5ba026861d63b7c4e6744a216fb7; _uuid=FBD75EC9-577D-8D18-2E66-710D86BDA4210864544infoc; fingerprint=ce88fef1736a4cbdf6d8f38ce80ab7c7; sid=4hfkrb0x; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTU5MTI1NDAsImlhdCI6MTY5NTY1MzI4MCwicGx0IjotMX0.KwtFpLG_67iz-xlfUIQ_bx5Se5FmB3KBWdLifIf0390; bili_ticket_expires=1695912480; buvid_fp=397f2638200f56c8c99b5d2e2c803998; PVID=1; b_lsid=6A93DDB7_18AD6BC5C52; innersign=0; bp_video_offset_15689358=846035804884041785"
}

response = requests.get(url,headers=headers)
if response.status_code == 200:
    data = response.json()
    # print(data)
    topics = data['data']['topic_items']
    topic_list = []
    for topic in topics:
        # topic_data = {
        #   'title':topic['name'],
        #   'view':topic['view'],
        #   'discuss':topic['discuss']
        # }
        topic_data = [
          topic['name'],
          topic['view'],
          topic['discuss'],
        ]
        topic_list.append(topic_data)
    df = pd.DataFrame(topic_list,columns=['话题','浏览','讨论'])
    df.to_excel('bilibili_topics.xlsx',index=False,engine="openpyxl")
    print("数据已经保存！")
    
else:
    print('无法获取网页')