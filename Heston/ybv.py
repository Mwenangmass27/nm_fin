import os
import time
import shutil
import subprocess
from datetime import datetime
import glob, os, shutil
import numpy as np
import json
import datetime
import matplotlib.pyplot as plt
import numpy.random as npr
import closedform as cf
import scipy.integrate as integrate
int_law=10000
h=1/1000
samples=[]
for k in range(int_law):
	g=npr.normal(0,1)
	motion=np.zeros(1000)
	bridge=np.zeros(1000)
	sum=1
	motion[0]=sum
	for j in range(1,1000):
		sum+=g
		g=npr.normal(0,1)
		motion[j]=sum
	for j in range(1000):
		bridge[j]=motion[j]+(j/1000)*((1+h)-motion[-1])
	
	subV=[]
	subV[0]=Vu
	subV[l]=Vt
	for j in range(1000):
		suvV[j]


	su=integrate.simps(bridge,range(1000))
	samples.append(su)
s=np.array(samples)
np.savetxt("out.csv",s)
plt.hist(s,bins='auto')
plt.show()

#	plt.plot(range(1000),bridge)
#	plt.show()


