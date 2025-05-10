import requests
import hashlib
import re
import time

#注意
#token每次登录都会变

hd={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'}
def Getsign(Nowtime,AudioId):
    #加密参数
    s=['NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt', 'appid=1014', f'clienttime={Nowtime}', 'clientver=20000', 'dfid=0jHMQT0nxtb84UxNzj27InKW', f'encode_album_audio_id={AudioId}', 'mid=9cee8b3175bebe82a84731c301652da3', 'platid=4', 'srcappid=2919', 'token=d28b54971e126d924b1c1a9ef16b4d101c6dac4c759e66cbba782bf5a8500f26', 'userid=2286093853', 'uuid=9cee8b3175bebe82a84731c301652da3', 'NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt']
    #把列表合并成字符串
    string=''.join(s)
    MD5=hashlib.md5()
    MD5.update(string.encode('utf-8'))
    signature=MD5.hexdigest()
    return signature

link='https://www.kugou.com/yy/rank/home/1-52144.html?from=rank'
html=requests.get(link,headers=hd).text
#提取歌曲ID
music_id_list=re.findall('data-eid="(.*?)">',html)
for music_id in music_id_list:
    #获取时间戳
    Nowtime=int(time.time()*1000)
    signature=Getsign(Nowtime,music_id)

    m_url = 'https://wwwapi.kugou.com/play/songinfo'
    data={
    'srcappid':'2919',
    'clientver':'20000',
    'clienttime':Nowtime,
    'mid':'9cee8b3175bebe82a84731c301652da3',
    'uuid':'9cee8b3175bebe82a84731c301652da3',
    'dfid':'0jHMQT0nxtb84UxNzj27InKW',
    'appid':'1014',
    'platid':'4',
    'encode_album_audio_id':music_id,
    'token':'d28b54971e126d924b1c1a9ef16b4d101c6dac4c759e66cbba782bf5a8500f26',
    'userid':'2286093853',
    'signature':signature
    }

    m_resp=requests.get(url=m_url,params=data,headers=hd)
    json_data=m_resp.json()
    #获取歌名
    name=json_data.get('data').get('audio_name')
    print(name)
    #获取歌曲链接
    play_url=json_data['data']['play_url']
    print(play_url)
    #获取歌曲内容
    music_content=requests.get(url=play_url,headers=hd).content
    #数据保存
    with open(f'xm25music\\{name}.mp3','wb') as f:
        f.write(music_content)