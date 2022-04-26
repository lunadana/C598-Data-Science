#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 09:36:40 2021

@author: lunadana
"""

import pandas as pd 
import requests
import sys, os
import json
import argparse

# python3 collect_newest.py -o test.json -s /r/concordia 

parser = argparse.ArgumentParser()
parser.add_argument('-o', required=True)
parser.add_argument('-s', required=True)
args = parser.parse_args()
file_out = args.o
subredit = args.s

# Define the two urls
url = "https://www.reddit.com"+subredit+"/new.json?limit=100"

# Open the files
file = requests.get(url, headers={'User-agent': 'Chrome'}).json()["data"]["children"]

f_out = open(file_out, 'w')
for post in file:
    json.dump(post, f_out)
    f_out.write("\n")
f_out.close()






