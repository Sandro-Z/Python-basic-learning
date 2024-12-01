import matplotlib.pyplot as plt

d={
	'exon':5,
	'intron':42,
	'intergenic':45,
	'UTR':3,
	'Promoter':5
}
plt.figure()
plt.pie(d.values(),labels=list(d.keys()),autopct='%.2f%%')
plt.show()