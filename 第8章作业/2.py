import numpy as np
arr1=np.random.rand(5,3)
arr2=np.random.randint(0,5,size=[5,3])
arr3=arr1**2
print(arr2+arr3,arr2-arr3,arr2*arr3,arr2/arr3)
print(arr1)
arr4=arr1[:,1]
arr4[0]=100
print(arr1)#发生变化