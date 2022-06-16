import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.family']='STSONG'
plt.rcParams['font.size']=16

index_col=[0]
sdf=pd.read_excel("tj_course.xlsx",index_col=[0],header=0)


#改进:选课3门课图形展示
sdf3=sdf.iloc[0:3,0:3]
sdf3.plot(kind='bar',figsize=(10,5))
plt.xlabel(rotation=0)

sdf.plot(kind="bar")
plt.title("课程信息")
plt.ylabel('成绩')
plt.legend(fontsize=10)
plt.savefig('mybar.jpg')
plt.show()
