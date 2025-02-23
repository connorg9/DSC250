#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 09:11:19 2025

@author: connorgood
"""

#P2.6.3

f = open("/Users/connorgood/Downloads/ex2-6-g-esi-data.txt", "r")

names =[]
radii = []
densities = []
v_esc = []
surf_temp = []
esi = []

weights = [0.57, 1.07, 0.7, 5.58]

biggest = 0.0
big_name = " "

for i in f.readlines()[3:]: #dont use enumerate here, messes with the string modifications later :(
                            #this is a bit weird, but I dont want the first three lines since they are just labels
                            
    line = [line.lstrip() for line in i.split('  ') if line] 
    
    #creates a new list that has no leading whitespace, then splits i (each line) in f by anywhere with two spaces, then only saves the non-empty strings
    #this is basically a line comprehension version of the code provided in the assignment. I did it with repeating code blocks initially and it got tedious
    
    names.append(line[0])
    radii.append(float(line[2]))
    densities.append(float(line[3]))
    v_esc.append(float(line[5]))
    surf_temp.append(float(line[7]))

for i in range(len(names)):
    x = (
            (1 - abs((radii[i] - radii[0]) / (radii[i] + radii[0]))) ** weights[0] * 
            (1 - abs((densities[i] - densities[0]) / (densities[i] + densities[0]))) ** weights[1] * 
            (1 - abs((v_esc[i] - v_esc[0]) / (v_esc[i] + v_esc[0]))) ** weights[2] * 
            (1 - abs((surf_temp[i] - surf_temp[0]) / (surf_temp[i] + surf_temp[0]))) ** weights[3] 
          ) ** (1 / (len(weights)))
    
    esi.append(x)

    #calculates each component of the ESI, then appends it to a final list
    
    print("The ESI of ", "{0: <12}".format(names[i]), "is ", "{0:.4f}".format(esi[i]))  
    
    #use string formatters to make the ESIs all line up, and to 4 decimal places
    

for i in range(len(esi))[1:]:
    if esi[i] > biggest:
        biggest = esi[i]
        big_name = names[i]
    
print("The planet with the largest ESI is '", big_name, "', which has an ESI of", biggest)

