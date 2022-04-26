# -*- coding: utf-8 -*-

import json
import sys

input_f = sys.argv[1]

def main():
    list_posts = []
    with open(input_f, 'r') as f:
        for line in f:
            list_posts.append(json.loads(line))
    total = 0
    for post in list_posts:
        total += len(post['data']['title'])
    average = total/len(list_posts)
    print(average)
    return average

if __name__ == '__main__':
    main()