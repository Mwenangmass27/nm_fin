import scipy
import numpy as np
from scipy.stats import gamma
import matplotlib.pyplot as plt
import numpy.random as npr
import math
import scipy.integrate as integrate

maturity=1
mu=0.0319
kappa=6.21
xi=0.61
theta=0.019
rho=-0.7
vol_init=0.010201
spot_init=100
n=200
dt=maturity/n
d=4*theta*kappa/xi**2
val_mu=0.5*d-1
i=complex(0,1)

#fonction for the integral calculus
def gamma(a):
	return np.sqrt(kappa**2-2*xi**2*i*a)

def f(z):
	return ((0.5*z*dt)/np.sinh(0.5*z*dt))

def g(z):
	return z/(np.tanh(0.5*dt))

def h(z,vt,vu):
	return scipy.special.yv(0.5*d-1,4*np.sqrt(vt*vu)*f(z)/xi**2)

def char_func(a,vt,vu):
	r1=f(gamma(a))/f(kappa)
	r2=np.exp(((vu+vt)/xi**2)*(-g(gamma(a))))/np.exp(((vu+vt)/xi**2)*(-g(kappa)))
	r3=h(gamma(a),vt,vu)/h(kappa,vt,vu)
	return r1*r2*r3

def dist_func(x,vt,vu,a,b):
	vec=np.linspace(a,b,n,endpoint=True)
	y=((2/math.pi)*np.sin(vec*x)/vec)*(char_func(vec,vt,vu)).real
	return integrate.simps(y,vec)
samples=[]
vals=np.linspace(-100,100,n)
for xv in vals:
	df=dist_func(xv,0.07,0.010201,dt,50)
	samples.append(df)

s=np.array(samples)
plt.plot(vals,s)
plt.show()
