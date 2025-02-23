#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 09:07:04 2025

@author: connorgood
"""

#Q2.7.3

"""
The provided code does not work because there is no return statement at the end of the function,
and because the variable is only modified within the function and not globally.
The working alternative is:
"""

balance = 100
def add_interest(balance, rate):
    return balance + balance * rate / 100

for year in range(4):
    balance = add_interest(balance, 5)
    print("Balance after year {}: ${:.2f}".format(year + 1, balance))
    
#%%

#P2.7.5

import numpy as np

g = 9.81

def motion(v, a):
    a = a * (np.pi / 180)
    r = (v**2 * np.sin(2 * a)) / g
    h = (v**2 * ((np.sin(a)) ** 2)) / (2 * g)
    return r, h

result = motion(10, 30)
print("The projectile has range {:.3f} m".format(result[0]), "and max height {:.3f} m".format(result[1]))

#%%

#Homework 6-3
    
def find(file, column, row):
    
    f = open(file, "r")
    
    for i, line in enumerate(f):
        
        if i == 2:
            planet = line.lower()
            planet = planet.split("\t")
            planet = [column.lower().strip() for column in planet]
        
        else:
            label = line.lower()
            label = label.strip()
            label = label.split("\t")
            if row.lower() in label[0] and column.lower() in planet:
                
                index = planet.index(column.lower())
                print("{0} has a {1} of {2}".format(column, label[0], label[index + 1]))
                return
            
    print("Improper name of planet or data selection")
            
find("/Users/connorgood/Downloads/planetary-fact-sheet.txt", "mars", "mass")
find("/Users/connorgood/Downloads/planetary-fact-sheet.txt", "Neptune", "temp")
find("/Users/connorgood/Downloads/planetary-fact-sheet.txt", "Jupiter", "Moons")

    
#%% 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    