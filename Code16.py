import matplotlib.pyplot as plt
fig, ax= plt.subplots()
xmin= -10
xmax= 10
ymin= -10
ymax= 10
plt.axis([xmin,xmax,ymin,ymax])
plt.plot([xmin,xmax],[0,0],'b')
plt.plot([0,0],[ymin,ymax],'b')
for x in range(10):
    y = 0.5*x + 1
    plt.plot([x],[y],'ro')
plt.show()
