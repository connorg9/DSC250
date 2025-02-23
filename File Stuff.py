#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 09:43:34 2025

@author: connorgood
"""


#%%

f = open('sample text file.txt', 'wt')
for i in range(1, 10001):
    print(i, i**2, i**3, i**4, sep = ' ', file = f)
    f.close()

#%%

f = open('sample text file.txt', 'r')
for i, line in enumerate(f):
    if i == 4:
        s = line.split(',')
        s = [int(j) for j in s]
        print(sum(s))
        break
f.close()

#%%

f = open("/Users/connorgood/Downloads/redwood-data.txt")

max_d = 0.00
max_h = 0.00

for i, line in enumerate(f):
    if i > 2:
        s = line.split("\t")
        diam = s[2]
        height = s[3][:-2]
        
        if float(diam) > float(max_d):
            name_d = s[0]
            max_d = diam
            
        if float(height) > float(max_h):
            name_h = s[0]
            max_h = height
            
print("The max diameter tree is", name_d, "which is", max_d, "m wide")
print("The max height tree is", name_h, "which is", max_h, "m tall")



