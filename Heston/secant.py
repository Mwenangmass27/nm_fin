import scipy
import numpy as np
from scipy.stats import gamma
import matplotlib.pyplot as plt
import numpy.random as npr

def secant(a,b,f,tol):
	vec_x=[a,b]
	xf=a
	while(np.absolute(vec_x[-1]-xf)>tol):
		x_new=vec_x[-1]-(vec_x[-1]-xf)/(f(vec_x[-1])-f(xf))*f(vec_x[-1])
		xf=vec_x[-1]
		vec_x.append(x_new)
	return vec_x[-1]