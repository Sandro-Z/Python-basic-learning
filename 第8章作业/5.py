import numpy as np

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