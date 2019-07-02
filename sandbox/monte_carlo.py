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

def f(T,S0,K,r,sigma,n): #prix call
    St = S0*np.exp((r-(sigma**2)/2)*T + sigma*np.sqrt(T)*npr.normal(size=n)) ;
    tmp = np.maximum(St-K,0) ;
    tmp = tmp*np.exp(-r*T) ;
    St = tmp ;
    prix_mc = np.mean(St) ;
    ecart_type = np.std(St,ddof=1) ;
    IC_down = prix_mc - 1.96*ecart_type/np.sqrt(n) ;
    IC_up = prix_mc + 1.96*ecart_type/np.sqrt(n) ;
    erreur = 1.96*ecart_type/np.sqrt(n)
    return prix_mc,IC_down,IC_up,erreur

def g(T,S0,K,r,sigma,n): #prix put
    St = S0*np.exp((r-(sigma**2)/2)*T + sigma*np.sqrt(T)*npr.normal(size=n)) ;
    tmp = np.maximum(K-St,0) ;
    tmp = tmp*np.exp(-r*T) ;
    St = tmp ;
    prix_mc = np.mean(St) ;
    ecart_type = np.std(St,ddof=1) ;
    IC_down = prix_mc - 1.96*ecart_type/np.sqrt(n) ;
    IC_up = prix_mc + 1.96*ecart_type/np.sqrt(n) ;
    erreur = 1.96*ecart_type/np.sqrt(n)
    return prix_mc,IC_down,IC_up,erreur

prix_call = f(T,S0,K,r,sigma,n)
print(prix_call)

prix_put = g(T,S0,K,r,sigma,n)
print(prix_put)