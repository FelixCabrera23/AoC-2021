#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 22:51:52 2021

@author: walberto

Advent of code 2021, day 1
"""

# unpaking data
file = open('input.txt')
lines = file.readlines()
file.close()

measures = []

for data in lines:
    measures.append(int(data))
    
# Part 1, how many increases

x0 = measures[0]

i = 0

for num in measures:
    if num > x0: i += 1
    
    x0 = num
    
print('The number of increases is: ',i)

# Part 2

# measures = [199,200,208,210,200,207,240,269,260,263]
sums_3 = []

increases = 0

i = 0

while i < (len(measures)-3):

    # Aux sum numbers
    A = 0
    B = 0
    
    # iteration numbers
    j = 0
    for j in range(3):
        A = A + measures[i+j]
        B = B + measures[i+1+j]

    if B > A : increases+=1
    sums_3.append(A)
    i+=1

print('The number of increases is: ',increases)
    

    