# HW1_P11_5360
######################################################
# none of the various versions of linear regression  #
# give me the same coeffes or statistics inference.  #
# The reason is that there multi-colinear variables  #
# and they couldn't be removed by the codes below.   #
# On the contrary, R can remove colinear problem     #
# automatically, which is awesome. Hence, in the     #
# future, it's possible that I use python to modify  #
# data or run loops and then use R to gain satistics #
# analysis.                                          #
######################################################

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

## write the linear reg 
sigma_tau = np.reshape(sigma_tau, (len(sigma_tau), 1))
tau = np.reshape(tau, (len(tau),1))

from sklearn import linear_model
sigma_tau_train = sigma_tau[0:int(len(sigma_tau)*0.8)]
sigma_tau_test = sigma_tau[int(len(sigma_tau)*0.8):]
sigma_tau_train = np.reshape(sigma_tau_train, (len(sigma_tau_train),1))
sigma_tau_test = np.reshape(sigma_tau_test, (len(sigma_tau_test),1))

tau_train = tau[0:int(len(tau)*0.8)]
tau_test = tau[int(len(tau)*0.8):]
tau_train = np.reshape(tau_train, (len(tau_train), 1))
tau_test = np.reshape(tau_test, (len(tau_test), 1))

results3 = linear_model.LinearRegression()
results3.fit(sigma_tau_train, tau_train)
results4 = linear_model.LinearRegression()
results4.fit(np.log10(sigma_tau_train), np.log10(tau_train))

print('Coefficients of linlin: \n', results3.coef_)
print("Mean squared error of linlin: %.2f" % np.mean((results3.predict(sigma_tau_test) - tau_test) ** 2))

print 'Coeffs of loglog ', results4.coef_
print 'R Squared of loglog: ', np.mean((results4.predict(np.log10(sigma_tau_test)) - np.log10(tau_test)) ** 2)

