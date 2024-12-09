import matplotlib.pyplot as plt
import pandas as pd

t1=pd.read_csv('t1.csv',names=['Gene','Expression'],header=None)
print(t1)
plt.figure()
plt.bar(t1.loc[:,'Gene'],t1.loc[0:,'Expression'],color='green')
plt.show()