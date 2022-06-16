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
gdpdict1={"美国":(193621.3,34567),"加拿大":(16403.9,42578),"意大利":(19211.4,54887),"德国":(36518.7,38756),"法国":(25748.1,27865),"英国":(25650.5,47653),"中国":(122427.7,67498),"日本":(48844.9,63456),"印度":(24390.1,48769),"巴西":(20809.2,28765)}
alist=sorted(gdpdict,key=(lambda x:x[0]))
print("按照国家名字排序")
print(alist)
blist=sorted(gdpdict,key=(lambda x:x[1]))
print("按照GDP数据排序")
print(blist)

gdpdict1=list(gdpdict1.items())
clist=sorted(gdpdict1,key=lambda x:x[1][0])
print(clist)
dlist=sorted(gdpdict1,key=lambda x:x[1][1],reverse=True)
print(dlist)