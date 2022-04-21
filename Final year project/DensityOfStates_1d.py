import math
from math import pi
import numpy as np
import matplotlib.pyplot as plt

#Given values:
m0=9.1*pow(10,-31)#Mass of a free electron
mstar=0.012*m0#Effective mass of an electron
h=6.625*pow(10,-34)
hbar=h/(2*pi)
L=70*pow(10,-9)#Length of the wire
n1=1
L1=35*pow(10,-9)
L2=35*pow(10,-9)

p=((2*mstar)/(hbar*hbar))**1/2
q=(L*p)/pi
r=(pi*pi*hbar*hbar)/(2*mstar)

En1=[0.0,0.0,0.0,0.0]

for n2 in range(1,4):
    En1[n2]=r*(1/L1*L1+(n2*n2)/(L2*L2))

E=np.arange(0,5*pow(10,-20),5*pow(10,-23))
D=[0.0]*1000
D0=np.array(D)

for i in range(0,1000):
    if E[i]<En1[1]:
        D0[i]=0

    elif E[i]<En1[2]:
        D0[i]=q*((E[i]-En1[1])**(-1/2))

    elif E[i]<En1[3]:
       D0[i]=q*((E[i]-En1[2])**(-1/2))

    else:
       D0[i]=q*((E[i]-En1[3])**(-1/2))

plt.plot(E,D0,'r')
plt.xlabel('E')
plt.ylabel('D(E)')
plt.show()
