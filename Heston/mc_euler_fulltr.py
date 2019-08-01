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




def mc_pricer_fulltr(kappa,mu,theta,xi,rho,time_t,vol_init,spot_init,nmc,n,strike):
#Montecarlo loop
	payoff_sum=0.0
	g=npr.normal(0,1)
	z=npr.normal(0,1)
	w=np.sqrt(1-rho**2)*g+rho*z
	for i in range(nmc):
		dt=time_t/(n-1)
#calc_vol_path and spot_path

		vol_path=vol_init
		spot_path=spot_init
		for j in range(1,n):
			v_max=np.maximum(vol_path,0)
			vol_path=vol_path+kappa*dt*(theta-v_max)+xi*np.sqrt(v_max*dt)*w
			spot_path=spot_path*np.exp((mu-0.5*v_max)*dt+np.sqrt(v_max*dt)*z)
			g=npr.normal(0,1)
			z=npr.normal(0,1)
			w=np.sqrt(1-rho**2)*g+rho*z
		payoff_sum+=np.maximum(spot_path-strike,0)
	option_price=(payoff_sum/nmc)*np.exp(-mu*time_t)

	print(option_price)



mc_pricer_fulltr(6.21,0.0319,0.019,0.61,-0.7,1,0.010201,100,10000,1000,100)

