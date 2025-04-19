import requests
from lxml import etree
data=[]
prices=[]
for i in range(1,4):
    prices = []
    url=f'https://newhouse.fang.com/house/s/b9{i}/'
    resp = requests.get(url)
    e=etree.HTML(resp.text)
    names=e.xpath('//div[@class="nlcd_name"]/a/text()')
    print(names)
    addreses=e.xpath('//div[@class="address"]/a/@title')
    for a, b in zip(e.xpath('//div[@class="nhouse_price"]/span/text()'),e.xpath('//div[@class="nhouse_price"]/em/text()')):
        if b == '暂未取得预售证':
            prices.append(b)
        if a == '价格待定':
            prices.append(a)
        if a and b!='暂未取得预售证':
            prices.append(a+b)
    tables=e.xpath('//div[@class="house_value clearfix"]/p/text()')
    for a,b,c in zip(names,addreses,prices):
        data.append([a,b,c])
    print(data)
    print(len(names),len(addreses),len(prices))
import pandas
df=pandas.DataFrame(data,columns=['小区名','地址','价格'])
print(df)
# url=f'https://newhouse.fang.com/house/s/b91/'
# resp = requests.get(url)
# e=etree.HTML(resp.text)
# a=e.xpath('//div[@class="nhouse_price"]/span/text()')
# c=e.xpath('//div[@class="nhouse_price"]/em/text()')
# print(len(a))
# print(len(c))