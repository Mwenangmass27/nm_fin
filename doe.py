#----------------------
#ID: *
#NAME: *
#DES: *
#AUTHOR: Malcom WENANG-MASSING
#VERSION: 1.0.0
#DATE: 2016-07-18
#----------------------

#Set python library
import csv
import os
import time
import shutil
import subprocess
from datetime import datetime
import glob, os, shutil
import numpy as np
import json
import datetime
import BSanalytic as bs
import matplotlib.pyplot as plt
from   scipy.stats import norm
import sobol_seq
from sobol_seq import i4_sobol, i4_sobol_generate, i4_uniform, i4_bit_hi1, i4_bit_lo0, prime_ge
import BSanalytic as bs
import Montecarlo as mlo 
import Montecarlo_is as mloi 
import Montecarlo_antithetic as mant
import FD_eulerexp as fdx
import FD_eulerimp as fdi
import FD_cn as fdc
import FT_gp_inv as ftg
import pandas as pd 
import copy
from threading import Thread


nb_exp=5
nb_params_mc=5
nb_params_fd=7
nb_params_a=4




#print(sobol)

# Generation du plan d'experience monte carlo
ti=time.time()
sobol=sobol_seq.i4_sobol_generate(nb_params_mc,nb_exp)
data={"s_on_k":[0.8,1.2],"maturity":[1,8],"sigma":[0.10,0.35],"mu":[-0.005,0.04],"nmc":[100,10**5],"nx":[100,10^5],"nt":[100,10**5],"a":[0.01,0.001],"b":[50,55],"n":[1000,10000]}
output={}
for key,values in data.items():
	for j in range(nb_exp):
		for k in range (nb_params_mc):
			tmp=data[key][-1]
			data[key].insert(k+1,data[key][k]+(tmp-data[key][k])*sobol[j,k])

doe=pd.DataFrame(data)
out=pd.DataFrame(output)

for i in doe.itertuples():
	doe.at[i.Index,'analytic value']=(bs.BSanalytic(mu=i.mu,sigma=i.sigma,maturity=i.maturity,s_on_k=i.s_on_k)).pricer_call()	


for i in doe.itertuples():
	start_montecarlo=time.time()
	doe.at[i.Index,'montecarlo']=(mlo.Montecarlo(mu=i.mu,sigma=i.sigma,maturity=i.maturity,s_on_k=i.s_on_k,nmc=int(i.nmc))).pricer_call()
	time_mc=time.time()-start_montecarlo
	out.at[i.Index,"error_mc"]=np.absolute(doe.at[i.Index,"montecarlo"]-doe.at[i.Index,'analytic value'])
	out.at[i.Index,"ctime_mc"]=time_mc


for i in doe.itertuples():
	start_montecarlo_is=time.time()
	doe.at[i.Index,'montecarlo is']=(mloi.Montecarlo_is(mu=i.mu,sigma=i.sigma,maturity=i.maturity,s_on_k=i.s_on_k,nmc=int(i.nmc))).pricer_call()
	time_mc_is=time.time()-start_montecarlo_is
	out.at[i.Index,"error_mc_is"]=np.absolute(doe.at[i.Index,"montecarlo is"]-doe.at[i.Index,'analytic value'])
	out.at[i.Index,"ctime_mc_is"]=time_mc_is

for i in doe.itertuples():
	start_montecarlo_antithetic=time.time()
	doe.at[i.Index,'montecarlo antithetic']=(mant.Montecarlo_antithetic(mu=i.mu,sigma=i.sigma,maturity=i.maturity,s_on_k=i.s_on_k,nmc=int(i.nmc))).pricer_call()
	time_mc_antithetic=time.time()-start_montecarlo_antithetic
	out.at[i.Index,"error_mc_antithetic"]=np.absolute(doe.at[i.Index,"montecarlo antithetic"]-doe.at[i.Index,'analytic value'])
	out.at[i.Index,"ctime_mc_antithetic"]=time_mc_antithetic

for i in doe.itertuples():
	start_eulerexp=time.time()
	doe.at[i.Index,'euler explicite']=(fdx.FD_eulerexp(mu=i.mu,sigma=i.sigma,maturity=i.maturity,s_on_k=i.s_on_k,nx=int(i.nx),nt=int(i.nt))).pricer_call()
	time_eulerexp=time.time()-start_eulerexp
	out.at[i.Index,"error_eexp"]=np.absolute(doe.at[i.Index,"euler explicite"]-doe.at[i.Index,'analytic value'])
	out.at[i.Index,"ctime_eulerexp"]=time_eulerexp


for i in doe.itertuples():
	start_eulerimp=time.time()
	doe.at[i.Index,'euler implicite']=(fdi.FD_eulerimp(mu=i.mu,sigma=i.sigma,maturity=i.maturity,s_on_k=i.s_on_k,nx=int(i.nx),nt=int(i.nt))).pricer_call()
	time_eulerimp=time.time()-start_eulerimp
	out.at[i.Index,"error_eimp"]=np.absolute(doe.at[i.Index,"euler implicite"]-doe.at[i.Index,'analytic value'])
	out.at[i.Index,"ctime_eulerimp"]=time_eulerimp

for i in doe.itertuples():
	start_cn=time.time()
	doe.at[i.Index,'crank nicolson']=(fdc.FD_cn(mu=i.mu,sigma=i.sigma,maturity=i.maturity,s_on_k=i.s_on_k,nx=int(i.nx),nt=int(i.nt))).pricer_call()
	time_cn=time.time()-start_cn
	out.at[i.Index,"error_cn"]=np.absolute(doe.at[i.Index,"crank nicolson"]-doe.at[i.Index,'analytic value'])
	out.at[i.Index,"ctime_cn"]=time_cn


for i in doe.itertuples():
	start_fourier_gil=time.time()
	doe.at[i.Index,'ft_gilp']=(ftg.FT_gp_inv(mu=i.mu,sigma=i.sigma,maturity=i.maturity,s_on_k=i.s_on_k,n=int(i.n),a=i.a,b=i.b)).pricer_call()
	time_fourier_gil=time.time()-start_fourier_gil
	out.at[i.Index,"error fourier gp"]=np.absolute(doe.at[i.Index,"ft_gilp"]-doe.at[i.Index,'analytic value'])
	out.at[i.Index,"ctime fourier gp"]=time_fourier_gil


desc=out.describe()
#print(doe.tail(5))
doe.to_csv("./doe.csv")
out.to_csv("./out.csv")
desc.to_csv("./desc.csv")
print("Temps d'éxécution: %s secondes " % (time.time()-ti))