import matplotlib.pyplot as plt
import numpy as np

x1= 0
y1= 55
x2= 2
y2= 76

m= (y2 - y1) / (x2 - x1)
b= y1 - m*x1
print("y = ", m, "x + ", b)
xmin= 0
xmax= 10
ymin= 0
ymax= 150

y3= m*xmin + b
y4= m*xmax + b

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax])
plt.plot([xmin,xmax],[0,0],'b')
plt.plot([0,0],[ymin,ymax])

ax.set_xlabel("time")
ax.set_ylabel("population")
ax.grid(True)

plt.plot([xmin,xmax],[y3,y4],'r')
plt.show()
