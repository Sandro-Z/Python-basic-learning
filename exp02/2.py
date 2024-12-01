source=open('matrix.txt.1','r')
file_output=open('matrix.txt.2','w')

source_list=source.readlines()[1:]
data=[]
for line in source_list:
	data.append(line.strip().split('\t'))

cell_expression_dict={}#细胞——总表达量
cell_genenum_dict={}#细胞——基因数目
cell_hasMT_expnum={}
for row in data:
	cell_expression_dict[row[1]]=cell_expression_dict.get(row[1],0)+eval(row[2])
	cell_genenum_dict[row[1]]=cell_genenum_dict.get(row[1],0)+1
	if 'MT-' in row[0]:
		cell_hasMT_expnum[row[1]]=cell_hasMT_expnum.get(row[1],0)+eval(row[2])

file_output.write('cell\tnFeature_RNA\tnCount_RNA\tpercent_mt\n')
for cell in cell_expression_dict:
	file_output.write('{}\t{}\t{}\t{:.2%}\n'.format(cell,cell_genenum_dict[cell],cell_expression_dict[cell],cell_hasMT_expnum[cell]/cell_expression_dict[cell]))