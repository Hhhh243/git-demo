import requests
from lxml import etree
import os
url='https://yys.163.com/media/picture.html'
hd={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'}
resp=requests.get(url,headers=hd)
e=etree.HTML(resp.text)
imgs1=[url1[:url1.rindex('/')]+'/2732x2048.jpg'for url1 in e.xpath('/html/body/div[2]/div[3]/div[1]/div[3]/div[3]/div/div/div/img/@data-src')]
imgs2=[url2[:url2.rindex('/')]+'/1080x1920.jpg'for url2 in e.xpath('/html/body/div[2]/div[3]/div[1]/div[3]/div[4]/div/div/div/img/@data-src')]
if not os.path.exists('heng'):
    os.makedirs('heng')
if not os.path.exists('shu'):
    os.makedirs('shu')

for url3 in imgs1:
    resp=requests.get(url3,headers=hd)
    file_name=url3[url3.rindex('picture'):url3.rindex('/')].replace('/','_')+'.jpg'
    print(f'正在保存；{file_name} 壁纸')
    with open(f'heng/{file_name}.jpg','wb') as f:
        f.write(resp.content)