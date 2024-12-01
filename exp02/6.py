import numpy
expression_file=open('matrix.txt.4','r').readlines()[1:]
lines=[]
for line in expression_file:
    lines.append(line.strip().split('\t'))
dic={}
for gene in lines:
	subls=gene[1:]
	for i in range(len(subls)):
		subls[i]=int(subls[i])
	var=numpy.var(subls)
	dic[gene[0]]=var
gene_var=list(dic.items())
gene_var.sort(key=lambda x:x[1],reverse=True)
for i in range(2000):
	print(gene_var[i][0],gene_var[i][1])