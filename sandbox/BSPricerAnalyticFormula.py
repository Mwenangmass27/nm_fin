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

class BSPricerAnalyticFormula(BSPricer):
"Classe calculant le prix d'une option par la formule de Black-Scholes en fonction:"
"-sa valeur initiale"
"-du prix d'exercice"
"de la maturité"
"de sa volatilité"
"du taux d'intérêt"

def _init_(sekf)
	Pricer._init_(self)

def Pricer_Call(self)

     d1=(1/(self.sigma*np.sqrt(self.T)))*(np.log(self.S0/self.K)+(self.mu+0.5*self.sigma**2*self.T))
     d2=d1-self.sigma*np.sqrt(self.T)
     
     Vrai_prix=self.S0*norm.cdf(d1)-self.K*np.exp(-self.mu*self.T)*norm.cdf(d2)
     return Vrai_prix

def Pricer_Put(self)
	 
	 d1=(1/(self.sigma*np.sqrt(self.T)))*(np.log(self.S0/self.K)+(self.mu+0.5*self.sigma**2*self.T))
     d2=d1-self.sigma*np.sqrt(self.T)
   
     Vrai_prix=-self.S0*norm.cdf(-d1)+self.K*np.exp(-self.mu*self.T)*norm.cdf(-d2)
     return Vrai_prix


