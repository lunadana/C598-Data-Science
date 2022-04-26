
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
COMP598 - hw5
Dana Luna - 260857641
Cleaning Data

"""

# Import relevant librairies
import json
import sys
from dateutil import parser
import pytz

data = []
# Helper functions
def title_check(element):
    if ("title" not in element) and ("title_text" not in element) or (("title" in element) and ("title_text" in element)):
        return False
    return True

def time_check(element):
    try:
        element["createdAt"] = parser.parse(element["createdAt"]).astimezone(pytz.utc)
        element["createdAt"] = element["createdAt"].strftime('%Y-%m-%d %H:%M:%S')
    except: 
        return False
    return True

def valid_check(line):
    try:
        json.loads(line)
    except: 
        return False
    return True

def author_check(element):
     if (element["author"] == None) or (element["author"] == "N/A") or (element["author"] == ""):
         return False
     return True

def count_check(element):
     try:
         element["total_count"] = int(element["total_count"])
     except:
         return False
     return True

def tag_check(element):
    new_tags = []
    for word in element["tags"]:
        word_split = word.split(" ")
        for subword in word_split:
            new_tags.append(subword)
    element["tags"] = new_tags
    for i in new_tags:
        if " " in i:
            return False
    if len(new_tags) == 4:
        return True
    return False
        

def main():    
    input_file = sys.argv[2]
    outputfile = sys.argv[4]
    
    # Open input file
    input_file = open(input_file, 'r')
    data_lines = input_file.readlines()
    
    # Iterate in the lines of the files
    for line in data_lines:
        
        # 5. Remove invalid dictionnaries
        if valid_check(line) == True:
            element = json.loads(line)
        else : 
            continue
        
        # 1. Check if contains at least title or title_text
        if title_check(element) == False:
            continue
        
        # 2. For objects with a title_text field, rename the field in the output object to title
        if "title" not in element: element["title"] = element.pop("title_text")
    
        # 3-4. Standardize all createdAt date times to the UTC timezone.
        if (time_check(element) == False) and ("createdAt" in element):
            continue
        
        # 6. Remove the posts with empty author field
        if author_check(element) == False:
            continue
        
        # 7-8. Total counts 
        if count_check(element) == False:
            if "total_count" in element:
                continue
        
        # 9. Tags
        if "tags" in element:
            new_list = []
            for word in element["tags"]:
                list_of_words = word.split(" ")
                for subword in list_of_words:
                    new_list.append(subword)
            element["tags"] = new_list
        
        # If passed all tests, add it to final list
        data.append(element)
    
    # 10. Write to json file
    output_file = open(outputfile, "w")
    for l in data:
        json.dump(l, output_file)
        output_file.write("\n")
    output_file.close()
    
if __name__ == "__main__":
    main()





