import numpy as np
import pandas as pd
df=pd.read_csv('xm23wx.csv',header=16)

df['金额']=pd.to_numeric(df['金额(元)'].str[1:],errors='ignore')
df['交易时间']=pd.to_datetime(df['交易时间'],errors='ignore')
df['时段']=df['交易时间'].apply(lambda x : x.strftime('%H'))
df['月份']=df['交易时间'].apply(lambda x : x.strftime('%Y-%m-%d'))

out_file_name='out.xls'
writer = pd.ExcelWriter(out_file_name,engine='openpyxl')
df.to_excel(excel_writer=writer,sheet_name='原始数据')

#交易时间
df2=pd.pivot_table(df,index=['月份'],values=['金额'],aggfunc=(sum,len,max,np.mean))
#保存结果到excel
df2.to_excel(excel_writer=writer,sheet_name='交易时间分析')

#交易对象
df3=pd.pivot_table(df,index=['交易对方'],values=['金额','收/支'],aggfunc=(sum,len))
#保存结果到excel
df3.to_excel(excel_writer=writer,sheet_name='交易对象分析')

writer.save()
writer.close()