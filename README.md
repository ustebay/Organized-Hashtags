# Analysis of Twitter hashtags

In this project I analyse Twitter data to identify characteristics of hashtags produced by automated or organized sources.

I collected tweets using the Twitter API for three months at the end of 2013. I then stripped hashtags from these tweets and concentrated on the time behaviour hashtags mentioned at least 1000 times in this period.

Originally I concentrated on Turkish hashtags because at the time they were frequently appearing in the world wide trending topics section. But there seems to be other hashtags with similar behaviour. (I labeled Turkish hashtags by hand.)

Recently similar arguments were made for tweets published during the US elections. Kollanyi et al 2016 tries to identify bots on 3 days of hashtag data around the third presedential debate.


##### Files:
twitterstream.py: Collect tweets (Note that I removed my Twitter developer credentials from the file, you need to enter yours to make this run)

hashtags.py: Strip the hashtags and write hashtag dictionary (hashtag:mention timestamps) in a json file

generate_dataset.py: Create time series for the hashtags

analysis.ipynb: Analyze the data by defining a metric of burstiness

