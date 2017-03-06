# HW1_P11_5360

from astropy.io import ascii
import numpy as np 
import pandas as pd 
from __future__ import division
import time

data = ascii.read("ES.asc")
data = data.to_pandas()
#data.head(n=10)
data1 = data.head(n=10000)

diff_ratio = pd.DataFrame(np.nan, index=np.arange(10000), columns=np.arange(1000))
t0 = time.time()
for i in range(0, 999):
	for j in range(0, 9999):
		if j > i:
			diff_ratio.loc[j][i] = (data1.iloc[j]['Close'] - data1.iloc[j-i-1]['Close'])/data.iloc[j-i-1]['Close']
t1 = time.time()
print total = t1 - t0

#diff_ratio.head(n=100)

