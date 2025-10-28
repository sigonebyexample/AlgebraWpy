import matplotlib.pyplot as plt
x1= 1
y1= 7
x2= 2
y2= 10
m= (y2 - y1) / (x2 - x1)
b= y1 - m*x1
print("y = ", m, "x + ", b)
xmin= -10
xmax= 10
ymin= -10
ymax= 10
y3= m*xmin + b
y4= m*xmax + b
fig, ax= plt.subplots()
plt.axis([xmin,xmax,ymin,ymax])
plt.plot([xmin,xmax],[0,0],'b')
plt.plot([0,0],[ymin,ymax],'b')
plt.plot([xmin,xmax],[y3,y4],'r')
plt.show()
