#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 09:44:59 2025

@author: connorgood
"""

'''
1. The output is:
    1st
    3rd
    5th
This code works because suff is the suffixes of each of the numerical "endings". When n changes,
the print statement is formatted such that it will print n, but also a section of suff that is 
extracted using string manipulation. If n is 1, then the string segment is from [2:4], which
means that the second and third character (st) are printed. Because of the way that suff is formatted,
this works for any 0-10 number. 

'''
#%%

#2

# a)
a11 = 1.1
a12 = 1.2
a13 = 1.3
a21 = 2.1
a22 = 2.2
a23 = 2.3
a31 = 3.1
a32 = 3.2
a33 = 3.3

print("[ {0: .1f} {1: .1f} {2: .1f} ]".format(a11, a12, a13))
print("[ {0: .1f} {1: .1f} {2: .1f} ]".format(a21, a22, a23))
print("[ {0: .1f} {1: .1f} {2: .1f} ]".format(a31, a32, a33))

print("\n")
    
# b)

a11 = 1
a12 = 0
a13 = 0
a21 = 0
a22 = 1
a23 = 0
a31 = 0
a32 = 0
a33 = 1

print("[ {0: .1f} {1: .1f} {2: .1f} ]".format(a11, a12, a13))
print("[ {0: .1f} {1: .1f} {2: .1f} ]".format(a21, a22, a23))
print("[ {0: .1f} {1: .1f} {2: .1f} ]".format(a31, a32, a33))

