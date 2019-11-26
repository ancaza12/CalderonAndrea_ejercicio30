import os
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(10,5))
data = np.loadtxt('ej30.dat')

plt.subplot(131)
plt.plot(data[:,0], data[:,1])
plt.xlabel('N_x')
plt.ylabel('N iteraciones')

plt.subplot(132)
plt.plot(data[:,0], data[:,1])
plt.xlabel('N_x')
plt.ylabel('Error centro x10^2')

plt.subplot(133)
plt.plot(data[:,0], data[:,1])
plt.xlabel('N_x')
plt.ylabel('Error convergencia x10^6')

plt.savefig('resultado.png')

