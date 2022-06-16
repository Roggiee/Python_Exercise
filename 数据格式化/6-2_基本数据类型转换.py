#字符串转整数
i=int('2019')
#字符串转浮点数
f=float('20.19')
#浮点数转字符串
s=str(20.19)

#字符串转日期
import datetime
a="2019/10/1"
date1=datetime.datetime.strptime(a,"%Y/%m/%d")
print(date1)
#按格式输出日期
date2=date1.strftime('%Y{y}%m{m}%d{d}').format(y='年',m='月',d='日')
print(date2)

#2.列表，集合和字典的转换
#创建列表
