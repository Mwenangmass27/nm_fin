import scipy
import numpy as np
from scipy.stats import gamma
import matplotlib.pyplot as plt
import numpy.random as npr
import pandas as pd
from rate import rate_inc
from grad import grad_f
from descent import grad_descent
from sseh import sse_heston

kappa=0.5 #6.21
xi=0.61
theta=0.019
rho=-0.7
#nmc=1000
#n=1000
vol_init=0.010201
mp=pd.read_csv("market_datar.csv",delimiter=";")

vec=[kappa,vol_init,theta,rho,xi]

def f(x):
	return sse_heston(mp,x)

val=grad_descent(f,vec,10**(-4),0.1)
print(val)

print(mp)
