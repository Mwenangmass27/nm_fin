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

class Montecarlo_is:
#Classe calculant le prix d'une option par la formule de Black-Scholes en fonction:
#-sa valeur initiale
#-du prix d'exercice
#-de la maturité
#-de sa volatilité
#-du taux d'intérêt
#-du nombre de simulations


     def __init__(self,s_on_k,maturity,sigma,mu,nmc):
         self.s_on_k=s_on_k
         self.maturity=maturity
         self.sigma=sigma
         self.mu=mu
         self.nmc=nmc

     def pricer_call(self):
          g=npr.normal(0,1,self.nmc)    
          s=self.s_on_k*np.exp((self.mu-self.sigma**2/2)*self.maturity+self.sigma*np.sqrt(self.maturity)*g)
          wei=np.exp(-0.5*self.mu**2+self.mu*g)
          payoff= np.exp(-self.mu*self.maturity)*np.maximum(s-1,0)*wei
          mc_price_call=np.mean(payoff)
          return mc_price_call

     def pricer_put(self):
          g=npr.normal(0,1,self.nmc)      
          s=self.s_on_k*np.exp((self.mu-self.sigma**2/2)*self.maturity+self.sigma*np.sqrt(self.maturity)*g)
          wei=np.exp(-0.5*self.mu**2+self.mu*g)
          payoff= np.exp(-self.mu*self.maturity)*np.maximum(-s+1,0)*wei
          mc_price_put=np.mean(payoff)
          return mc_price_put

     def pricer_str(self):
          return self.pricer_put(self)+self.pricer_call(self)