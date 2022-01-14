#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 12:06:19 2022

@author: walberto

Advent of code 2021, day 5
"""

# unpaking data
# file = open('example.txt')
file = open('input.txt')
lines = file.readlines()
file.close()

def evol (lista,dias):
    """
    Esta función evolucióna la lista por una cantidad determinada de dias

    """
    lista2 = lista[:]

    for i in range(dias):
        for j in range(len(lista2)):
            pez = lista2[j]
            
            if pez > 0:
                lista2[j] -= 1
                
            if pez == 0:
                lista2[j] = 6
                lista2.append(8)
                
        # print(lista)
        
    return(len(lista2))
                
peces1 = lines[0].split()[0]

peces2 = peces1.split(',')

peces3 = []

for pez in peces2:
    peces3.append(int(pez))
    

# parte 2

def inteli_evol(lista,dias):
    "Esta función evoluciona de manera distinta"
    num0 = lista.count(0)
    num1 = lista.count(1)
    num2 = lista.count(2)
    num3 = lista.count(3)
    num4 = lista.count(4)
    num5 = lista.count(5)
    num6 = lista.count(6)
    num7 = lista.count(7)
    num8 = lista.count(8)
    
    for i in range(dias):
        temp = num0
        num0 = num1
        num1 = num2
        num2 = num3
        num3 = num4
        num4 = num5
        num5 = num6
        num6 = num7 + temp
        num7 = num8
        num8 = temp
        
    total = num0 + num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8
    
    return(total)
    
    

    