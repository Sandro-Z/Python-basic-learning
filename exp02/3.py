gene_cell_file=open('matrix.txt.1','r').readlines()[1:]
cell_expression_file=open('matrix.txt.2','r').readlines()[1:]
output_file=open('matrix.txt.3','w')

#根据mat2进行针对细胞的第一轮筛选
cells_ok=[]
for line in cell_expression_file:
	line=line.strip('').split('\t')
	if not (eval(line[1])<200 or eval(line[2])<500 or eval(line[2])>5000 or eval(line[3].strip().strip('%'))/100>0.2):
		cells_ok.append(line[0])

#根据mat1进行针对基因的第二轮筛选
mat1_ls=[]
for line in gene_cell_file:
	line=line.strip().split('\t')
	if line[1] in cells_ok:
		mat1_ls.append(line)
gene_appeared_times={}
selected_gene=[]
for item in mat1_ls:
	gene_appeared_times[item[0]]=gene_appeared_times.get(item[0],0)+1
for item in gene_appeared_times.items():
	if item[1]>3:
		selected_gene.append(item[0])

#写文件
output_file.write('gene\tcell\tN\n')
for item in mat1_ls:
	if item[0] in selected_gene:
		output_file.write('{0}\t{1}\t{2}\n'.format(item[0],item[1],item[2]))