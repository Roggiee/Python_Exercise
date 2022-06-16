#精确模式
import jieba
text="我是深圳职业技术学院计算机工程学院17级软件技术专业的一名学生"
list1=jieba.lcut(text)
print("精确模式:"+"/".join(list1))

#全模式
list2=jieba.lcut(text,cut_all=True)
print("全模式"+"/".join(list2))

#搜索引擎模式
list3=jieba.lcut_for_search(text)
print("搜索引擎模式:"+"/".join(list3))


