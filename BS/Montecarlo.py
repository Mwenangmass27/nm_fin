#----------------------
#ID: *
#NAME: *
#DES: *
#AUTHOR: Malcom WENANG-MASSING
#VERSION: 1.0.0
#DATE: 2016-07-18
#----------------------

#Set python library
import numpy as np 
import numpy.random as npr
from   scipy.stats import norm
import matplotlib.pyplot as plt

class Montecarlo:


     def __init__(self,s_on_k,maturity,sigma,mu,nmc):
          self.s_on_k=s_on_k
          self.maturity=maturity
          self.sigma=sigma
          self.mu=mu
          self.nmc=nmc

     def pricer_call(self):
          g=npr.normal(0,1,self.nmc)
      
          s=self.s_on_k*np.exp((self.mu-self.sigma**2/2)*self.maturity+self.sigma*np.sqrt(self.maturity)*g)
          payoff= np.exp(-self.mu*self.maturity)*np.maximum(s-1,0)

          mc_price_call=np.mean(payoff)
          return mc_price_call

     def pricer_put(self):
          g=npr.normal(0,1,self.nmc)
      
          s=self.s_on_k*np.exp((self.mu-self.sigma**2/2)*self.maturity+self.sigma*np.sqrt(self.maturity)*g)
          payoff= np.exp(-self.mu*self.maturity)*np.maximum(-s+1,0)

          mc_price_put=np.mean(payoff)
          return mc_price_put

     def pricer_str(self):

          return self.pricer_put(self)+self.pricer_call(self)