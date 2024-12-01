gene_cell_file=open('matrix.txt.1','r').readlines()[1:]
cell_expression_file=open('matrix.txt.2','r').readlines()[1:]
output_file=open('matrix.txt.5','w')

#根据mat2进行针对细胞的第一轮筛选
cells_ok=[]
line=None
bol=input('请输入筛选条件：')
for line in cell_expression_file:
	line=line.strip('').split('\t')
	try:
		if eval(bol):
			cells_ok.append(line[0])
	except NameError:
		print('筛选条件不合法！')
		break

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
output_file.close()

all_cells=open('barcodes.tsv','r').readlines()
for i in range(len(all_cells)):
	all_cells[i]=all_cells[i].strip()
output=open('matrix.txt.6','w')
#写矩阵第一行
output.write('genes\t')
output.write('\t'.join(all_cells))

mat3=open('matrix.txt.3','r').readlines()[1:]
genes=[]
for line in mat3:
	genes.append(line.strip().split('\t')[0])
#基因去重
genes=list(set(genes))

#准备按行输出
for gene in genes:
	selected_lines=[]
	for line in mat3:
		if gene in line:
			selected_lines.append(line.strip().split('\t'))
	cell_expression_dict={}
	for cell in all_cells:
		cell_expression_dict[cell]=0
	for line in selected_lines:
		cell_expression_dict[line[1]]=line[2]
	output.write('{}\t'.format(gene))
	ls_cache=[]#准备后面使用join方法，以去除最后一个元素换行的问题
	for cell in all_cells:
		ls_cache.append(str(cell_expression_dict[cell]))
	output.write('\t'.join(ls_cache))
	output.write('\n')