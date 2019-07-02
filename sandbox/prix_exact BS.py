#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 2019

@author: 11317832
"""
import numpy as np 
import numpy.random as npr
from   scipy.stats import norm
import matplotlib.pyplot as plt

S0=100;
K=100;
r=np.log(1.1);
sigma=0.2;
T=1;
n=100;
#npr.seed(777)

def Prix_Call_Exact_BS(S0,K,T,sigma,r)

     d1=(1/(sigma*np.sqrt(T)))*(np.log(S0/K)+(r+0.5*sigma**2*T))
     d2=d1-sigma*np.sqrt(T)
     
     Vrai_prix=S0*norm.cdf(d1)-K*np.exp(-r*T)*norm.cdf(d2)
     return Vrai_prix


def Prix_Put_Exact_BS(S0,K,T,sigma,r)

     d1=(1/(sigma*np.sqrt(T)))*(np.log(S0/K)+(r+0.5*sigma**2*T))
     d2=d1-sigma*np.sqrt(T)
     
     Vrai_prix=-S0*norm.cdf(-d1)+K*np.exp(-r*T)*norm.cdf(-d2)
     return Vrai_prix


