#Pandas模块中read_excel()函数读取Excel表格数据
import pandas as pd
data=pd.read_excel('data/trips.xlsx')
print(data)

#使用Pandas模块提提供的to_exexcel()函数把数据写入到Excel表格
datal=pd.read_excel('data/tips.xlsx',usecols=[0,1,2])
print(datal)
datal.to_excel("tips_new.xlsx",sheet_name='小费数据',index=False)

#创建Series数据
obj=pd.Series([4,7,-5,3])
print(obj)

#通过字典创建DataFram类型数据
data={'省份':['江西','广东','福建','浙江','上海'],
      '姓名':['张胜利','王冬冬','徐海峰','赵向阳','孙怀国'],
      'age':[22,29,33,25,19]}
frame=pd.DataFrame(data)
print(frame)

#Pandas常用属性访问
import pandas as pd
data=pd.read_excel('tips.xlsx')
print('小费统计表的索引为:\n',data.index)
print('小费统计表的所有值:\n',data.values)
print('小费统计表的列名:\n',data.columns)
print('小费统计表的数据类型:\n',data.size)
print('小费统计表的元素个数:',data.dtypes)
print('小费统计表维度数为:',data.ndim)
print('小费统计表的形状为:',data.shape)

#使用pandas常规数据方法访问数据
data=pd.read_excel('data/tips.xlsx')
total_bill=data["total_bill"]
print("每个帐单总金额为:\n",total_bill)


data2=data['total_bill'][2:6]
print("每个帐单总金额数据中，行索引从2到6的数据为:\n",data2)
data3=data[["total_bill","tip"]][2:6]
print("每个帐单总金额和小费这两项中，行索引从2到6的数据为:\n",data3)


#使用loc和iloc函数访问pandas数据
data=pd.read_excel("data/t.xlsx")
print("用loc方法获取行索引名称从2到10的行，有关账单总额和小费数据:\n",data.loc[2:10,["total_bill","tip"]])
print("用iloc方法获取行索引名称从2到10的行，有关账单总额和小费数据:\n",data.iloc[2:10,0:2])
print("用loc方法获取小费金额小于3块钱，有关账单总金额和小费的数据:\n",data.loc["tip"]<3,["total_bill","tip",])


#groupby函数
scores=pd.read_excel('data/scores.xlsx')
scoresGroup=scores[['class','chn','math']].groupby(by='class')
print('每个班的语文成绩和数学成绩平均分为:\n',scoresGroup.mean())

scoresGroup=scores.groupby(by='class').sum()
print(scoresGroup)

scoresGroup=scores.groupby(by='class').agg9({'chn':max,'math':min})
print(scoresGroup)


















