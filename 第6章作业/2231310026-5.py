#生物强基2301 张海阳
#1
import random
ls=[]
for i in range(30):
	ls.append(str(random.randint(0,30)))
f=open('test.txt','w')
for i in range(3):
	cache=ls[10*(i):10*(i+1)]
	f.write(','.join(cache))
	f.write('\n')
f.close()
fi=open('test.txt','r').readlines()
target_data=fi[1].strip('\n').split(',')
for i in range(len(target_data)):
	target_data[i]=int(target_data[i])
print(target_data)
max=max(target_data)
min=min(target_data)
average=sum(target_data)/len(target_data)
target_data.sort()
if len(target_data)%2==0:
	mid=(target_data[len(target_data)//2-1]+target_data[len(target_data)//2])/2
else:
	mid=target_data[len(target_data)//2]
print(max,min,average,mid)
#2
f=open('test.txt','r').read()
string='python'+f+'python'
f=open('test.txt','w')
f.write(string)
f.close()
#3
import os
for i in range(5):
	f=open(str(i),'w')
	f.write('')
	f.close()
for i in range(5):
	os.rename(str(i),str(i)+'python')
#4
import os
files=os.getcwd()
for file in os.listdir(files):
	if file.endswith('python'):
		os.rename(file,file[0]+'class')