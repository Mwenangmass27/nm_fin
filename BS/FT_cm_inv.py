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


class FT_cm_inv:
	def __init__(self,s_on_k,maturity,sigma,mu,n):
		self.s_on_k=s_on_k
		self.maturity=maturity
		self.sigma=sigma
		self.mu=mu
		self.n=n


	def pricer_call(self):	