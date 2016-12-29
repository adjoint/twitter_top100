# -*- coding: utf-8 -*-

import copy
import csv
import urllib
import time
import requests
import io

"""
f = open("tw.txt", "r")
#print f.readline().split(",")
#print f.readline().replace(" ","").replace("\r", "").replace("\t","").split(",")[4]

edges = io.open("edges_gephi.csv", "w", encoding="utf-8")
#edges.write("source,target,type\n")
data = f.readlines()

for line in data[1:2]:
    #print line
    l = line.decode('utf8').replace(" ","").replace("\r", "").replace("\t","").split(",")
    yup = l[2]#.replace('"', "")
    #print yup
    yup_rev = l[3]#.replace('"', "")
    #print yup_rev

for line in data[1:5]:
    #print line
    l = line.decode('utf8').replace(" ","").replace("\r", "").replace("\t","").split(",")
    u1 = l[0]
    #print u1
    u2 = l[1]
    #print u2
    e12 = l[2]#.replace('"', "")
    #print e12
    e21 = l[3]#.replace('"', "")

    if e12 == yup:
        print 1
        edges.write(u1 + "," + u2 + ",directed\n")
    if e21 == yup_rev:
        print 2
        edges.write(u2 + "," + u1 + ",directed\n")

edges.close()"""
    
with open('extracted_data.csv', 'rb') as f:
    reader = csv.reader(f)
    lines0 = map(list, reader)
del lines0[0]
lines = copy.deepcopy(lines0)

edges = open("edges.csv", "w")
#nodes = open("nodes.csv", "w")
edges.write("source,target,type\n")


for l in lines:
    u1 = l[0]
    u2 = l[1]
    e12 = l[2]
    e21 = l[3]
    if "yup" in e12:
        #print 1
        edges.write(u1 + "," + u2 + ",directed\n")
    if "yup" in e21:
        #print 2
        edges.write(u2 + "," + u1 + ",directed\n")

edges.close()

"""data = open('tw3.csv', 'rb').read()
print data.find('\x00')
print data.count('\x00')
for i, c in enumerate(data):
    if c == '\x00':
        print i, repr(data[i-30:i]) + ' *NUL* ' + repr(data[i+1:i+31])"""
        
"""fi = open('tw3.csv', 'rb')
data = fi.read()
fi.close()
fo = open('mynew.csv', 'wb')
fo.write(data.replace('\x00', ''))
fo.close()"""