genes=open('sample_sanger.fastq','r')
read_number=0
for line in genes:
	if line.startswith('+'):
		read_number+=1
print('总共{}条reads'.format(read_number))
Q_file=open('sample_sanger.fastq.txt.1','r')
Q_mean_list=[]
for line in Q_file:
	line=line.strip().split(',')
	for i in line:
		if i=='0':line.remove(i)
	for i in range(len(line)):
		line[i]=int(line[i])
	Q_mean_list.append(sum(line)/len(line))
biggerthan30=[]
for Q in Q_mean_list:
	if Q>30:
		biggerthan30.append(Q)
print('平均质量大于30的比例为{:.2%}'.format(len(biggerthan30)/len(Q_mean_list)))

import numpy as np
Q_array=np.loadtxt('sample_sanger.fastq.txt.1',dtype=np.int32,delimiter=',',)
Q_mean=np.mean(Q_array,axis=0)
print(Q_mean)

DNA_list=[]
fi=open('sample_sanger.fastq','r').readlines()
for i in range(len(fi)):
	if i%4==1:
		DNA_list.append(fi[i].strip())
rate_list=[]
for dna in DNA_list:
	rate_list.append((dna.count('C')+dna.count('G'))/len(dna.strip()))
num=0
for item in rate_list:
	if item<0.3 or item>0.7:num+=1
print('GC含量<30或者>70%的比例为{:.2%}'.format(num/len(rate_list)))