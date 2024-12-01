import matplotlib.pyplot as plt

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