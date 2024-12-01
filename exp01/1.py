def calc_Q(char):
	return ord(char)-33

gene=open('sample_sanger.fastq','r').readlines()
selected_lines=[]
for i in range(len(gene)):
	if i%4==3:
		selected_lines.append(gene[i].strip())
Q_values=[]
for item in selected_lines:
	Q_lis=[]
	for char in item:
		Q_lis.append(calc_Q(char))
	if len(Q_lis)<100:
		for i in range(100-len(Q_lis)):
			Q_lis.append(0)
	Q_values.append(Q_lis)
output=open('sample_sanger.fastq.txt.1','w')
for item in Q_values:
	for i in range(len(item)):
		item[i]=str(item[i])
	output.write(','.join(item))
	output.write('\n')
output.close()