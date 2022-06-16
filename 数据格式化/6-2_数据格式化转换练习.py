import datetime
s = '20.19万手'

# get number
print(float(s.replace('万手', '')))
print(float(s.replace('万手', '')) * 10000)

# task 2
a = '2019/10/1'
date1 = datetime.datetime.strptime(a, '%Y/%m/%d')
future_time = date1 + datetime.timedelta(days=100)
fu = future_time.strftime('%Y{y}/%m{m}/%d{d}').format(y='年', m='月', d='日')
print(fu)

# 算出今天2019天前的日期
day = datetime.datetime.now() + datetime.timedelta(days=-2019)
print(day.strftime('%Y{y}/%m{m}/%d{d}').format(y='年', m='月', d='日'))
