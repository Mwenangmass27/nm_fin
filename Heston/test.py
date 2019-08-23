import os
import time
import shutil
import subprocess
from datetime import datetime
import glob, os, shutil
import numpy as np
import json
import datetime
import matplotlib.pyplot as plt
import numpy.random as npr
import closedform as cf


call=cf.FT_H(maturity=1,mu=0.0319,kappa=6.21,xi=0.61,theta=0.019,rho=-0.7,vol_init=0.010201,spot_init=100)
print(call.pricercall(0,50,10000))
#print(np.exp(-call.maturity*call.mu))