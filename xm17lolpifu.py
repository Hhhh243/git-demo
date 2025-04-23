import requests
import re
from time import sleep
import os
hd={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'}

all_hero_url='https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js?ts=2908981'
all_hero_js_resp=requests.get(all_hero_url,headers=hd)
all_hero_name=all_hero_js_resp.json().get('hero')
id_list=[]
name_list=[]
for i in all_hero_name:
   id_list.append(i.get('heroId'))
   name_list.append(i.get('name'))
for n,x in zip(id_list,name_list):
    sleep(1)
    url=f'https://game.gtimg.cn/images/lol/act/img/js/hero/{n}.js?ts=2908973'
    resp=requests.get(url,headers=hd)
    hero_info_js=resp.text
    hero_ids=re.findall(r'"skinId":"(\d+?)"',hero_info_js)
    hero_names=re.findall(r'"name":"(.+?)".+?"chrom',hero_info_js)
    img_url= [a.get('loadingImg') for a in resp.json().get('skins')]
    for src,id,name in zip(img_url,hero_ids,hero_names):
        if src=='':
            continue
        else:
            img_resp=requests.get(src,headers=hd)
            name=name.encode().decode('unicode_escape') #转中文
            if not os.path.exists(f'loljpg/{x}'):
                os.mkdir(f'loljpg/{x}')
            with open(f'./loljpg/{x}/{name}.jpg','wb') as f:
                f.write(img_resp.content)
            sleep(2)





