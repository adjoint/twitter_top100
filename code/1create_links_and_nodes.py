# -*- coding: utf-8 -*-

import copy
import csv

#here we parse the raw data file and create doesfollow.com links for Octoparse to extract connections from

with open('0top100.csv', 'rb') as f:
    reader = csv.reader(f)
    lines0 = map(list, reader)
lines = copy.deepcopy(lines0)

links = open("links.csv", "w")
nodes = open("nodes.csv", "w")
nodes.write("ID,label,rank\n")

people = []
for i in range(len(lines)):
    if i % 6 == 0:
        rank = lines[i][0]
        grade = lines[i+1][0]
        username = lines[i+2][0].lower()
        tweets = lines[i+3][0].replace(",", "")
        followers = lines[i+4][0].replace(",", "")
        following = lines[i+5][0].replace(",", "")
        people.append(username)
        nodes.write(username + "," + username + "," + rank + "\n")

for p in people:
    for q in people:
        if p < q:
            tow = "https://doesfollow.com/"+p+"/"+q
            #links.write(tow + "\n")

links.close()