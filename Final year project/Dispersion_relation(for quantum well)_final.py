##Dispersion relation for Quantum well##
import math
from math import *
import numpy as np
import matplotlib.pyplot as plt

#Given values:
m0=9.1*pow(10,-31)#Mass of a free electron
mstar=0.012*m0#Effective mass of an electron
h=6.625*pow(10,-34)
hbar=h/(2*pi)
q=1.602*pow(10,-19)
d=50*pow(10,-9)

c=(hbar*hbar)/(2*mstar)

##1st part##
##Kinetic Energy(X direction)##
Ex=np.arange(30,200)*pow(10,-3)*q##Energy in x-direction in eV

px=[0]*(len(Ex))
lamda_x=[0]*(len(Ex))
kx=[0]*(len(Ex))
Exx=[0]*(len(Ex))

for i in range(len(Ex)):
    px[i]=sqrt(2*mstar*Ex[i])
    lamda_x[i]=h/px[i]
    kx[i]=(2*pi)/lamda_x[i]
    Exx[i]=c*kx[i]*kx[i]

##2nd part##
##Kinetic Energy(Y direction)##
Ey=np.arange(30,200)*pow(10,-3)*q##Energy in y-direction in eV

py=[0]*(len(Ey))
lamda_y=[0]*(len(Ey))
ky=[0]*(len(Ey))
Eyy=[0]*(len(Ey))

for i in range(len(Ey)):
    py[i]=sqrt(2*mstar*Ey[i])
    lamda_y[i]=h/py[i]
    ky[i]=(2*pi)/lamda_y[i]
    Eyy[i]=c*ky[i]*ky[i]

##Calculation of Ef##
n_system=3.3*pow(10,16)#in cc
ni=pow(10,10)#in cc
KT=4.11*pow(10,-21)#in J
Ef=KT*log(n_system/ni)

##3rd part##
##Potential Energy(for quantisation in Z-direction)##
n=np.arange(1,6)
b=pi/d
Ezz=[0]*len(n)

for i in range(len(n)):
    Ezz[i]=c*b*b*n[i]*n[i]

##Final Energy Calculation##
##n=1##
E1=[0]*len(Exx)

for i in range(len(Exx)):
    E1[i]=Exx[i]+Eyy[i]+Ezz[0]

##n=2##
E2=[0]*len(Exx)

for i in range(len(Exx)):
    E2[i]=Exx[i]+Eyy[i]+Ezz[1]

##n=3##
E3=[0]*len(Exx)

for i in range(len(Exx)):
    E3[i]=Exx[i]+Eyy[i]+Ezz[2]

##n=4##
E4=[0]*len(Exx)

for i in range(len(Exx)):
    E4[i]=Exx[i]+Eyy[i]+Ezz[3]

##n=5##
E5=[0]*len(Exx)

for i in range(len(Exx)):
    E5[i]=Exx[i]+Eyy[i]+Ezz[4]

##k calculation##
k=[0]*len(Exx)
for i in range(len(Exx)):
    k[i]=sqrt(kx[i]*kx[i]+ky[i]*ky[i])

E_fermi=[Ef]*len(k)

plt.plot(k,E1,k,E2,k,E3,k,E4,k,E5,k,E_fermi)
plt.title('Dispersion Relation for 2D')
plt.xlabel('Wavevector(k)')
plt.ylabel('Energy(E)')
plt.show()











