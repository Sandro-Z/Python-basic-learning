import matplotlib.pyplot as plt
import pandas as pd
import random
COLORS=[
	'red',
	'blue',
	'green',
    'yellow',
    'orange',
    'purple',
    'pink',
	'cyan'
]

t=pd.read_table('countries.txt')
d={}
for line in t.itertuples():
	d[line[1]]=[line[2],line[3],line[4]]
x=[]
y=[]
size=[]
for item in list(d.values()):
	y.append(item[1])
	x.append(item[0])
	size.append(item[2]/20)
plt.figure()
plt.scatter(x,y,s=size,color=COLORS)
for i in range(len(x)):
	plt.annotate(list(d.keys())[i], xy = (x[i], y[i]), xytext = (x[i]+1, y[i]))
plt.ylim(60,85)
plt.xlim(5,45)
plt.rcParams['font.sans-serif']=['SimHei']
plt.xlabel('出生率（/千人）')
plt.ylabel('预期寿命（/岁）')
plt.savefig('4.png')
plt.show()