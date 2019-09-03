import scipy
import numpy as np
from scipy.stats import gamma
import matplotlib.pyplot as plt
import numpy.random as npr
from rate import rate_inc


def grad_f(f,param,h):
	grad=[]
	df=0
	for j in range(len(param)):
		df=rate_inc(f,param,h,j)
		grad.append(df)
	return np.array(grad)