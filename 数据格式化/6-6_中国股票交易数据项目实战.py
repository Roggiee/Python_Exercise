StockList=[]
with open("StockData.txt","r") as fn:
   lines=fn.readlines()

for S in lines:
    dict1=eval(S)
    StockList.append(dict1)
    cj=dict1['成交量'][:-2]
    if(cj.strip()!=''):
        dict1['成交量']=float(cj)*10000
    else:
        del dict1['成交量']

    cje=dict1['成交额'][:-2]
    if(cje.strip()!=''):
        dict1['成交额'] = float(cje) * 10000
    else:
        del dict1['成交额']

    cjh = dict1['委比'][:-2]
    if (cjh.strip() != ''):
        dict1['委比'] = float(cjh) * 10000
    else:
        del dict1['委比']

    StockList=dict()
    for dic in StockList:
        StockList[dic['股票名称']]=dic
        


import pickle
output=open('股票信息字典.pki','wb')
pickle.dump(StockList,output)
