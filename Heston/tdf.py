import scipy
import numpy as np
from scipy.stats import gamma
import matplotlib.pyplot as plt
import numpy.random as npr
import math
import scipy.integrate as integrate

maturity=1
mu=0.0319
kappa=0.5 #6.21
xi=0.61
theta=0.019
rho=-0.7
vol_init=0.10201
spot_init=100
n=150
dt=maturity/n
d=4*theta*kappa/xi**2
val_mu=0.5*d-1
i=complex(0,1)
vu=vol_init**2
vt=vu*1.007
eps=10**(-4)


xa=10**(-10)
xb=0.03
nh=1000


def gamma(a):
	return np.sqrt(kappa**2-2*xi**2*i*a)

def char_func(a,vt,vu):
	r1=(gamma(a)*np.exp(-0.5*(gamma(a)-kappa)*dt))*(1-np.exp(-kappa*dt))/(kappa*(1-np.exp(-gamma(a)*dt)))
	r2=np.exp(((vu+vt)/xi**2)*(kappa*(1+np.exp(-kappa*dt))/(1-np.exp(-kappa*dt))-gamma(a)*(1+np.exp(-gamma(a)*dt))/(1-np.exp(-gamma(a)*dt))))
	r3=scipy.special.iv(0.5*d-1,4*np.sqrt(vt*vu)*gamma(a)*np.exp(-0.5*gamma(a)*dt)/(xi**2*(1-np.exp(-gamma(a)*dt))))/(scipy.special.iv(0.5*d-1,4*np.sqrt(vt*vu)*kappa*np.exp(-0.5*kappa*dt)/(xi**2*(1-np.exp(-kappa*dt)))))
	return r1*r2*r3

def density_func(x,u,vt,vu):
	return ((1/x)*np.exp(-x*i*u)*char_func(u,vt,vu)).imag

def dist_func(x,vt,vu,a,b):
	vec=np.linspace(a,b,n,endpoint=True)
	integrand=0
	y=[]
	for x_vec in vec:
		integrand=((1/x_vec)*np.exp(-x_vec*i*x)*char_func(x_vec,vt,vu)).imag
		y.append(integrand)
	return (-np.trapz(y,vec)/(math.pi)+0.5)

def dist_func_sum(xa,xb,n):
	x_values=np.linspace(xa,xb,n,endpoint=True)
	y=[]
	pas_h=0.05
	for x in x_values:
		#pas_h=2*math.pi/x+0.00005
		int_sum=pas_h*x/math.pi
		j=1
		y_arret=10
		y_val=0
		while(y_arret>=math.pi*eps*0.5):
			y_val=char_func(pas_h*j,vt,vu).real
			y_arret=y_val/j
			int_sum+=y_val*(2/math.pi)*(1/j)*np.sin(pas_h*j*x)
			j+=1
		y.append(int_sum)
	return x_values,y

x_values,y=dist_func_sum(xa,xb,n)
yp=np.array(y)
plt.plot(x_values,yp)
plt.show()



