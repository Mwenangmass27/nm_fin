#----------------------
#ID: *
#NAME: *
#DES: *
#AUTHOR: Alexandre LE MAISTRE
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
import lib.BSPricerAnalyticFormula as bs

#import des pricer

def bs_price_analytic_formula(mu,sigma,s_on_k,maturity,perfect_price):
    start = datetime.datetime.now()
    price=bs.Pricer_Call(mu,sigma,s_on_k,maturity,perfect_price)
    end = datetime.datetime.now()    
    # appel au pricer
    output={
        "price": price,
        "error": price-perfect_price,
        "computing_time": -1
    }
    return output

def bs_price_montecarlo(mu,sigma,s_on_k,maturity,perfect_price,Nt,nmc,useAntitetic,seed):
    output={
        "price": 2.0,
        "error": 2.0,
        "computing_time": 2.0}
    return output

def bs_price_fd_euler(mu,sigma,s_on_k,maturity,perfect_price,dt,dS):
    output = {

    # Definition des constantes de l ’EDP
    alpha =float(sigma)**2/2
    beta =float(r)-alpha
    gamma=-float(r)
    # Definition des coefficients de la matrice explicite 
    ksi1 = dt*(alpha/(dS**2) + beta/(2*dS));
    ksi2 = 1 + dt*(gamma-2*alpha/(dS**2));
    ksi3 = dt*(alpha/(dS**2)-beta/(2*dx));

    }
    return output

def bs_price_fd_crank_nicolson(mu,sigma,s_on_k,maturity,perfect_price,dt,dS):
    output={
        "price":2.0,
        "error": 2.0,
        "computing_time": 2.0
    }
    return output

def generate_design_of_experiment(outputfile) :
    mu=np.arange(-0.5,0.04,0.0005)
    s_on_k=np.arange(0.8,1.2,0.05)
    sigma=np.arange(0.1,0.35,0.025)
    maturity=np.arange(1,8)
    methods=["montecarlo","montecarlo_antithetic","fd_eulerexp","fd_eulerimp","fd_cn","fe_1deg","fourier"]
    option_type=["Call","Put","Straddle"]
    f = open(outputfile)

    for i in mu:
        for j in s_on_k:
            for k in sigma:
                for l in maturity:
                    for m in methods:
                        for n in option_type:
                            f.write(i+","+j+","+k+","+l+","+m+","+n+"\n")







def exectute_design_of_experiment(inputfile,outfile_path) :
    f = open(inputfile)
    outout_list=[]
    rows = f.readlines()
    for l_row in rows:
        l_row_arr=l_row.split(",")
        if(l_row_arr[1]=="analytics"):
            mu=float(l_row_arr[2])
            sigma=float(l_row_arr[3])
            s_on_k=float(l_row_arr[4])
            maturity=float(l_row_arr[5])
            perfect_price=0.0
            out=bs_price_analytic_formula(mu, sigma, s_on_k, maturity, perfect_price)
            outout_list.append(out)
        if (l_row_arr[1] == "montecarlo"):
            out = bs_price_montecarlo(l_row_arr[2], l_row_arr[2], 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
            outout_list.append(out)
    outputfile= open(outfile_path,"w+")
  
    outputfile.write(json.dumps(outout_list, sort_keys=True, indent=4))               

def main() :
  if True :
      generate_design_of_experiment("./data/doe.csv")
  if True:
      exectute_design_of_experiment("./data/doe.csv","./data/results.csv")

if __name__ == '__main__':
    main()









