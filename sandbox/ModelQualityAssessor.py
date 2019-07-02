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
import lib.Pricer as pr 

class ModelQualityAssessor:
"Cette classe compare différentes manières de pricer une option"

def _init_(self)
	self.reference=None
	self.operand=None

def perfect_price_Call(self)
	return self.reference.Pricer_Call()

def perfect_price_Put(self)
	return self.reference.Pricer_Put()

def AssessPricer_Call(self)
	start=time.time()
	price=self.operand.Pricer_Call()
	computing_time=time.time()-start
	output = {
		"price": price,
		"error": np.abs(price-self.perfect_price_Call()),
		"computing_time": computing_time,
	}
	return output

def AssessPricer_Put(self)
	start=time.time()
	price=self.operand.Pricer_Put()
	computing_time=time.time()-start
	output = {
		"price": price,
		"error": np.abs(price-self.perfect_price_Put()),
		"computing_time": computing_time,
	}
	return output


#def main(input_file,output_file):
#	open input_file
#	pour chaque ligne
#		if(methode== monterlae)
#			pricer montecarlo





#if __name__ == '__main__':
#	main()







	


