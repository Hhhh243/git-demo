import requests
from lxml import etree
url='https://datachart.500star.com/ssq/'
hd={'user-agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'}
resp=requests.get(url,headers=hd)
resp.encoding='utf-8'
e=etree.HTML(resp.text)
reds=[tr.xpath('./td[contains(@class,"chartBall01")]/text()') for tr in e.xpath('//*[@id="tdata"]/tr[not(contains(@class,"tdbck"))]')]
blues=e.xpath('//*[@id="tdata"]/tr[not(contains(@class,"tdback"))]/td[contains(@class,"chartBall02")]/text()')
for r,b in zip(reds,blues):
    print(f'红球是:{r} 蓝球是:{b}')

