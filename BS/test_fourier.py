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
import matplotlib.pyplot as plt
from   scipy.stats import norm
import scipy
import FT_gp_inv as ftg
import Montecarlo as mlo 

mc_opt=mlo.Montecarlo(mu=0.04,s_on_k=0.85,sigma=0.35,maturity=1,nmc=10000)
ft=ftg.FT_gp_inv(mu=0.04,s_on_k=0.85,sigma=0.35,maturity=1,n=10000,a=0.00000001,b=60)
#print(ft.pi_1())
#print(ft.pi_2())

ft_price=ft.pricer_call()

mc_price=mc_opt.pricer_call()
print(mc_price)
print(ft_price)
