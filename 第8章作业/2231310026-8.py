#生物强基2301张海阳
#1
import numpy as np
array=np.arange(0,102,2)
#2，3
arr1=np.random.rand(5,3)
arr2=np.random.randint(0,5,size=[5,3])
arr3=arr1**2
print(arr2+arr3,arr2-arr3,arr2*arr3,arr2/arr3)
print(arr1)
arr4=arr1[:,1]
arr4[0]=100
print(arr1)#发生变化
#4
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
#5
arr1=np.random.random((8,8))
arr1[0,0]=np.nan
arr1[3,4]=np.nan
arr2=arr1.copy()
print(arr1)
#delete可以直接一条语句删除所有符合条件的行/列
arr1=np.delete(arr1,np.where(np.isnan(arr1))[0],axis=0)
print(arr1)

for line in arr2:
	if np.isnan(line).any():
		cache=np.delete(line,np.where(np.isnan(line)))
		line[np.where(np.isnan(line))]=np.mean(cache)
print(arr2)

arr3=np.sqrt(arr2)
print(np.mean(arr3,axis=1))
print(np.max(arr3,axis=1))
print(np.min(arr3,axis=1))

def get_mean(iterable:np.ndarray):
	print((sum(iterable)-iterable.max()-iterable.min())/(len(iterable)-1))

np.apply_along_axis(get_mean,axis=1,arr=arr3)