#一维数组的创建
import numpy as np
arr1=np.array([1,2,3,4,5,6,7,8,9])
print("创建的数组为:",arr1)


#二维数组的创建
arr2=np.array([[1,2,3,4],[5,6,7,8,9]])
print("创建的数组",arr2)

#一维数组的访问
arr3=np.array([1,2,3,4,5,6,7,8,9])
print("数组arr为",arr3)
print("数组中第6个元素为:",arr3[5])
print("数组中第4个至第6个为:",arr3[3:6])
print("数组中倒数第2个元素为",arr3[:-2])
print("数组中所有的下标为奇数的元素:",arr3[1::2])


#二维数组的访问
arr4=np.array([1,2,3,4,5],[4,5,6,7,8],[7,8,9,10])
print("创建的二维数组为:\n",arr4)
print("数组中第1行中第3列和第4列的元素为:",arr4[0,2:4])
print("数组中第2行和第3行中的3-5列的元素:",arr4[1:,2:])
print("数组中第2列的元素:",arr4[:,1])



#数值运算
arr5=np.array([1,2,3,4,5],[4,5,6,7,8],[7,8,9,10,11])
print("创建的数组为:\n",arr5)
print("数组的和为:\n",np.sum(arr5))
print("数组纵轴的和为:\n",np.sum(arr5,axis=0))
print("数组的横轴的和为:\n",snp.sum(arr5,axis=1))
print("数组均值为:\n",np.mean(arr5))
print("数组的标准差为:\n",np.std(arr5))
print("数组的方差为:\n",np.var(arr5))
print("数组的最小值为:\n",np.min(arr5))
print("数组的最大值为:\n",np.max(arr5))



#Numpy文件的读和写
arr6=np.array([1,2,3,4],[4,5,6,7],[7,8,9,10])
print("创建的数组为:\n",arr6)
np.savetxt("arr6.txt",arr6,fmt="%d",delimiter=",")
loaded_data=np.loadtxt("arr6.txt",delimiter=",")
print("读取的数组为:\n",loaded_data)

















