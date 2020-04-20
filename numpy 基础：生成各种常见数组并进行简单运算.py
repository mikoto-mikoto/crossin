import numpy as np
import matplotlib.pyplot as plt
#1.
arr1=np.arange(4).astype('float').reshape(2,2)
print("第一题输出结果：arr1=\n",arr1)

#2.
arr2=np.zeros((6,6))
arr3=np.ones((6,6))
arr4=np.eye(6)

print("\n第二题输出结果：\narr2=\n",arr2,"\narr3=\n",arr3,"\narr4=\n",arr4)

#3.
arr5=np.arange(10,step=2).astype('int')
print("\n第三题输出结果：\narr5=\n",arr5)

#4.
arr6=np.linspace(1,13,6,endpoint=False)
print("\n第四题输出结果：\narr6=\n",arr6)

#5.
arr7=np.random.randint(0,100,10)
print("\n第五题输出结果：随机数组为\n",arr7)
arr7[np.argmax(arr7)]=0
print("替换后为\n",arr7)

#6.
x=np.array([1,2,3,2,3,4,3,4,5,6])
y=np.array([7,2,10,2,7,4,9,4,9,8]) 
 
dict1=np.linalg.norm(x-y)
dict2=np.sqrt(np.sum(np.square(x-y)))
print("\n第六题输出结果：两种方式算出来的结果分别为dict1=\n",dict1,"\ndict2=\n",dict2)

#7.
np.random.seed(1) 
values = np.random.randn(1000).cumsum()
print("\n第七题输出结果:")
plt.plot(values)
plt.show()

#8.
np.random.seed(1) 
arr9=np.random.randn(1000)
def Maxdown(arr):
    i=np.argmax((np.maximum.accumulate(arr)-arr)/np.maximum.accumulate(arr))
    if i == 0:
        return 0
    j=max(arr[:i])
    return (j-arr[i])/j

print("\n第八题输出结果:任务7中资金价值的最大回撤为\n",Maxdown(arr9))