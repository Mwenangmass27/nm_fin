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
import scipy

class FD_cn:
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
		c=dt/(2*(dx**2))

		x = np.linspace(a,b,self.nx)
		u=x[1:self.nx-1]
		T = np.maximum(np.exp(0.5*(k+1)*u)-np.exp(0.5*(k-1)*u),0)

		mat_imp=np.zeros((self.nx-2,self.nx-2))
		mat_imp[0,0]=1+2*c
		mat_imp[0,1]=-c
		mat_imp[self.nx-3,self.nx-4]=-c
		mat_imp[self.nx-3,self.nx-3]=1+2*c

		mat_exp=np.zeros((self.nx-2,self.nx-2))
		mat_exp[0,0]=1-2*c
		mat_exp[0,1]=c
		mat_exp[self.nx-3,self.nx-4]=c
		mat_exp[self.nx-3,self.nx-3]=1-2*c

		for j in range(1,self.nx-3):
			mat_imp[j,j]=1+2*c
			mat_imp[j,j-1]=-c
			mat_imp[j,j+1]=-c

			mat_exp[j,j]=1-2*c
			mat_exp[j,j-1]=c
			mat_exp[j,j+1]=c

		for n in range(0,self.nt):
			vec_imp=np.zeros(self.nx-2)
			vec_exp=np.zeros(self.nx-2)

			vec_imp[-1]=-c*(np.exp(0.5*(k+1)*x[-1]+0.25*(k+1)**2*(n*dt))-np.exp(0.5*(k-1)*x[-1 ]+0.25*(k-1)**2*((n+1)*dt)))
			vec_exp[-1]=c*(np.exp(0.5*(k+1)*x[-1]+0.25*(k+1)**2*(n*dt))-np.exp(0.5*(k-1)*x[-1 ]+0.25*(k-1)**2*(n*dt)))

			T=np.dot(np.linalg.inv(mat_imp),np.transpose(np.dot(mat_exp,T)+vec_exp-vec_imp))

		v=(np.log(self.s_on_k)-a)/dx
		val=(self.s_on_k)**(-0.5*(1-k))*np.exp(-0.125*((k+1)**2)*self.sigma**2*self.maturity)*T[int(v)-1]
		return val