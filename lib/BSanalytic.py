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

class BSanalytic:
#Classe calculant le prix d'une option par la formule de Black-Scholes en fonction:
#-sa valeur initiale
#-du prix d'exercice
#de la maturité
#de sa volatilité
#du taux d'intérêt
 
     def __init__(self,s_on_k,maturity,sigma,mu):
          self.s_on_k=s_on_k
          self.maturity=maturity
          self.sigma=sigma
          self.mu=mu

     def pricer_call(self):

          d1=(1/(self.sigma*np.sqrt(self.maturity)))*(np.log(self.s_on_k)+(self.mu+0.5*self.sigma**2*self.maturity))
          d2=d1-self.sigma*np.sqrt(self.maturity)
     
          vrai_prix=self.s_on_k*norm.cdf(d1)-np.exp(-self.mu*self.maturity)*norm.cdf(d2)
          return vrai_prix

     def pricer_put(self):
	 
          d1=(1/(self.sigma*np.sqrt(self.maturity)))*(np.log(self.s_on_k)+(self.mu+0.5*self.sigma**2*self.maturity))
          d2=d1-self.sigma*np.sqrt(self.maturity)
   
          vrai_prix=-self.s_on_k*norm.cdf(-d1)+np.exp(-self.mu*self.maturity)*norm.cdf(-d2)
          return vrai_prix

     def pricer_str(sekf):
          return self.pricer_put(self)+self.pricer_call(self)

