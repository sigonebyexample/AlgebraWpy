import matplotlib.pyplot as plt
fig, ax= plt.subplots()
xmin= -10
xmax= 10
ymin= -10
ymax= 10
plt.axis([xmin,xmax,ymin,ymax])
plt.plot([xmin,xmax],[0,0],'b')
plt.plot([0,0],[ymin,ymax],'b')
plt.plot([5],[4], 'ro')
plt.show()
