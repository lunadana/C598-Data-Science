#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 13:55:49 2021

@author: lunadana
"""

import pandas as pd 

# ---------------- 1. Data Collection ----------------
# import csv
print("reading csv")
raw_df = pd.read_csv("https://raw.githubusercontent.com/fivethirtyeight/russian-troll-tweets/master/IRAhandle_tweets_1.csv",nrows = 10000)
print("done")

# Only keep tweets in english
df = raw_df.loc[raw_df["language"] == "English"]

# Remove question 
df = df[df["content"].str.find("?") < 1]
col = df
# ---------------- 2. Data Annotation ----------------

# Keep tweets with Trump mention
df["trump_mention"] = df.content.str.contains("Trump")

# Only keep relevant columns 
df = df[["tweet_id", "publish_date", "content","trump_mention"]]
ano = df
# Save as tsv
df.to_csv("/Users/lunadana/Desktop/comp598-2021-main/hw1/submission_template/data/dataset.tsv", sep = '\t', index=False)

# ---------------- 3. Analysis ----------------

percentage_contains_trump = len(df)/len(raw_df)*100

df_frac = pd.DataFrame(columns = ["result","value"])
df_frac = df_frac.append({'result': "frac-trump-mentions", "value" : percentage_contains_trump}, ignore_index=True)
df_frac.to_csv("/Users/lunadana/Desktop/comp598-2021-main/hw1/submission_template/data/results.tsv", sep = '\t', index=False)





