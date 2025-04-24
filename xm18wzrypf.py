import requests
from lxml import etree
import os
from time import sleep
hd={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'}
hero_list_url='https://pvp.qq.com/web201605/js/herolist.json'
hero_resp=requests.get(hero_list_url,headers=hd)
for h in hero_resp.json():
    id_name=h.get('id_name')
    ename=h.get('ename')
    cname=h.get('cname')
    if not os.path.exists(f'wzryjpg/{cname}.jpg'):
        os.makedirs(cname)
    url=f'https://pvp.qq.com/web201605/herodetail/{id_name}.shtml'
    resp=requests.get(url,headers=hd)
    resp.encoding='gbk'
    e=etree.HTML(resp.text)
    names=e.xpath('//ul[@class="pic-pf-list pic-pf-list3"]/@data-imgname')[0]
    a=[]
    for i in names.split('|'):
        a.append(i[0:i.index('&')])
    for i,n in enumerate(a):
        pf_url_resp=requests.get(f'https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{ename}/{ename}-bigskin-{i+1}.jpg')
        with open(f'wzryjpg/{cname}/{n}.jpg','wb') as f:
            f.write(pf_url_resp.content)
        print(f'已下载{n}的皮肤')
        sleep(1)