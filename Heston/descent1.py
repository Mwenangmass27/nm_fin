import scipy
import numpy as np
from scipy.stats import gamma
import matplotlib.pyplot as plt
import numpy.random as npr
from rate import rate_inc
from grad import grad_f


def grad_descent(f,x0,tol,theta):
	res=10
	xprime=x0
	xsec=0
	h=tol*100
	n=2
	ninit=0
	while(res>tol):
		xsec=xprime-theta*grad_f(f,xprime,h)
		res=np.linalg.norm(xsec-xprme)
		xprime=xsec
		theta=theta/n
		n+=1
	return np.array(xprime)