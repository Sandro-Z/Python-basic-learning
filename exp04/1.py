import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,4,50)
d=np.random.randn(50)
f=x**3-2*x**2+3
y=f+d
plt.scatter(x,y,marker='o')

plt.plot(x,f,linewidth=3,label='y=x^3-2x^2+3')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('curve')
plt.savefig('1.png')
plt.show()