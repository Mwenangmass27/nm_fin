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
from scipy.optimize import leastsq
from numpy.linalg import norm
from descent import grad_descent

#Ce script calcule les prix pour des valeurs données et calcule un optimum qui n'est pas acceptable car la vol_init est négative

#fonction auxiliaire
def get_ind(tab):
	ind_tab=[]
	for j in range(len(tab)):
		ind_tab.append(50*tab[j])
	return ind_tab

#initialisation du jeu de données d'entrées 
mp=pd.read_csv("market_datar.csv",delimiter=";")
kappa=3.66927696 #6.21
xi=1.12853699 #0.61
theta=0.06350197 #0.019
rho=-0.7
vol_init=-0.09802954#0.010201
nmc=50
strike=100

time_t=np.array(mp.iloc[:,2])
spots=np.array(mp.iloc[:,-4])
mus=np.array(mp.iloc[:,3])
market_prices=np.array(mp.iloc[:,-3])

new_time=[]
tmp=0
for i in range(len(time_t)):
	if(time_t[i]!=tmp):
		new_time.append(time_t[i])
		tmp=new_time[-1]

mod_time=get_ind(new_time)
nt=int(mod_time[-1])
dt=time_t[-1]/nt

g=npr.normal(0,1,(nmc,nt))
z=npr.normal(0,1,(nmc,nt))
w=np.sqrt(1-rho**2)*g+rho*z



def std_scheme(kappa,mu,theta,xi,dt,norm_matrix,corr_norm_matrix,ind_mc,strike,vol_init,spot_init):
	vol_path=vol_init
	spot_path=spot_init
	payoff_sum=0
	for j in range(norm_matrix.shape[0]):
		v_max=np.maximum(vol_path,0)
		vol_path=vol_path+kappa*dt*(theta-v_max)+xi*np.sqrt(v_max*dt)*norm_matrix[ind_mc,j-1]
		spot_path=spot_path*np.exp((mu-0.5*v_max)*dt+np.sqrt(v_max*dt)*corr_norm_matrix[ind_mc,j-1])
	payoff_sum+=np.maximum(spot_path-strike,0)
	return payoff_sum

#boucle de Montecarlo
def mc_pricer_fulltr(kappa,mu,theta,xi,dt,norm_matrix,corr_norm_matrix,vol_init,spot_init,nmc,strike,ind_time):
#Montecarlo loop
#	npr.seed(777) #JACKPOT
	payoff_sum=0
	for ind_mc in range(nmc):
		payoff_sum+=std_scheme(kappa,mu,theta,xi,dt,norm_matrix,corr_norm_matrix,ind_mc,strike,vol_init,spot_init)
	option_price=(payoff_sum/nmc)*np.exp(-mu*ind_time)
	return option_price

#	print(option_price)

#Fonction principale du pricer
def pricer(kappa,mu,theta,xi,rho,time_t,vol_init,spot_init,nmc,strike,dt,g,w):
	prices=[]

	for j in range(len(time_t)):
		prices.append(mc_pricer_fulltr(kappa,mu[j],theta,xi,dt,g,w,vol_init,spot_init[j],nmc,strike,time_t[j]))
	return prices

#fonction d'entrée de la méthode d'optimisation leastsq de scipy.optimize
def heston_eval(x):
	kappa=x[0]
	theta=x[1]
	xi=x[2]
	vol_init=x[3]
	rho=x[4]
	return pricer(kappa=kappa,theta=theta,xi=xi,vol_init=vol_init,rho=rho,mu=mus,dt=dt,g=g,w=w,nmc=nmc,strike=100,time_t=time_t,spot_init=spots)-market_prices

x0=[kappa,theta,xi,vol_init,rho]
plsq=leastsq(heston_eval,x0)
print(plsq)
'''

tab=pricer(kappa=kappa,mu=mus,theta=theta,xi=xi,rho=rho,vol_init=vol_init,spot_init=spots,time_t=time_t,nmc=50,strike=100,g=g,w=w,dt=dt)

print(tab)

#out=pd.DataFrame(tab)
#out.to_csv("./outhes.csv")
'''
