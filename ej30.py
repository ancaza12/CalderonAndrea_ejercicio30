import os
import numpy as np
import matplotlib.pyplot as plt

plt.figure()
data = np.loadtxt('ej30.dat')

plt.subplot(121)
plt.plot(data[:,0], data[:,1])

plt.subplot(122)
plt.plot(data[:,0], data[:,1])
plt.xlabel('X')
plt.ylabel('Y')

plt.savefig('difusion.png')
