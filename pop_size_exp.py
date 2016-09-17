import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(10,8), dpi=120)
x2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],[10,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,900,1000])

y1 = [1421.902,1628.846,1222.214,1429.114,1020.494,1228.35,1023.312,1021.388,1026.374,1025.868,1024.114,1021.08,1016.828,1019.698,1009.502,1019.386,1011.786,1019.692,1013.882] 
y2 = [260.4,250.4,236.4,232.6,240.4,236.4,230.6,238.6,240.2,242.4,228.2,232.6,236.2,230.6,230.2,226.4,226.6,228.4,230.2]
y3 = [746.484,348.458,358.964,173.304,206.888,155.694,177.228,544.95,128.366,150.146,169.264,131.872,131.262,110.038,108.174,105.19,129.044,110.628,104.916]

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
plt.xlabel('the size of population')
plt.plot(x2,y1,color='r',linewidth=1.5,linestyle='-.',marker='D',label="Dataset 1")
plt.plot(x2,y2,color='g',linewidth=1.5,linestyle='--',marker='p',label="Dataset 2")
plt.plot(x2,y3,color='b',linewidth=1.5,linestyle=':',marker='d',label="Dataset 4")
plt.legend(loc='upper right')
plt.show()