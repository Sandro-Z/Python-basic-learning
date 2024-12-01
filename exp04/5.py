import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

file_path='gc.txt'
data=pd.read_csv(file_path,sep='\s+',header=None,names=['P1','P2','Rg','se','Z','P'])

phenotypes=set(data['P1']).union(set(data['P2']))
phenotype_index={phenotype:idx for idx,phenotype in enumerate(phenotypes)}
phenotype_order=list(phenotype_index.keys())

correlation_matrix=np.zeros((len(phenotypes),len(phenotypes)))

for _,row in data.iterrows():
	idx1=phenotype_index[row['P1']]
	idx2=phenotype_index[row['P2']]
	correlation_matrix[idx1,idx2]=row['Rg']
	correlation_matrix[idx2,idx1]=row['Rg']

plt.figure(figsize=(12,10))
heatmap=plt.imshow(correlation_matrix,cmap='coolwarm',aspect='auto',interpolation='none')
plt.xticks(range(len(phenotype_order)),phenotype_order,rotation=90)
plt.yticks(range(len(phenotype_order)),phenotype_order)
plt.colorbar(heatmap,label='Rg')
plt.title('Genetic Correlation Heatmap')
plt.xlabel('Phenotype 1 (P1)')
plt.ylabel('Phenotype 2 (P2)')
plt.tight_layout()
plt.savefig('5.png')
plt.show()