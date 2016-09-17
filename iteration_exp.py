import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(10,8), dpi=120)
x1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],[10,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,900,1000])

y1 = [1429.352,1227.636,1025.392,1023.708,1028.998,1022.592,1033.392,1026.926,1020.776,1016.57,1023.744,1017.162,1020.55,1021.316,1018.892,1013.872,1010.512,1020.926,1016.592]
y2 = [244.6,242.2,238.4,242.4,242.2,234.2,240.4,248.2,240.6,232.2,234.2,230.6,230,230.4,232.8,226.2,228.4,230,234.2]
y3 = [175.728,150.632,134.418,172.742,355.482,349.91,175.406,154.66,166.398,174.93,143.358,106.996,114.518,107.776,169.412,129.434,148.086,106.38,124.304]
max = -2140000;
min = 2140000;
for item in y1:
    if item > max:
        max = item
    if item < min:
        min = item
for i in range(len(y1)):
    y1[i] = (y1[i] - min) / (max -min)
    
max = -2140000;
min = 2140000;
for item in y2:
    if item > max:
        max = item
    if item < min:
        min = item
for i in range(len(y2)):
    y2[i] = (y2[i] - min) / (max -min)
    
max = -2140000;
min = 2140000;
for item in y3:
    if item > max:
        max = item
    if item < min:
        min = item
for i in range(len(y3)):
    y3[i] = (y3[i] - min) / (max -min)
    
plt.xlim(0,20)
plt.ylim(-0.2,1.2)
plt.ylabel('normalized cost')
plt.xlabel('the number of iteration')
plt.plot(x1,y1,color='r',linewidth=1.5,linestyle='-.',marker='D',label="Dataset 1")
plt.plot(x1,y2,color='g',linewidth=1.5,linestyle='--',marker='p',label="Dataset 2")
plt.plot(x1,y3,color='b',linewidth=1.5,linestyle=':',marker='d',label="Dataset 4")
plt.legend(loc='upper right')
plt.show()