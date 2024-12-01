reads=open('sample_sanger.fastq','r').readlines()
cache=[]
read_list=[]
count=0
for line in reads:
	cache.append(line)
	count+=1
	if count==4:
		count=0
		read_list.append(cache)
		cache=[]
for item in read_list:
	for i in range(len(item)):
		item[i]=item[i].strip()

def calc_Q(char):
	return ord(char)-33

ok=False
import random
while not ok:
	selected_list=[]
	for i in range(len(read_list)//2):
		selected_list.append(random.choice(read_list))
	Q_list=[]
	for item in selected_list:
		for char in item[-1]:
			Q_list.append(calc_Q(char))
	calc=0
	for Q in Q_list:
		if Q>30:
			calc+=1
	if calc/len(Q_list)>0.7:ok=True
print(selected_list)
output=open('sample_sanger_downsampled.fastq','w')
for i in range(len(selected_list)):
	selected_list[i]='\n'.join(selected_list[i])
output.write('\n'.join(selected_list))
output.close()