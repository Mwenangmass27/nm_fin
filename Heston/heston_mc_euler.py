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




def mc_pricer_heston(kappa,mu,theta,xi,rho,time_t,vol_init,spot_init,nmc,n):
#Montecarlo loop
	payoff_sum=0.0
	for i in range(nmc):


		npr.seed(77)
		dt=time_t/n
		g=npr.normal(0,1,n)

		z=npr.normal(0,1,n)
		w=np.sqrt(1-rho**2)*g+rho*z

#calc_vol_path and spot_path

		vol_path=np.zeros(n+1)
		spot_path=np.zeros(n+1)
		vol_path[0]=vol_init
		spot_path[0]=spot_init
		for j in range(1,n+1):
			v_max=np.maximum(vol_path[j-1],0)
			vol_path[j]=vol_path[j-1]+kappa*dt*(theta-v_max)+xi*np.sqrt(v_max*dt)*w[j-1]
			spot_path[j]=spot_path[j-1]+(mu-0.5*v_max)*dt+np.sqrt(v_max*dt)*z[j-1]
		payoff_sum+=spot_path[n]

	option_price=(payoff_sum/nmc)*np.exp(-mu*time_t)
	print(option_price)



mc_pricer_heston(6.21,0.0319,0.019,0.61,-0.7,1,0.010201,100,1500,1000)

