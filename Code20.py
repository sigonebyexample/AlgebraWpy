import matplotlib.pyplot as plt
import numpy as np
xmin= -10
xmax= 10
ymin= -10
ymax= 10
points= 2*(xmax-xmin)
x= np.linspace(xmin, xmax, points)
fig,ax=plt.subplots()
plt.axis([xmin,xmax,ymin,ymax])
plt.plot([xmin,xmax],[0,0],'b')
plt.plot([0,0],[ymin,ymax],'b')
ax.set_xlabel("x values")
ax.set_ylabel("y values")
ax.set_title("Graph")
ax.grid(True)
ax.set_xticks(np.arange(xmin, xmax+1, 1))
ax.set_yticks(np.arange(ymin, ymax+1, 1))
y = x**-1
plt.plot(x,y, 'r',label='y=x**-1')
plt.plot([4],[6], 'go', label='point')
plt.plot(x,3*x, label='steeper line')
plt.legend()
plt.show()
