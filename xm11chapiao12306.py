# 3车次  4车起始  6查询起始点  5车终点  7查询车终点  8出发时间  9到达时间  10历时  32商务特等  31一等座  30二等座 二等包座  21高级软卧  23软卧一等卧、动卧  28硬卧二等卧  27软座?  29硬座  26无座
import requests
import sys
start_time=sys.argv[3]
begin_addr=sys.argv[2]
end_addr=sys.argv[1]
#获取城市信息
station_url='https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9343'
hd = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'}
resp=requests.get(station_url,headers=hd)

s_data=resp.text[resp.text.find('='):-1]
s_data=s_data.split('|')
num = len(s_data)//5
station_name={}
station_name_back={}
k1=1
k2=2
for i in range(num):
    station_name[s_data[k1]]=s_data[k2]
    station_name_back[s_data[k2]] = s_data[k1]
    k1+=5
    k2+=5
#获取票信息
ba=station_name.get(begin_addr)
ea=station_name.get(end_addr)
url=f'https://kyfw.12306.cn/otn/leftTicket/queryG?leftTicketDTO.train_date={start_time}&leftTicketDTO.from_station={ba}&leftTicketDTO.to_station={ea}&purpose_codes=ADULT'
hd={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    'cookie':'_uab_collina=174478480990979815963561; JSESSIONID=D2F4E925D4E102A7F8C7CDBE7AD3462B; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; _jc_save_fromStation=%u77F3%u5BB6%u5E84%2CSJP; _jc_save_toStation=%u4FDD%u5B9A%2CBDP; _jc_save_wfdc_flag=dc; BIGipServerotn=1675165962.24610.0000; BIGipServerpassport=921174282.50215.0000; route=495c805987d0f5c8c84b14f60212447d; _jc_save_toDate=2025-04-18; _jc_save_fromDate=2025-04-19; BIGipServerportal=3067347210.17695.0000'
}

resp=requests.get(url,headers=hd)
resp_data=resp.json().get('data').get('result')
for r in resp_data:
    data = [a for a in r.split('|')]
    if data[1]!='列车停运':
        print(f'发车日期：{data[13]}---发车时间：{data[8]}---查询起点站：{station_name_back.get(data[6])}---商务特等余票：{data[32]}---一等座余票：{data[31]}---二等座余票：{data[30]}')