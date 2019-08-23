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
import math
import scipy.integrate as integrate


i=complex(0,1)


class FT_H:
	def __init__(self,maturity,mu,kappa,vol_init,spot_init,xi,theta,rho):
		self.maturity=maturity
		self.mu=mu
		self.kappa=kappa
		self.xi=xi
		self.vol_init=vol_init
		self.spot_init=spot_init
		self.theta=theta
		self.rho=rho
		self.strike=100

	def alpha(self,x,j):
		res=-0.5*x**2-0.5*x+i*j*x
		return res

	def beta(self,x,j):
		res=self.kappa-self.rho*self.xi*j-self.rho*self.xi*i*x
		return res

	def gamma(self):
		res=0.5*self.xi**2
		return res

	def d(self,x,j):
		res=np.sqrt(self.beta(x,j)**2-4*self.alpha(x,j)*self.gamma())
		return res

	def rm(self,x,j):
		res=(self.beta(x,j)-self.d(x,j))/self.xi**2
		return res

	def rp(self,x,j):
		res=(self.beta(x,j)+self.d(x,j))/self.xi**2
		return res

	def g(self,x,j):
		res=self.rm(x,j)/self.rp(x,j)
		return res

	def param1(self,j,x,tho):
		res=self.kappa*(self.rm(x,j)*tho-(2/self.xi**2)*np.log((1-self.g(x,j)*np.exp(-self.d(x,j)*tho))/(1-self.g(x,j))))
		return res

	def param2(self,j,x,tho):
		res=(self.rm(x,j)*(1-np.exp(-self.d(x,j)*tho)))/(1-self.g(x,j)*np.exp(-self.d(x,j)*tho))
		return res

	def psi(self,x,tho):
		return np.exp(self.param1(0,x,tho)*self.theta+self.param2(0,x,tho)*self.vol_init)

	def integrand(self,a,b,n):
		su=0
		h=(b-a)/n
		ft=np.exp(self.mu*self.maturity)*self.spot_init
		u=np.log(self.strike/ft)
		vec=np.linspace(a,b,n,endpoint=True)
		y=[(self.psi(vec-0.5*i,self.maturity)*np.exp(-i*u*vec)*(1/(0.25+vec**2))).real]
		su=integrate.simps(y,vec)
		return su

	def pricercall(self,a,b,n):
		res=self.spot_init-(np.sqrt(self.spot_init*self.strike*np.exp(-self.mu*self.maturity))/math.pi)*self.integrand(a,b,n)
		return res
