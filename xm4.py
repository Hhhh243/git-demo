
from flask import Flask,render_template,request
import requests #发送请求模块
from lxml import etree  #解析数据模块
app = Flask(__name__) #创建一个可以支持web应用的对象

def get_mobile(phone):
    #发送请求的地址
    url=f"https://ip138.com/mobile.asp?mobile={phone}&action=mobile"
    #伪装
    headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'}
    #发送请求
    resp=requests.get(url,headers=headers)
    #设置中文提示
    resp.encoding='utf-8'
    #解析数据
    e=etree.HTML(resp.text)
    #编写xpath提取数据
    datas0=e.xpath('//tr/td[2]/span/text()')
    datas1=e.xpath('//tr/td[2]/span/a/text()')
    datas2=e.xpath('//tr/td[2]/a[1]/text()')
    datas=' '.join(datas0)+' '.join(datas1)+' '+' '.join(datas2)
    return datas
    print(type(datas))
@app.route('/')
def index():
    return render_template("index3.html")
@app.route('/search_phone') #建立路由
def search_phone():
    phone = request.args.get('phone')
    data=get_mobile(phone)
    return '</t>'.join(data)
app.run(debug=True) #跑web服务
