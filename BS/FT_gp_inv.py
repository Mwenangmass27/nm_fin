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
import math

class FT_gp_inv:
	def __init__(self,s_on_k,maturity,sigma,mu,n,a,b):
		self.s_on_k=s_on_k
		self.maturity=maturity
		self.sigma=sigma
		self.mu=mu
		self.n=n
		self.a=a
		self.b=b

#	def char_func(self,x):
#		i=complex(0,1)
#		return np.exp(i*x*(np.log(self.s_on_k)+self.maturity*(self.mu-((self.sigma)**2)/2))-0.5*self.maturity*(self.sigma*x)**2)

#	def integrand(self,x,char_func):
#		i=complex(0,1)
#		k=self.maturity*(self.sigma**2)
#		return char_func(self,x)*np.exp(-i*k*x)/(i*x)

	def pi_1(self):
		i=complex(0,1)
		#k=self.maturity*(self.sigma**2)
		sum=0
		h=(self.b-self.a)/self.n
		vec=np.linspace(self.a,self.b,self.n,endpoint=True)
		for x in vec:
			char_func=np.exp(i*x*(np.log(self.s_on_k)+self.maturity*(self.mu+((self.sigma)**2)/2))-0.5*self.maturity*(self.sigma*x)**2)
			integrand=char_func/(i*x)
			sum+=integrand
		v0=np.exp(i*self.a*(np.log(self.s_on_k)+self.maturity*(self.mu+((self.sigma)**2)/2))-0.5*self.maturity*(self.sigma*self.a)**2)
		vn=np.exp(i*self.b*(np.log(self.s_on_k)+self.maturity*(self.mu+((self.sigma)**2)/2))-0.5*self.maturity*(self.sigma*self.b)**2)
		g0=v0*np.exp(i*self.a)/(i*self.a)
		gn=vn*np.exp(i*self.b)/(i*self.b)
		return (0.5+(1/math.pi)*h*(sum-0.5*(g0+gn))).real




	def pi_2(self):
		i=complex(0,1)
#		k=self.maturity*(self.sigma**2)
		sum=0
		h=(self.b-self.a)/self.n
		vec=np.linspace(self.a,self.b,self.n,endpoint=True)
		for x in vec:
			char_func=np.exp(i*x*(np.log(self.s_on_k)+self.maturity*(self.mu-((self.sigma)**2)/2))-0.5*self.maturity*(self.sigma*x)**2)
			integrand=char_func/(i*x)
			sum+=integrand
		v0=np.exp(i*self.a*(np.log(self.s_on_k)+self.maturity*(self.mu-((self.sigma)**2)/2))-0.5*self.maturity*(self.sigma*self.a)**2)
		vn=np.exp(i*self.b*(np.log(self.s_on_k)+self.maturity*(self.mu-((self.sigma)**2)/2))-0.5*self.maturity*(self.sigma*self.b)**2)
		g0=v0/(i*self.a)
		gn=vn/(i*self.b)
		return (0.5+(1/math.pi)*h*(sum-0.5*(g0+gn))).real

	def pricer_call(self):
		z=self.s_on_k*self.pi_1()-np.exp(-self.mu*self.maturity)*self.pi_2()
		return z
