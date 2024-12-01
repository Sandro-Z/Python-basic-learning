import matplotlib.pyplot as plt
import pandas as pd

#1
p1=plt.figure(figsize=(8,6),dpi=80)
sub1=p1.add_subplot(1,2,1)
y= [1.5, 3.4, 2.1, 5.4, 6.2, 8.5, 3.3, 4.2, 5.6, 6.7]
x=range(1,11)
sub1.plot(x,y,color='c',marker='o')
sub2=p1.add_subplot(1,2,2)
y=[5.5, 6.4, 4.1, 2.4, 1.2, 6.5, 2.3, 5.2, 2.6, 3.7]
sub2.plot(x,y,linestyle='-.',marker='o')
plt.show()

#2
t1=pd.read_csv('t1.csv',names=['Gene','Expression'])
plt.figure()
plt.bar(t1.loc[:,'Gene'],t1.loc[0:,'Expression'],color='green')
plt.show()

#3
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

#4
years=[2017,2018,2019,2020,2021,2022]
sales=[41,53,88,280,432,643]
growth=[100,129,215,683,1054,1568]

fig=plt.figure()

ax1=fig.add_subplot(1,1,1)
ax1.bar(years,sales)
ax1.set_ylabel('Sales')

ax2=ax1.twinx()
ax2.plot(years,growth,color='y',marker='o')
ax2.set_ylabel('Growth (%)')

plt.show()