import serial
import time
import random
from itertools import count
import numpy as np
import matplotlib.pyplot as plt

ser = serial.Serial('COM3',9600)


mat_i = 0
mat_j = 0
window_size = 50
mat = np.zeros((window_size, window_size))




    
plt.ion()
for i in range(window_size):
    for j in range(window_size):
        b = ser.readline()
        b = float(b)
        print(b)   
        if b < 30:
            mat[mat_j,mat_i] = 250
            if mat_i == window_size-1:
                mat_i = 0
                mat_j += 1
            else:
                mat_i +=1


        plt.imshow(mat)
        plt.show()
        plt.pause(0.001)
        plt.clf()