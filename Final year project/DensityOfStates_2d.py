def H(n):
    if n<0:
        return 0
    else:
        return 1

import math
from math import pi
import numpy as np
import matplotlib.pyplot as plt

#Given values:
m0=9.1*pow(10,-31)#Mass of a free electron
mstar=0.01*m0#Effective mass of an electron
h=6.625*pow(10,-34)
hbar=h/(2*pi)
d=30*pow(10,-9)

p=(hbar*hbar*pi*pi)/(2*mstar*d*d)
q=mstar/(pi*hbar*hbar)

En=[0.0,0.0,0.0,0.0]
En0=np.array(En)
D=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
D0=np.array(D)

for n in range(0,4):
    En0[n]=p*n*n

E=np.arange(0,3*pow(10,-20),pow(10,-21))

for i in range(0,30):
    if E[i]<En0[0]:
        D0[i]=0
    
    elif E[i]<En0[1]:
        D0[i]=1

    elif E[i]<En0[2]:
        D0[i]=2

    elif E[i]<En0[3]:
        D0[i]=3

plt.plot(E,D0)
plt.xlabel('E')
plt.ylabel('D(E)')
plt.show()






