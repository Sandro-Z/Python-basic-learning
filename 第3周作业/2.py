a=[4,54,12,35,24,0,43,0,98,1,43,0,0,65]
sum=0
n=0
for i in a:
	if i:
		sum+=i
		n+=1
print('average={}'.format(sum/n))