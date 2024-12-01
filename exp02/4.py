all_cells=open('barcodes.tsv','r').readlines()
for i in range(len(all_cells)):
	all_cells[i]=all_cells[i].strip()
output=open('matrix.txt.4','w')
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