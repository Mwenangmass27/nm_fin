import scipy
import numpy as np
from scipy.stats import gamma
import matplotlib.pyplot as plt
import numpy.random as npr


def rate_inc(f,param,h,j):
	a=param
	param[j]+=h
	ah=param
	res=(f(ah)-f(a))/h
	return res