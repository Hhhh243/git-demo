from wsgiref import headers

import requests

url='https://xy124x236x62x69xy.mcdn.bilivideo.cn:4483/upgcxcode/92/36/29007283692/29007283692-1-100022.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&trid=0000f3e5f9c42a734db5aec2b682d360617u&og=cos&uipk=5&deadline=1744352531&tag=&nbs=1&platform=pc&oi=2095903168&gen=playurlv3&os=mcdn&mid=0&upsig=cc44c686e6bca74071d762e3d0d0d78b&uparams=e,trid,og,uipk,deadline,tag,nbs,platform,oi,gen,os,mid&mcdnid=50020279&bvc=vod&nettype=0&bw=120932&build=0&dl=0&f=u_0_0&agrr=0&buvid=9DC8B207-9DD7-C543-FC84-A2237A90C3C249153infoc&orderid=0,3'

hd={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)","referer":"https://www.bilibili.com/video/BV1ypXsYUEBm/?spm_id_from=333.1007.tianma.4-1-11.click"}

res=requests.get(url,headers=hd)

open('视频.mp4',"wb").write(res.content)


print(res.status_code)

url='https://xy223x247x68x233xy.mcdn.bilivideo.cn:8082/v1/resource/29007283692-1-30216.m4s?agrr=0&build=0&buvid=9DC8B207-9DD7-C543-FC84-A2237A90C3C249153infoc&bvc=vod&bw=61068&deadline=1744352531&dl=0&e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M%3D&f=u_0_0&gen=playurlv3&mcdnid=50020279&mid=0&nbs=1&nettype=0&og=hw&oi=2095903168&orderid=0%2C3&os=mcdn&platform=pc&sign=37be50&tag=&traceid=trcFcTUDZWYEBp_0_e_N&uipk=5&uparams=e%2Cdeadline%2Ctag%2Cnbs%2Cplatform%2Ctrid%2Coi%2Cmid%2Cuipk%2Cgen%2Cos%2Cog&upsig=fe4c9d27e159576238e53c1eaed6120b'

hd={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)","referer":"https://www.bilibili.com/video/BV1ypXsYUEBm/?spm_id_from=333.1007.tianma.4-1-11.click"}

res=requests.get(url,headers=hd)

open('视频.mp3',"wb").write(res.content)

from moviepy.editor import*

video=VideoFileClip("视频.mp4")
audio=AudioFileClip('视频.mp3')
hc=video.set_audio(audio)
hc.write_videofile('完整的视频.mp4')

print(res.status_code)