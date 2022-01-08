#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 12:08:07 2021

@author: walberto

Advent of code 2021, day 5
"""

import numpy as np

# unpaking data
# file = open('example.txt')
file = open('input.txt')
lines = file.readlines()
file.close()

# Generamos la matriz en limpio para hacer el mapa
size = 1000

map_1 = np.zeros((size,size),int)

def fill_lines (x1,y1,x2,y2):
    """
    Esta función llena la matriz mapa con las coordenadas indicadas
    """
    
    if x1 == x2:
        
        if y1 > y2:
            temp = y1
            y1 = y2
            y2 = temp
        
        i = y1
        while i <= y2:
            map_1[i][x1] += 1
            i += 1
    
    if y1 == y2:
        
        if x1 > x2:
            temp = x1
            x1 = x2
            x2 = temp
        
        i = x1
        while i <= x2:
            map_1[y1][i] += 1
            i += 1


            
            
        
            
# llenamos la matriz

for line in lines:
    nums = line.split()
    pA = nums[0].split(',')
    pB = nums[2].split(',')
    x1,y1 = int(pA[0]),int(pA[1])
    x2,y2 = int(pB[0]),int(pB[1])
    
    fill_lines(x1,y1,x2,y2)

points = 0

for line in map_1:
    for ele in line:
        if ele > 1:
            points += 1
            
print(points)

# Parte 2

def fill_diag (x1,x2,y1,y2):
    """
    Esta función llena las diagonales en la matriz
    """
    # Primero ordenamos los puntos segun las x
    if x1 > x2:
        temp = x2
        x2 = x1
        x1 = temp
        temp = y1
        y1 = y2
        y2 = temp
        
        
    if x1 != x2 and y1 != y2:
        i = x1
        j = y1
        while i <= x2:
            map_1[j][i] +=1
            i+=1
            if y1 < y2:
                j+=1
            else:
                j-=1
            
                

for line in lines:
    nums = line.split()
    pA = nums[0].split(',')
    pB = nums[2].split(',')
    x1,y1 = int(pA[0]),int(pA[1])
    x2,y2 = int(pB[0]),int(pB[1])
    
    fill_diag(x1, x2, y1, y2)

points = 0

for line in map_1:
    for ele in line:
        if ele > 1:
            points += 1

print(points)
