import matplotlib.pyplot as plt
import numpy as np
f=open('exp.txt','r').readlines()
l1=f[0].strip().split('\t')[1:]
l2=f[1].strip().split('\t')[1:]
l3=f[2].strip().split('\t')[1:]
l4=f[3].strip().split('\t')[1:]
for i in range(len(l1)):l1[i]=eval(l1[i])
for i in range(len(l2)):l2[i]=eval(l2[i])
for i in range(len(l3)):l3[i]=eval(l3[i])
for i in range(len(l4)):l4[i]=eval(l4[i])
main_fig=plt.figure()
ax1=main_fig.add_subplot(221)
ax1.hist(l1)
ax2=main_fig.add_subplot(222)
ax2.hist(l2)
ax3=main_fig.add_subplot(223)
ax3.hist(l3)
ax4=main_fig.add_subplot(224)
ax4.hist(l4)
plt.savefig('3.1.png')
plt.show()

plt.figure()
d={
	'Gene1':l1,
	'Gene2':l2,
	'Gene3':l3,
    'Gene4':l4
}
plt.boxplot(d.values(),labels=d.keys())
plt.savefig('3.2.png')
plt.show()

