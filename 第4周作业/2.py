def f(*nums):
	num_list=list(nums)
	avg=sum(num_list)/len(num_list)
	higher_than_avg=0
	for num in num_list:
		if num>avg:
			higher_than_avg+=1
	return avg,higher_than_avg
print(f(1,2,3,4,5))