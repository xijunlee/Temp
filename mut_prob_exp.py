import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(20,8), dpi=120)
x2 = [1,2,3,4,5,6,7,8,9,10,11,12,13]
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12,13],[0.00001,0.0001,0.001,0.01,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9])

y1 = [1124.926,1028.937,1124.954,1120.80,1022.89,1023.5079,1021.186,1022.622,1025.9089,1123.742,1026.714,1125.918,1025.81]
y2 = [246.2,236.2,238.4,232.4,234,232.2,230.4,236.2,230.2,234.4,232.8,230,236.2]
y3 = [240.382,160.386,242.038,122.28,158.871,151.055,141.037,142.762,154.95,153.454,141.146,153.709,144.55]

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
    
plt.xlim(0,14)
plt.ylim(-0.2,1.2)
plt.ylabel('normalized cost')
plt.xlabel('the probability of mutation')
plt.plot(x2,y1,color='r',linewidth=1.5,linestyle='-.',marker='D',label="Dataset 1")
plt.plot(x2,y2,color='g',linewidth=1.5,linestyle='--',marker='p',label="Dataset 2")
plt.plot(x2,y3,color='b',linewidth=1.5,linestyle=':',marker='d',label="Dataset 4")
plt.legend(loc='upper right')
plt.show()