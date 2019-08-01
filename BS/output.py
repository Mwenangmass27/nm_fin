#----------------------
#ID: *
#NAME: *
#DES: *
#AUTHOR: Malcom WENANG-MASSING
#VERSION: 1.0.0
#DATE: 2016-07-18
#----------------------

#Set python library
import csv
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
import sobol_seq
from sobol_seq import i4_sobol, i4_sobol_generate, i4_uniform, i4_bit_hi1, i4_bit_lo0, prime_ge
import BSanalytic as bs
import Montecarlo as mlo 
import Montecarlo_is as mloi 
import Montecarlo_antithetic as mant
import fd_eulerexp as fdx
import fd_eulerimp as fdi
import pandas as pd 
import copy
from threading import Thread

import doe

doe_df=pd.read_csv('/Users/malcom/Documents/Stage/Codes/nm_fin/lib/doe.csv')




