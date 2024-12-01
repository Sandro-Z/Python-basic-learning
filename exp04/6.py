import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('BMJ2018-fracture.txt', sep='\t')
data['LogP'] = -np.log10(data['P'])
chr_positions = {}
for chr_num in data['CHR'].unique():
    chr_data = data[data['CHR'] == chr_num]
    chr_positions[chr_num] = (chr_data['BP'].min(), chr_data['BP'].max())
plt.figure(figsize=(20, 10))
for chr_num in sorted(chr_positions.keys()):
    start, end = chr_positions[chr_num]
    chr_data = data[data['CHR'] == chr_num]
    plt.scatter(chr_data['BP'], chr_data['LogP'], color='blue', label=f'Chr {chr_num}')
tick_positions = []
tick_labels = []
for chr_num in sorted(chr_positions.keys()):
    start, end = chr_positions[chr_num]
    tick_positions.append((start + end) / 2)
    tick_labels.append(f'Chr {chr_num}')
plt.xticks(tick_positions, tick_labels)
p_value_threshold = 0.05 / len(data)
plt.axhline(y=p_value_threshold, color='r', linestyle='--', label=f'Bonferroni Threshold (p={p_value_threshold:.2e})')
plt.legend()
plt.xlabel('Chromosome Position (bp)')
plt.ylabel('-log10(P-value)')
plt.title('Manhattan Plot for Fracture GWAS')
plt.savefig('manhattan_plot.png')
plt.close()