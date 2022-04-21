#Importing packages
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt

#Exponential distribution
x = st.expon.rvs(scale=1,size=10000)
plt.subplot(211)
plt.title('Exponential distribution')
plt.hist(x,bins=150,range=(0,10))


#Normal distribution
x = st.norm.rvs(loc=0, scale=1, size=10000)
plt.subplot(212)
plt.title('Normal distribution')
plt.hist(x,bins=150,range=(-5,5))

plt.show()
