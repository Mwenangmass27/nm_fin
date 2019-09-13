import numpy as np
from scipy.stats import gamma
import matplotlib.pyplot as plt
import numpy.random as npr

#génération de la densité d'une loi gamma

fig, ax = plt.subplots(1, 1)

a=1.99
'''
x = np.linspace(gamma.ppf(0.01,a),gamma.ppf(0.99, a),100)

ax.plot(x, gamma.pdf(x, a),'r-', lw=5, alpha=0.6, label='gamma pdf')
#rv = gamma(a)
#ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')
'''
samples=[]
def c(x,alpha):
	return x**((alpha-1)*np.exp(-0.5*x))/(2**(alpha-1)*(1-np.exp(-0.5*x))**(alpha-1))
alpha=a

for i in range(100000):
	u=npr.uniform(0,1)
	x=-2*np.log(1-u**(1/alpha))
	v=npr.uniform(0,1)
	if v<c(x,alpha):
		samples.append(x)
s=np.array(samples)
plt.hist(s,bins='auto')
plt.show()
'''

aa=(1-np.exp(-0.5))**alpha/((1-np.exp(-0.5))**alpha+alpha*np.exp(-1)/(2**alpha))
bb=alpha*np.exp(-1)/2**alpha
for i in range(100000):
	u=npr.uniform(0,1)
	if u<aa:
		x=-2*np.log(1-(u*bb)**(1/alpha))
	else:
		x=-np.log((2**alpha/alpha)	*bb*(1-u))
	v=npr.uniform(0,1)
	if x<=1:
		if v<=c(x,alpha):
			samples.append(x)
	else:
		if v<=x**(alpha-1):
			samples.append(x)

s=np.array(samples)
plt.hist(s,bins='auto')
'''