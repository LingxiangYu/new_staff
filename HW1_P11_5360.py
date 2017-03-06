# HW1_P11_5360
from astropy.io import ascii
import numpy as np 
import pandas as pd 
from __future__ import division
import time
import matplotlib.pyplot as plt

t1 = time.time()
data = ascii.read("ES.asc")
data = data.to_pandas()
#data.head(n=10)
data1 = data.head(n=1000000)

diff_ratio = pd.DataFrame(np.nan, index=np.arange(1000000), columns=np.arange(1000))
t2 = time.time()
t2 - t1

t3 = time.time()
for i in range(1, 1001):
	data1_temp = data1['Close'].shift(i)
	diff_temp = (data1['Close'] - data1_temp)/data1_temp
	diff_ratio.loc[:][i-1] = diff_temp
t4 = time.time()
t4 - t3

sigma_tau = np.std(diff_ratio, axis=0)

plt.subplot(2,1,1)
tau = np.arange(1, 1001, 1)
plt.plot(tau, sigma_tau)
plt.title('lin-lin')

plt.subplot(2,1,2)
plt.loglog(tau, sigma_tau, 'ro')
plt.title('log-log')

plt.show()

# lines below are about different versions of linear regression 
import statsmodels.api as sm
results = sm.OLS(np.log10(sigma_tau), np.log10(tau)).fit()

from scipy import stats
results1 = stats.linregress(sigma_tau, tau)
results2 = stats.linregress(np.log10(sigma_tau), np.log10(tau))

