import pandas as pd
import numpy as np
import scipy
import matplotlib.pyplot as plt
import numpy.random as npr
from scipy.optimize import leastsq
from mc_euler_im import mc_pricer_im



def error_evaluation(market_prices,x):
	x=(vol_init,kappa,xi,theta,rho)
	err=np.zeros(market_prices.shape[0])
	for j in range(market_prices.shape[0]):
		model_price=mc_pricer_im(spot_init=market_prices.iloc[j,6],vol_init=vol_init,strike=100,time_t=market_prices.iloc[j,2],kappa=kappa,xi=xi,theta=theta,rho=rho,mu=market_prices.iloc[j,3],nmc=100,n=50)
		err[j]=(model_price-market_prices.iloc[j,-1])
	return err

mp=pd.read_csv("market_datar.csv",delimiter=";")
p0 = (0.03940606,  0.03301662,  2.48004912,  0.56642651,  0.63548062)
plsq = leastsq(error_evaluation(mp,x), p0)
print(plsq[0])