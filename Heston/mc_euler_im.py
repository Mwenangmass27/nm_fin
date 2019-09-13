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




def mc_pricer_im(kappa,mu,theta,xi,rho,time_t,vol_init,spot_init,nmc,strike):
#Montecarlo loop
	nt=np.maximum(spot_init)*50
	dt=1/50
	g=npr.normal(0,1,(nmc,nt))
	z=npr.normal(0,1,(nmc,nt))
	w=np.sqrt(1-rho**2)*g+rho*z
#calc_vol_path and spot_path

	vol_path=vol_init*np.ones((nmc,1))
	spot_path=spot_init*np.ones((nmc,1))

	for j in range(1,n):
		v_max=np.maximum(vol_path,0)
		vol_path=(vol_path+kappa*dt*theta+xi*np.sqrt(v_max*dt)*w+xi**2/4*dt*(w**2-1))/(1+kappa*dt)
		vp_max=np.maximum(vol_path,0)
		spot_path=spot_path*np.exp((mu-0.25*(v_max+vp_max))*dt+rho*np.sqrt(v_max*dt)*w+0.5*(np.sqrt(vp_max)+np.sqrt(v_max))*(z-rho*w)*np.sqrt(dt)+xi*rho*0.25*dt*(w**2-1))
		g=npr.normal(0,1)
		z=npr.normal(0,1)
		w=np.sqrt(1-rho**2)*g+rho*z
		payoff_sum+=np.maximum(spot_path-strike,0)
	option_price=(payoff_sum/nmc)*np.exp(-mu*time_t)
	return option_price



#mc_pricer_im(6.21,0.0319,0.019,0.61,-0.7,1,0.010201,100,10000,1000,100)