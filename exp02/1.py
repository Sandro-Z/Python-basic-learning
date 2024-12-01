matrix=open('matrix.mtx','r')
features=open('features.tsv','r')
cells=open('barcodes.tsv','r').readlines()
output_file=open('matrix.txt.1','w')

#格式化基因名称列表
features_ls=features.readlines()
genes=[]
for name in features_ls:
	genes.append(name.strip().split('\t')[1])

#格式化matrix并以其中编号建立嵌套列表
matrix_ls=matrix.readlines()[2:]
matrix_=[]
for item in matrix_ls:
	matrix_.append(item.strip().split('\t'))

#格式化细胞名列表
cell_=[]
for cell in cells:
	cell_.append(cell.strip())

output_file.write('gene cell    N\n')
for i in range(len(matrix_)):
	#根据嵌套列表的值寻找gene，cell名称并填入槽中进行输出
	output_file.write('{0}\t{1}\t{2}\n'.format(genes[eval(matrix_[i][0])-1],cell_[eval(matrix_[i][1])-1],matrix_[i][2]))

output_file.close()