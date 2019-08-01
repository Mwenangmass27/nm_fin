#----------------------
#ID: *
#NAME: *
#DES: *
#AUTHOR: Malcom WENANG-MASSING
#VERSION: 1.0.0
#DATE: 2016-07-18
#----------------------

#Set python library
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
import Montecarlo as mlo 
import Montecarlo_is as mloi 
import Montecarlo_antithetic as mant
import fd_eulerexp as fdx
import fd_eulerimp as fdi

mu=np.linspace(-0.005,0.04,10,endpoint=True)
s_on_k=np.linspace(0.8,1.2,10,endpoint=True)
sigma=np.linspace(0.1,0.35,10,endpoint=True)
maturity=np.arange(1,8)

perfect_price={}


#for i in mu:
#	for j in s_on_k:
#		for k in sigma:
#			for l in maturity:
#				call=bs.BSanalytic(mu=i,s_on_k=j,sigma=k,maturity=l)
#				perfect_price[i,j,k,l]=call.pricer_put()

mc_opt=mlo.Montecarlo(mu=0.04,s_on_k=0.9,sigma=0.35,maturity=3,nmc=100)
mc_opt1=mloi.Montecarlo_is(mu=0.04,s_on_k=0.9,sigma=0.35,maturity=3,nmc=100)
mc_opt2=mant.Montecarlo_antithetic(mu=0.04,s_on_k=0.9,sigma=0.35,maturity=3,nmc=100)

euler_explicite=fdx.fd_eulerexp(mu=0.04,s_on_k=0.9,sigma=0.35,maturity=3,nt=1000,nx=45,quantile=2.58)
res=euler_explicite.pricer_call()

mc_price=mc_opt.pricer_call()
mc_price1=mc_opt1.pricer_call()
mc_price2=mc_opt2.pricer_call()


print(mc_price)
print(mc_price1)
print(mc_price2)

put=bs.BSanalytic(mu=0.04,s_on_k=0.9,sigma=0.35,maturity=3	)
print(put.pricer_call())
