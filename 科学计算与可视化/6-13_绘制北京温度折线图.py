import numpy as np
import matplotlib.pyplot as plt
arr_tep=np.array([3,4,8,17,25,30,32,31,30,22,16,6])
arr_month=np.array(1,13,1)
p1=plt.figure(figsize=(8,6),dpi=80)
plt.title("Weather")
plt.xlabel("Month")
plt.ylabel("tem")
plt.xlim((0,12))
plt.ylim((0,50))
plt.xticks(np.arange(13))
plt.yticks(np.arange((0,50,5)))
plt.plot(arr_month,arr_tep)






