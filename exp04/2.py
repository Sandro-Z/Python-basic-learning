import matplotlib.pyplot as plt

days=['星期一','星期二','星期三','星期四','星期五','星期六','星期日']
maxTmp=[20.1,19.3,22.0,16.2,11.1,25.1,6.8]
minTmp=[11.0,12.5,9.2,3.6,5.2,6.5,-2.3]
plt.style.use('ggplot')
plt.rcParams['font.sans-serif']=['SimHei']
plt.plot(days,minTmp,label='最低温',marker='^',color='orange',linewidth=2)
plt.plot(days,maxTmp,label='最高温',marker='^',color='#17becf',linewidth=2)
plt.title('一周温度变化')
plt.savefig('2.png')
plt.show()
