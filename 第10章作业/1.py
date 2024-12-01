import matplotlib.pyplot as plt

p1=plt.figure(figsize=(8,6),dpi=80)
sub1=p1.add_subplot(1,2,1)
y= [1.5, 3.4, 2.1, 5.4, 6.2, 8.5, 3.3, 4.2, 5.6, 6.7]
x=range(1,11)
sub1.plot(x,y,color='c',marker='o')
sub2=p1.add_subplot(1,2,2)
y=[5.5, 6.4, 4.1, 2.4, 1.2, 6.5, 2.3, 5.2, 2.6, 3.7]
sub2.plot(x,y,linestyle='-.',marker='o')
plt.show()