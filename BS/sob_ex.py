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
import fd_eulerexp as fdx
import fd_eulerimp as fdi
import pandas as pd 
import copy
from threading import Thread


nb_exp=50
nb_params_mc=5
nb_params_fd=7
nb_params_a=4




#print(sobol)

# Generation du plan d'experience monte carlo
ti=time.time()
sobol=sobol_seq.i4_sobol_generate(nb_params_mc,nb_exp)
data={"s_on_k":[0.8,1.2],"maturity":[1,8],"sigma":[0.10,0.35],"mu":[-0.5,0.04],"nmc":[100,10**5],"nx":[100,10^5],"nt":[100,10**5]}
output={"error_mc":[],"error_mc_is":[],"error_mc_antithetic":[],"error_eexp":[],"error_eimp":[],"ctime_mc":[],"ctime_mc_is":[],"ctime_mc_antithetic":[],"ctime_eexp":[],"ctime_eimp":[]}
for key in data.keys():
	for j in range(nb_exp):
		for k in range (nb_params_mc):
			tmp=data[key][-1]
			data[key].insert(k+1,data[key][k]+(tmp-data[key][k])*sobol[j,k])