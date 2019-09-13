import scipy
import numpy as np
from scipy.stats import gamma
import matplotlib.pyplot as plt
import numpy.random as npr
from rate import rate_inc

#renvoie le vecteur gradient d'une fonction

def grad_f(f,param,h):
	a=np.array(param)
	grad=(f(a+h)-f(a))/h
#	df=0
#	for j in range(len(param)):
#		df=rate_inc(f,param,h,j)
#		grad.append(df)

	return np.array(grad)