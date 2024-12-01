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
#第1个筛选条件
DNA_list=[]
for i in range(len(reads)):
	if i%4==1:
		DNA_list.append(reads[i].strip())
rate_list=[]
for dna in DNA_list:
	rate_list.append((dna.count('C')+dna.count('G'))/len(dna.strip()))
for i in range(len(rate_list)):
	if rate_list[i]<0.3 or rate_list[i]>0.7:
		read_list.remove(read_list[i])
#第2个筛选条件
dna_read_dict={}
for i in range(len(read_list)):
	dna_read_dict[read_list[i][1]]=dna_read_dict.get(read_list[i][1],read_list[i])
	count+=1
read_list=[]
for item in list(dna_read_dict.items()):
	read_list.append(item[1])
#第3个筛选条件
def calc_Q(char):
	return ord(char)-33

for item in read_list:
	for i in range(4,-1,-1):
		if calc_Q(item[-1][i])<20:
			item[-1]=item[-1][i+1:]
			item[1]=item[1][i+1:]

for item in read_list:
	Q_ls=[]
	for char in item[-1]:
		Q_ls.append(calc_Q(char))
	calc=0
	for i in Q_ls:
		if i>20:calc+=1
	if calc/len(Q_ls)<0.7:read_list.remove(item)
