#Final Project--Break-out--Coca strategy

#import library
import urllib2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

""" download data
url = 'http://chart.finance.yahoo.com/table.csv?s=KO&a=0&b=1&c=2014&d=3&e=15&f=2017&g=d&ignore=.csv'
response = urllib2.urlopen(url)
html = response.read()
with open('coca.csv', 'wb') as f:
    f.write(html)
"""

#read data
data = pd.read_csv('coca.csv')
data = data.reindex(index=data.index[::-1])
data.index = range(827)
print data.head()

#define variables
initial_value = 1000000 #trade size--1000 shares of coca 'KO' stock, assume I have enough fund to buy 1000 shares
mp = 0 #market position--indicate wheter I have any KO stocks on hands: 0 means none shares; 1 menas have shares
iD = 0 #initial date--indicate the index of the first date during calculation 
Ratio = np.zeros((51,2)) #profit ratio
    
#define functions
def min_per_day(x):
    y = data.iloc[x].as_matrix()
    mpd = y[1:4].min()
    return mpd

def close_p(x):
    cp = data.iloc[x][4]
    return cp

def open_p(x):
    op = data.iloc[x][1]
    return op

#the main loop for trading
for k in range(51):
    iD = 0
    initial_value = 1000000
    Stop_pct = 0.005 + k * 0.0001
    while (iD <= 820):        
        if mp == 0:
            df_temp = data[iD:iD+5]
            HH = df_temp['High'].max()
            print HH
            iD = iD + 5
#            test = iD

#            for n in range(0,5):
#                if HH < open_p(iD+n):
#                    break
#            if test + 4 == iD + n:
#                iD = iD + n + 1
#                mp = 0

#            else:
#                iD = iD + n
            while HH > open_p(iD) and iD<=820:
                iD += 1
            print iD
            ep = open_p(iD) #ep is entry price
            print ep
            Ts = initial_value / ep
            print Ts
            pp = ep #pp is the previous peak price
            mp = 1

        if mp == 1:
            if close_p(iD) > pp:
                pp = close_p(iD)
            print pp
            sp = pp * (1 - Stop_pct) #sp is the stop-point of trading, shares sold at this price
            iD = iD + 1

            while sp < min_per_day(iD) and iD<=820:
                iD = iD + 1
            print iD
            end_value = open_p(iD) * Ts #the value of my fund after selling all shares
            print open_p(iD),end_value
            initial_value = end_value
            mp = 0
#    if mp == 1:
#        end_value = sp * Ts
#    if mp == 0:
#        end_value = initial_value

    
    Ratio[k][0] = Stop_pct
    Ratio[k][1] = (end_value - 1000000)/1000000
    
#    mp = 0
#    iD = 0
    #break

#Chart and Figure
Return_Ratio = pd.DataFrame({'Stop Precent':Ratio[:,0],'Return Ratio':Ratio[:,1],})
Return_Ratio = Return_Ratio[['Stop Precent','Return Ratio']]
Return_Ratio

fig, ax = plt.subplots()
ax.plot(Ratio[:,0],Ratio[:,1])
ax.set_title('Coca Return Ratio')
plt.show()

