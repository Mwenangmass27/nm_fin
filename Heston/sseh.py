import scipy
import numpy as np
from scipy.stats import gamma
import matplotlib.pyplot as plt
import numpy.random as npr
import math
import pandas as pd
from mc_euler_im import mc_pricer_im
#from mc_euler_milstein import mc_pricer_milstein
#rom mc_euler_fulltr import mc_pricer_fulltr
#from scipy.optimize import least_squares

mu=0.0319
kappa=0.5 #6.21
xi=0.61
theta=0.019
rho=-0.7
vol_init=0.010201
#nmc=1000
#n=1000

def sse_heston(market_prices,x):
	x=[kappa,vol_init,theta,rho,xi]
	sse=0
	model_price=0
	for j in range(market_prices.shape[0]):
		model_price=mc_pricer_im(spot_init=market_prices.iloc[j,6],vol_init=vol_init,strike=100,time_t=market_prices.iloc[j,2],kappa=kappa,xi=xi,theta=theta,rho=rho,mu=market_prices.iloc[j,3],nmc=100,n=50)
		sse+=(model_price-market_prices.iloc[j,-1])**2
	return sse

'''
mp=pd.read_csv("market_data.csv",delimiter=";")
#print(mp.shape[0])
#print(mp.shape[1])
res=sse_heston(mp,kappa,mu,theta,rho,xi)

#print(model_price)
'''

