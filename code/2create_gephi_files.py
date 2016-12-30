# -*- coding: utf-8 -*-

import copy
import csv
    
with open('extracted_data.csv', 'rb') as f:
    reader = csv.reader(f)
    lines0 = map(list, reader)
del lines0[0]
lines = copy.deepcopy(lines0)

edges = open("edges.csv", "w")
edges.write("source,target,type\n")


for l in lines:
    u1 = l[0]
    u2 = l[1]
    e12 = l[2]
    e21 = l[3]
    if "yup" in e12:
        edges.write(u1 + "," + u2 + ",directed\n")
    if "yup" in e21:
        edges.write(u2 + "," + u1 + ",directed\n")

edges.close()