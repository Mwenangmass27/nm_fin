import os
import time
import shutil
import subprocess
from datetime import datetime
import glob, os, shutil
import numpy as np
import json
import datetime
import matplotlib.pyplot as plt
import numpy.random as npr
import pandas as pd




def mc_pricer_fulltr(kappa,mu,theta,xi,rho,time_t,vol_init,spot_init,nmc,strike):
#Montecarlo loop
#	npr.seed(777) #JACKPOT
	nt=int(np.amax(time_t)*50)
	dt=int(np.amax(time_t))/nt
	a=time_t[0]
	b=np.amax(time_t)
	time_tmod=nt*time_t/b
	g=npr.normal(0,1,(nmc,nt))
	z=npr.normal(0,1,(nmc,nt))
	w=np.sqrt(1-rho**2)*g+rho*z
#calc_vol_path and spot_path
	vol_path=vol_init*np.ones((nmc,1))
	spot_path=spot_init*np.ones((nmc,1))
	payoff_sum=0
	option_price=[]
	print(time_t[-1])

	for j in range(1,nt):
		v_max=np.maximum(vol_path,0)
		vol_path=vol_path+kappa*dt*(theta-v_max)+xi*np.sqrt(v_max*dt)*w[:,j-1]
		spot_path=spot_path*np.exp((mu-0.5*v_max)*dt+np.sqrt(v_max*dt)*z[:,j-1])
		payoff_sum+=np.maximum(spot_path-strike,0)
		if((j*b/nt==int(time_t[j]))&(j<180)):
			val_option_price=np.mean(payoff_sum)*np.exp(-mu*time_t[j])
			option_price.append(val_option_price)


	print(option_price)

mp=pd.read_csv("market_datar.csv",delimiter=";")
kappa=6.21
xi=0.61
theta=0.019
rho=-0.7
#nmc=1000
#n=1000
vol_init=0.010201

mc_pricer_fulltr(kappa=kappa,mu=0.0319,theta=theta,xi=xi,rho=rho,vol_init=vol_init,spot_init=100,time_t=np.array(mp.iloc[:,2]),nmc=50,strike=100)



