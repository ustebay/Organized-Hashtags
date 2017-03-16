#! /usr/bin/python

from __future__ import division
import json, sys
from collections import defaultdict
import codecs
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib.dates as dates

sys.stdout = codecs.getwriter('utf-8')(sys.stdout)


__author__="Deniz Ustebay"
__date__ ="$Apr 6, 2013"


def read_tweets(tweetsfile,hashtag_time):
    i = 0
    for t in open(tweetsfile):
        try:
            tree = json.loads(t)        
            if 'entities' in tree:
                if tree['entities']['hashtags']:
                    hashtag = tree['entities']['hashtags'][0]['text']
                    hashtag_time[hashtag].append(tree['created_at'])
        except OSError, e:
            print e
            continue

    return hashtag_time
    

def get_freq(filename):
    hashtag_time = defaultdict(list)
    hashtag_time = read_tweets(filename,hashtag_time)
    return hashtag_time    
    
    
            
def write_data(hashtag_time):
    with open('my_dict4.json', 'w') as f:
        json.dump(hashtag_time, f) 
    


def usage():
    sys.stderr.write("""python hashtags.py <tweet_file>""")

if __name__ == "__main__":

    if len(sys.argv)!=2: # Expect exactly two arguments
        usage()
        sys.exit(2)
    try:
        tweet_file = sys.argv[1]
    except IOError:
        sys.stderr.write("ERROR: Cannot read inputfile %s.\n" % arg)
        sys.exit(1)
        
    ct = get_freq(tweet_file)
    write_data(ct)

