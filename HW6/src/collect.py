# -*- coding: utf-8 -*-

import requests
import json
import os

sample_url_h = "https://www.reddit.com/r/"
sample_url_t = "/new.json?limit=100"

# URLs Samples
sample1_words = ["funny","AskReddit","gaming""aww","pics",
                 "Music","science","worldnews","videos","todayilearned"]
sample2_words = ["memes","politics","nfl","nba",
                 "wallstreetbets","teenagers","PublicFreakout",
                 "leagueoflegends","unpopularopinion"]

# lists of urls
URL_subsribers = [sample_url_h+x+sample_url_t for x in sample1_words]
URL_postsbyday = [sample_url_h+x+sample_url_t for x in sample2_words]
Cache_subsribers = ["reddit_data_"+x+".json"for x in sample1_words]
Cache_postsbyday = ["reddit_data_"+x+".json" for x in sample2_words]
sample_1_outputfile = "sample1.json"
sample_2_outputfile = "sample2.json"

# Function to write the posts
def writeposts(output_f, list_files):
    list_posts = []
    for file in list_files:
        with open(file, 'r') as f:
            posts = json.load(f)["data"]["children"]
            list_posts.append(posts)
    f_out = open(output_f, 'w')
    for sub_list in list_posts:
        for post in sub_list:
            json.dump(post, f_out)
            f_out.write("\n")
    f_out.close()

# Function to check if the cache already exists
def checkaddressexists(cache, url):
    if os.path.exists(cache) == False:
        file = requests.get(url, headers={'User-agent': 'Chrome'}).json()        
        with open(cache, 'w') as f:
            json.dump(file, f)

def main():
    for i in range(0,len(URL_subsribers)):
        checkaddressexists(Cache_subsribers[i], URL_subsribers[i])
        checkaddressexists(Cache_postsbyday[i], URL_postsbyday[i])
    writeposts(sample_1_outputfile, Cache_subsribers)
    writeposts(sample_2_outputfile, Cache_postsbyday)

if __name__ == '__main__':
    main()