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

class BSPricer(Pricer):
"Classe qui définit un pricer pour le modèle de Black-Scholes"

def _init(self)
	Pricer._init_(self)
	self.S0=0
	self.K=0
	self.T=0
	self.sigma=0
	self.mu=0

def InitializePricer(S0,K,T,sigma,mu,self)
	self.SO=S0
	self.K=K
	self.T=T
	self.sigma=sigma
	self.mu=mu


