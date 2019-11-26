import os
import numpy as np
import matplotlib.pyplot as plt

plt.figure()
data = np.loadtxt('ej29.dat')

plt.subplot(131)
plt.imshow(data[:,0])

plt.subplot(132)
plt.plot(data[:,0], data[:,1])
plt.xlabel('X')
plt.ylabel('Y')

plt.subplot(133)
plt.plot(data[:,0], data[:,1])

plt.savefig('difusion.png')
