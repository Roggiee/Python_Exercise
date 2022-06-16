#⑴ 导入jieba库
import jieba
#⑵ 打开szpt.txt文件
f=open("szpt.txt""r").read()
seg_list=jieba.lcut(f)
#⑷ 创建空字典counts
counts={}
#⑸ 在列表seg_list中遍历每个词：
#⑹ 以词为键，创建字典的值，即统计数
for i in seg_list:
    counts[i]=counts.get(word,0)+1
#⑺ 将字典转换为列表
myitem=list(counts.items())
#(8) 按指定字段（统计数）对列表元素排降序
myitem.sort(key=lambda x:x[1],reverse=True)
#⑼ 打印输入列表前10个元素，即统计数最大的前10个词语
for j in range(10):
    word,counts=myitem[j]
    print(myitem[j])