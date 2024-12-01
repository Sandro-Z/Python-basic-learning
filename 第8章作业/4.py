lst = ['4.2','-0.5','2.3','6.3','6.5','-3.4','1.4','7.5']
import numpy as np
arr=np.array(lst,dtype='float32')
print(arr.ndim,arr.shape)
print(np.any(arr>0))
print(np.all(arr>0))
for i in range(len(arr)):
	if arr[i]<0:
		print(i)

arr1=arr**2
print(arr1)
arr2=arr1.reshape((4,2))
print(arr2)
arr3=arr2.T
print(arr3)
arr3[0,0]=100
print(arr2)#发生变化

