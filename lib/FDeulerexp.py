#----------------------
#ID: *
#NAME: *
#DES: *
#AUTHOR: Alexandre LE MAISTRE
#VERSION: 1.0.0
#DATE: 2016-07-18
#----------------------

#Set python library
import os
import time
import shutil
import subprocess
from datetime import datetime
import glob, os, shutil
import numpy as np
import json
import datetime
import BSanalytic as bs
import matop
import matplotlib.pyplot as plt

class FDeulerexp:
	def __init__(self,s_on_k,maturity,sigma,mu,s_max,n,m):
          self.s_on_k=s_on_k
          self.maturity=maturity
          self.sigma=sigma
          self.mu=mu
          self.s_max=s_max
          self.n=n
          self.m=m

	def pricer_call(self):
		alpha=float(self.sigma)**2/2
		beta=float(self.mu)-alpha
		gamma=-float(self.mu)

		dx=(np.log(self.s_max)-np.log(self.s_on_k))/float(self.m)
		tabx=[np.log(self.s_on_k)+(i-1)*dx for i in range (1,self.m)]
		tabs=[np.exp(x) for x in tabx]
		dt=self.maturity/self.n
		

		ksi1=(dt*alpha)/dx**2+beta/(2*dx)
		ksi2=1+dt*(gamma-2*alpha/(dx**2))
		ksi3=dt*(alpha/(dx**2)-beta/(2*dx))

		vect=[np.maximum(s-1,0) for s in tabs]

		for i in range (1,self.n):
			tn=self.maturity-i*dt
			A=matop.tridiag(ksi1,ksi2,ksi3,len(vect))
			c=np.zeros(len(vect))
			c[0]=(ksi3)*((self.s_on_k)-1)*np.exp(-self.mu*(self.maturity-tn))
			vect=matop.mult(A,vect)
			vect+=c

		tabsbis=[(self.s_on_k)]+tabs+[(self.s_max)]
		vectbis=[((self.s_on_k)-1)*np.exp(-self.mu*self.maturity)]+vect.tolist()+[vect[len(vect)-1]]	
		print(vectbis)
