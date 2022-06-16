import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family']='simhei'
plt.rcParams['axes.unicode_minus']=False  #显示负号
x=np.arange(0.0,2*np.pi,0.01)
ysin=np.sin(x)
ycos=np.cos(x)
plt.title("sin-cos函数图像")
plt.xlabel("x范围:0~2Π")
plt.ylabel("正弦(余弦)值")
plt.plot(x,ysin)
plt.plot(x,ycos)


