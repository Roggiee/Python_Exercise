import numpy as np
import pandas as pd
arr=np.array([1,3,5],[2,4,6],[7,9,11],[8,10,12])
#请输出二维数组中第二列所有元素
print(arr[:,1])
#请输出二维数组中第三行所有元素
print(arr[2,:])
#请输出二维数组的均值
print(np.mean(arr))
#请输入二维数组的标准差
print(np.std[arr])

dict={'one':['A','A','B','C','C','A','B','B','A','A'],
      'two':['B','B','C','C','A''A','C','B','C','A'],
      'three':['C','B','A','A','B','B','B','A','A','C''D']}
#通过字典创建DataFrame类型数据
frame=pd.DataFrame(dict)
print(frame.size)
#请输出满足one这一列元素值为A的所有行
print(frame.loc[frame=="A"])


#任务应用
data=pd.read_excel("scores.xlsx")
print(data.loc[1:])
print(data.loc[1:,2:,4:])
print(data.loc[2:10,"数学":"语文"])
print(data.loc[data["class"]==3,["语文","数学"]])
print(data["语文"]<60,"语文")
math=data.lioc[:,3]
print(data.iloc[2:10,[2,3]])

#groupby函数
scores=pd.read_excel('data/scores.xlsx')
scoresGroup=scores[['class','chn','math']].groupby(by='class')
print('每个班的语文成绩和数学成绩平均分为:\n',scoresGroup.mean())

scoresGroup=scores.groupby(by='class').sum()
print(scoresGroup)

scoresGroup=scores.groupby(by='class').agg9({'chn':max,'math':min})
print(scoresGroup)





























