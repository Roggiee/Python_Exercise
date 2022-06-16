gdpdict={"美国":193621.3,
         "加拿大":16403.9,
         "意大利":19211.4,
         "德国":36518.7,
         "法国":25748.1,
         "英国":25650.5,
         "中国":122427.7,
         "日本":48844.9,
         "印度":24390.1,
         "巴西":20809.2,}

print("按照字典的键(国家)排序")
for key in sorted(gdpdict.keys()):
    print(key,gdpdict[key])


print("按照字典的值排序，方案1")
for v in sorted(gdpdict.values()):
    print(v)