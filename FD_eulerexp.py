#----------------------
#ID: *
#NAME: *
#DES: *
#AUTHOR: Malcom WENANG-MASSING
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
import matplotlib.pyplot as plt
from   scipy.stats import norm

class FD_eulerexp:
	def __init__(self,s_on_k,maturity,sigma,mu,nx,nt):
		self.s_on_k=s_on_k
		self.maturity=maturity
		self.sigma=sigma
		self.mu=mu
		self.nx=nx
		self.nt=nt

	def pricer_call(self):
		a=np.minimum(np.log(self.s_on_k),0)-np.log(4)
		b=np.maximum(np.log(self.s_on_k),0)+np.log(4)
		k=self.mu/(0.5*self.sigma**2)
		dx=(b-a)/self.nx
		ct=self.sigma**2*self.maturity*0.5
		dt=ct/self.nt
		c=dt/(dx**2)

		x = np.linspace(a,b,self.nx)
		u=x[1:self.nx-1]
		T = np.maximum(np.exp(0.5*(k+1)*u)-np.exp(0.5*(k-1)*u),0)

		mat_exp=np.zeros((self.nx-2,self.nx-2))
		mat_exp[0,0]=1-2*c
		mat_exp[0,1]=c
		mat_exp[self.nx-3,self.nx-4]=c
		mat_exp[self.nx-3,self.nx-3]=1-2*c
		for j in range(1,self.nx-3):
			mat_exp[j,j]=1-2*c
			mat_exp[j,j-1]=c
			mat_exp[j,j+1]=c

		for n in range(0,self.nt):
			T=np.dot(mat_exp,T)
			T[-1]+=c*(np.exp(0.5*(k+1)*x[-1]+0.25*(k+1)**2*(n*dt))-np.exp(0.5*(k-1)*x[-1 ]+0.25*(k-1)**2*(n*dt)))

		v=(np.log(self.s_on_k)-a)/dx
		val=(self.s_on_k)**(-0.5*(1-k))*np.exp(-0.125*((k+1)**2)*self.sigma**2*self.maturity)*T[int(v)-1]
		return val

	def pricer_put(self):
		x_max=self.s_max
		pas_x=float(x_max)/float(self.nx)	
		pas_t=float(self.maturity)/float(self.nt)
		vec_x=np.linspace(0,x_max,self.nx+1)
		mat_eexp=np.zeros((self.nx,self.nx))

		m1=[1-(pas_t*((self.sigma*vec_x[j])/(pas_x))**2)+self.mu*pas_t for j in range(0,self.nx+1)]
		m2=[(pas_t/2)*((self.sigma*vec_x[j])/(pas_x))**2-((self.mu*vec_x[j])/2)*(pas_t/pas_x) for j in range(0,self.nx+1)]
		m3=[(pas_t/2)*((self.sigma*vec_x[j])/(pas_x))**2+((self.mu*vec_x[j])/2)*(pas_t/pas_x) for j in range(0,self.nx+1)]

		mat_eexp[0,0]=m1[1]
		mat_eexp[0,1]=m3[1]
		mat_eexp[self.nx-2,self.nx-3]=m2[self.nx-1]
		mat_eexp[self.nx-2,self.nx-2]=m1[self.nx-1]
		mat_eexp[self.nx-1,self.nx-1]=1
		for k in range(1,self.nx-2):
			mat_eexp[k,k-1]=m2[k+1]
			mat_eexp[k,k]=m1[k+1]
			mat_eexp[k,k+1]=m3[k+1]

		print((2*pas_t)/(pas_x**2))
		sol_bs=[np.maximum(1-vec_x[j],0) for j in range(0,self.nx+1)]
		val=sol_bs[1:self.nx+1]
		for n in range(1,self.nt):
			c=np.zeros(self.nx)
			c[0]=m3[1]*np.exp(-self.mu*(self.maturity-n*pas_t))
			val=np.dot(mat_eexp,(val+c))

#		print(val)

	def pricer_str(self):
		return self.pricer_put(self)+self.pricer_call(self)