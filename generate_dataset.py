
#! /usr/bin/python

from __future__ import division
import json
from collections import defaultdict
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib.dates as dates
import time
import os

plt.style.use('ggplot')
os.chdir('/Users/deniz/Research/Organized-Hashtags')

startTime = time.time()

def open_data(filename):
    with open(filename) as f:
        ct = json.load(f) 
    return ct
    
                
def write_data(d, filename):
    with open(filename, 'w') as f:
        json.dump(d, f) 
    
hashtag_time = open_data('/Users/deniz/Research/Organized-Hashtags/merged_g1000.json')


hashtag_count = defaultdict(int)
for item in hashtag_time:
    hashtag_count[item] = len(hashtag_time[item])
max_keys = sorted(hashtag_count, key=hashtag_count.get, reverse=True)
    
plt.semilogy([ hashtag_count[i] for i in max_keys])
plt.grid()

endTime = time.time()
print(endTime - startTime)  

df_final = pd.DataFrame()
meanAbsPctChange = np.empty((len(max_keys),1))
meanAbsPctChange[:] = np.NAN
interArrivalTimes = defaultdict(int)

startTime = time.time()
for w1 in range(len(max_keys)):
    w = max_keys[w1]
    times = hashtag_time[w]
    dateIndex1 = pd.to_datetime(times,format='%a %b %d %H:%M:%S +0000 %Y').sort_values()
      
    dateIndex1 = sorted(dateIndex1)
    
    df = pd.DataFrame(data=1, index = dateIndex1, columns=[w])
    df = df.resample('1min').sum()
    df_final = df_final.join(df,how='outer')
    
    difference = np.subtract(dateIndex1[1:],dateIndex1[0:-1])
    interArrivalTimes[w] = sorted([difference[i].seconds for i in range(len(difference))])


meanAbsPctChange = df_final.pct_change().abs().mean()
    
endTime = time.time()
print(endTime - startTime)  

write_data(interArrivalTimes, 'interArrivalTimes.json')
df_final.to_pickle('NumberMentionsPerMinute.pkl') 
meanAbsPctChange.to_pickle('meanAbsPctChange.pkl') 


